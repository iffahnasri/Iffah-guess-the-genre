#!/usr/bin/env python

import random


def main():
    """Start a music game."""
    print("Enchanted is my fav Taylor Swift Song!!!")

    genre = (
        "Country Pop Rock",
        "Country Pop",
        "Electro Pop",
        "Pop rock",
        "Metal",
        "Reggae",
    )

    x = "Country Pop Rock"

    guess = None
    print("This are example of genre:", (genre))
    while x != guess:

        guess = str(input("What genre of my favourite song? "))

        if guess == x:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print(
                "You guessed {}. Unfortunately its not the answer. Hint:a style of music that combines elements of traditional country songs and mainstream pop music".format(
                    guess
                )
            )


main()
