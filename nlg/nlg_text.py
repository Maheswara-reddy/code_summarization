import re
import pickle
import random
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F

# loading the data.
# A simple pickle file as input to load and train the data
pickle_in = open("plots_text.pickle","rb")
movie_plots = pickle.load(pickle_in)

# DATA PREPARATION
def create_seq(text, seq_len = 9):
    sequences = []
# Given seq_len = 9, if length is higher then this
    if len(text.split()) > seq_len:
      for i in range(seq_len, len(text.split())):

        seq = text.split()[i-seq_len:i+1]
        sequences.append(" ".join(seq))

      return sequences
# if the length is smaller than seq_len
    else:
      
      return [text]

seqs = [create_seq(i) for i in movie_plots]

# merging the lists into single one.
seqs = sum(seqs, [])

len(seqs)

x = [] # input
y = [] # target

for s in seqs:
  x.append(" ".join(s.split()[:-1]))
  y.append(" ".join(s.split()[1:]))

int2token = {} #  interger to token dictioary
cnt = 0 # number of tokens in the dictionary

for w in set(" ".join(movie_plots).split()):
  int2token[cnt] = w
  cnt+= 1

token2int = {t: i for i, t in int2token.items()} # token to integer dictionary

token2int["the"], int2token[14271]

vocab_size = len(int2token)
vocab_size


def get_integer_seq(seq):
  return [token2int[w] for w in seq.split()]

# convert text sequences to integer sequences
x_int = [get_integer_seq(i) for i in x]
y_int = [get_integer_seq(i) for i in y]

# convert integer sequence to numpy
x_int = np.array(x_int)
y_int = np.array(y_int)


# MODEL TRAINING
def get_batches(arr_x, arr_y, batch_size):
         
    ite = 0
    for n in range(batch_size, arr_x.shape[0], batch_size):
      x = arr_x[ite:n,:]
      y = arr_y[ite:n,:]
      ite = n
      yield x, y


class WordLSTM(nn.Module):
    
    def __init__(self, n_hidden=256, n_layers=4, drop_prob=0.5, lr=0.01):
        super().__init__()

        self.drop_prob = drop_prob
        self.n_layers = n_layers
        self.n_hidden = n_hidden
        self.lr = lr
        
        self.emb_layer = nn.Embedding(vocab_size, 200) # vocab_size = len(int2token)

        # define the LSTM
        self.lstm = nn.LSTM(200, n_hidden, n_layers, dropout=drop_prob, batch_first=True)
        
        #dropout layer
        self.dropout = nn.Dropout(drop_prob)
        
        #fully connected layer
        self.fc = nn.Linear(n_hidden, vocab_size)      
    
    def forward(self, x, hidden):

        # embedded layer
        embedded = self.emb_layer(x)     
        
        # hidden layer
        lstm_output, hidden = self.lstm(embedded, hidden)
        
        #dropout layer
        out = self.dropout(lstm_output)
        
        #out = out.contiguous().view(-1, self.n_hidden) 
        out = out.reshape(-1, self.n_hidden) 

        out = self.fc(out)

        # final output and hidden state
        return out, hidden
    

    def init_hidden(self, batch_size):

        weight = next(self.parameters()).data

        # if cuda is available
        if (torch.cuda.is_available()):
          hidden = (weight.new(self.n_layers, batch_size, self.n_hidden).zero_().cuda(),
                    weight.new(self.n_layers, batch_size, self.n_hidden).zero_().cuda())
        
        # if cuda is not available
        else:
          hidden = (weight.new(self.n_layers, batch_size, self.n_hidden).zero_(),
                    weight.new(self.n_layers, batch_size, self.n_hidden).zero_())
        
        return hidden

# instantiate the model
net = WordLSTM()


def train(net, epochs=10, batch_size=32, lr=0.001, clip=1, print_every=32):
    
    # optimizer
    opt = torch.optim.Adam(net.parameters(), lr=lr)
    
    # loss
    criterion = nn.CrossEntropyLoss()
    
    counter = 0

    net.train()

    for e in range(epochs):

        h = net.init_hidden(batch_size)
        
        for x, y in get_batches(x_int, y_int, batch_size):
            counter+= 1
            
            # convert numpy arrays to PyTorch arrays
            inputs, targets = torch.from_numpy(x), torch.from_numpy(y)
            
            h = tuple([each.data for each in h])

            # zero accumulated gradients
            net.zero_grad()
            
            output, h = net(inputs, h)
            
            # loss and perform backprop
            loss = criterion(output, targets.view(-1))

            # back-propagate error
            loss.backward()
            
            #prevent the exploding gradient problem in LSTMs
            nn.utils.clip_grad_norm_(net.parameters(), clip)

            # update weights
            opt.step()            
            
            if counter % print_every == 0:
            
              print("Epoch: {}/{}...".format(e+1, epochs), "Step: {}...".format(counter))

# TEXT GENERATION

# Funtion to predict next token
def predict(net, tkn, h=None):
         
  # input tensor
  x = np.array([[token2int[tkn]]])
  inputs = torch.from_numpy(x)

  # hidden state
  h = tuple([each.data for each in h])

  out, h = net(inputs, h)

  # softmax and token probabilities
  p = F.softmax(out, dim=1).data

  p = p.cpu()

  p = p.numpy()
  p = p.reshape(p.shape[1],)

  top_n_idx = p.argsort()[-3:][::-1]

  #random indices
  sampled_token_index = top_n_idx[random.sample([0,1,2],1)[0]]

  return int2token[sampled_token_index], h


# function to generate text
def sample(net, size, prime='it is'):
    
    net.eval()

    h = net.init_hidden(1)

    toks = prime.split()

    # predict next token
    for t in prime.split():
      token, h = predict(net, t, h)
    
    toks.append(token)

    for i in range(size-1):
        token, h = predict(net, toks[-1], h)
        toks.append(token)

    return ' '.join(toks)

# input a = number of words, b = input string
a,b = input().split(maxsplit=1)
print(sample(net,int(a), prime=b))
