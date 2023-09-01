from prompt_toolkit import prompt
import csv
import random

phrases = []
count = 0


def initialze_dictionary():
    with open('basic-italian-phrases.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            phrases.append([row[0], row[1]])


def get_random_italian_phrase():
    phrase_index = random.randint(0, len(phrases) - 1)
    print(phrases[phrase_index])


def next_phrase():
    global count
    print(phrases[count])
    if count >= len(phrases) - 1:
        count = 0
    else:
        count += 1


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
