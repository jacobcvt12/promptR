from __future__ import unicode_literals
from prompt_toolkit import prompt

def main():
    text = prompt("> ")
    print("You Entered:", text)

if __name__ == '__main__':
    main()
