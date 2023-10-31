from termcolor import colored
from noise import pnoise2

import random
import sys
import os


def generate_pattern(cols=10, rows=10, noise=10):
    data = [" ", ".", "-", "#", "!", "$", "!", "#", ".", " "]
    seed = random.randint(0, 100)
    pattern = ""
    for row in range(rows):
        for col in range(cols):
            n = pnoise2(row/rows, col/cols, base=seed)
            n *= noise
            n = round(n)
            n = n % len(data)

            pattern += data[n]
        pattern += "\n"
    return pattern


def ask_for_number(question):
    tries = 0
    while True:
        try:
            answer = input(colored(question + "\n", "yellow"))
        except:
            pass
        else:
            if answer == "quit":
                sys.exit()
            elif answer.isnumeric():
                return int(answer)
            else:
                print(colored("Oops this didn't make sense", "red"))


def main():
    cols = ask_for_number("How many cols?")
    row = ask_for_number("How many rows?")
    os.makedirs("outputs", exist_ok=True)
    noise_level = [5, 10, 20, 50, 100, 250, 500]
    counter = 0
    for i in noise_level:
        output = generate_pattern(cols, row, i)
        filename = os.path.join("outputs", f"output_n_{counter}.txt")
        counter += 1
        with open(filename, "w") as file:
            file.write(output)


if __name__ == "__main__":
    main()
