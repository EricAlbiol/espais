# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    state = "Practica els problemes de list comprehensions per a ser més Pythonic!"

    espai =  [i for i in state if i in ' ']
    print(len(espai))
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
