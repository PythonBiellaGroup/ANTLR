# ANTLR4 Tutorial - Python example

Example taken from 
https://github.com/gabriele-tomassetti/antlr-mega-tutorial/tree/master/antlr-python

The commands you need to know:
```
# to generate parser and lexer
java org.antlr.v4.Tool -Dlanguage=Python3 Chat.g4
# to execute the program
# there will be nothing on stdout: read output.html to see the results
python antlr.py input.txt
# to run the tests
python -m unittest discover -s . -p ChatTests.py
```