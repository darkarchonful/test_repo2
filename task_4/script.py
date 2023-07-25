for x in range(10):
	print(x)
print('end')

from random import randint
from sys import stderr
from time import sleep

def main():
    while True:
        value = randint(-2,2)

        try:
            sleep(value)
        except ValueError as e:
            print(e)
            continue
        print(f"Random value is {value}")

main()
