#!/usr/bin/env python3

# list of numbers I might be thinking of
a=[3, 5, 7, 11]

# reply if guess is correct
b= "GET OUT OF MY HEAD! You genius!"

# reply if incorrect

c= "My mind is like a fortress! Wrong, sucka!"

d= "...Nvm, I'm listening"


def main():
    guess= int(input("What number am I thinking of?"))

    if guess in a:
        print (b)
   # elif guess:
   #     print (d)
    else:
        print (c)

main()
