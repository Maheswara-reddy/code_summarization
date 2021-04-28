# Code Summarizer

## _Making the developer's job easier_

________________________________________________________________________________________________________________________

A Code Summarizer is a software tool tasked with generating readable summaries that describe the functionality of software.
This is a new approach in code summarization techniques.

#### Installation:
    $ git clone https://github.com/Maheswara-reddy/code_summarization.git


#### Enviroment setup
    pip3 install -r requirements.txt
All the requirements are list in the requirements file.


#### Run the code
    make run

Run the above command and give the input file.

#### Currently observed approaches:
| Method | Paper |
| ------ | ------ |
| Neural Code Sum | [ paper ](https://arxiv.org/pdf/1811.07234.pdf3) |
| Tree Transformer | [ paper ](https://arxiv.org/pdf/2002.08046) |
| Reiter and Dale | [ paper ](http://www3.nd.edu/~cmc/papers/mcburney_tse15.pdf) |

#### Our approach: 
- Passing the code through a lexical analyser.
- Generate sentences from the lexemes.
- Pass the sentences through a summarizer.

#### Technologies used:
- [python3] - Version 3.8.5
- [nltk] - natural language tool kit
- [Beautiful Soup] - bs4 
- [makefile] - running the software tool.


