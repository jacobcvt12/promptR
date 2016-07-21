from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from pygments.lexers import RConsoleLexer

def main():
    history = InMemoryHistory()

    while True:
        text = prompt("> ", lexer=RConsoleLexer, history=history)
        print("You Entered:", text)
    print('GoodBye!')

if __name__ == '__main__':
    main()
