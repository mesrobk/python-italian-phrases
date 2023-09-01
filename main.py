from prompt_toolkit import prompt
import csv
import random

phrases = []
count = 0


def initialze_dictionary():
    pass
    # todo: read from csv file 'basic-italian-phrases.csv' and add each row to the array phrases


def get_random_italian_phrase():
    pass
    # todo: generate random index and print the row from the phrases array


def next_phrase():
    global count
    # todo: Print each row from the phrases array and increment count index


def main():
    print("Let's start learning Italian!")
    initialze_dictionary()
    while True:
        text = prompt(
            'Would you like random phrases or to follow a list? (random/list) ')
        if text == "random":
            get_random_italian_phrase()
            while True:
                text = prompt(
                    'Would you like another phrase (y/n)? ')
                if text == 'y':
                    get_random_italian_phrase()
                else:
                    break
        elif text == "list":
            next_phrase()
            while True:
                text = prompt(
                    'Would you like another phrase (y/n)? ')
                if text == 'y':
                    next_phrase()
                else:
                    break
        else:
            print("Ciao bellissima!")
            break


if __name__ == '__main__':
    main()
