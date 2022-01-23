##############################################################
#                                                            #
#                                                            #
#        PASSWORD GENERATOR MADE BY ANTONIO LOURENCOS        #
#                                                            #
#                                                            #
##############################################################

import sys
import os
from random import randint as random


class ColorsBash:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'


class PasswordGenerator:

    #
    # run can be 'one' or 'multiple'
    #

    def __init__(self, process: str = 'multiple', passwordLen: int = 8):
        self.passwordLen = passwordLen
        self.process = process

        self.lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                          'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.upperCase = self.__upperCaseGenerator__()
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.specialCharacters = ['!', '@', '#', '$', '%', '^', '&', '*',
                                  '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ',', '.']
        self.AllChacters = [self.lowerCase, self.upperCase,
                            self.numbers, self.specialCharacters]

        self.__main__()

    def __main__(self):
        os.system('clear')
        print(f'{ColorsBash.OKGREEN}Checking arguments...')

        while True:
            if self.process == 'one' or self.process == 'multiple':
                break

            print(f'{ColorsBash.FAIL}Failed: Please use a expected value: {ColorsBash.WARNING}multiple {ColorsBash.FAIL}or {ColorsBash.WARNING}one{ColorsBash.FAIL}.')
            self.process = input(
                f"{ColorsBash.FAIL}Which of this options do you want to use: {ColorsBash.WARNING}").lower()

        print(f'{ColorsBash.OKGREEN}Checked!')
        print(f'{ColorsBash.OKGREEN}Starting process {self.process}.')

        if self.process == 'one':
            self.__createOne__()
        else:
            self.__createMultiple__()
        print(f'{ColorsBash.OKGREEN}Thank you!')

    def __upperCaseGenerator__(self):
        return list(map(lambda fragment: fragment.upper(), self.lowerCase))

    def __generatePassword__(self):
        fragmentPasswordGenerated: list = list()
        passwordGenerated: str = str()

        while True:
            if len(fragmentPasswordGenerated) == self.passwordLen:
                break

            IndexFromAllCharactersRandom = random(0, 3)
            listNewRandom = self.AllChacters[IndexFromAllCharactersRandom]
            newFragment = listNewRandom[random(0, len(listNewRandom) - 1)]

            if len(fragmentPasswordGenerated) <= self.passwordLen:
                if len(fragmentPasswordGenerated) == 0:
                    fragmentPasswordGenerated.append(newFragment)
                elif fragmentPasswordGenerated[-1] != newFragment:
                    fragmentPasswordGenerated.append(newFragment)

        passwordGenerated = str().join(fragmentPasswordGenerated)
        return passwordGenerated

    def __saveOne__(self, password: str):
        file = open(file="generatedPasswords.txt", mode='w+', encoding='utf8')
        file.truncate()
        file.writable()
        file.write(f'{password}\n')
        file.close()

    def __saveMultiple__(self, passwords: list):
        file = open(file="generatedPasswords.txt", mode='w+', encoding='utf8')
        file.truncate()
        file.writable()
        for password in passwords:
            file.write(f'{password}\n')
        file.close()

    def __createOne__(self):
        print(f'{ColorsBash.OKGREEN}Ok, getting started with creating a password.')
        generatedPassword = self.__generatePassword__()
        print(f'{ColorsBash.OKGREEN}The System created 1 password.')
        print(f'{ColorsBash.OKGREEN}Starting the password saving process.')
        self.__saveOne__(generatedPassword)
        print(f'{ColorsBash.OKGREEN}The System Saved the password')

    def __createMultiple__(self):
        while True:
            questionQuantity = input(
                f'{ColorsBash.OKGREEN}How many passwords do you want to generate? {ColorsBash.WARNING}')

            if questionQuantity.isnumeric() and int(questionQuantity) > 1:
                quantity = int(questionQuantity)
                break

            print(
                f'{ColorsBash.FAIL}Failed: Please send a positive number must be greater than 1')

        print(
            f'{ColorsBash.OKGREEN}Ok, starting the process of creating passwords ({quantity})')

        rounds: int = int(1)
        generatedPassword: list = list()
        while quantity >= rounds:
            generatedPassword.append(self.__generatePassword__())
            rounds += 1

        print(f'{ColorsBash.OKGREEN}The System created {quantity} passwords.')
        print(f'{ColorsBash.OKGREEN}Starting the passwords saving process.')
        self.__saveMultiple__(generatedPassword)
        print(f'{ColorsBash.OKGREEN}The System Saved the passwords')


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1] == "customParams":
        while True:

            process = input(
                f"{ColorsBash.OKGREEN}How many passwords do you want to? (one or multiple){ColorsBash.WARNING} ").lower()
            print(f"{ColorsBash.WARNING}The number must be greater than or equal 8")
            passwordLen = input(
                f"{ColorsBash.OKGREEN}Length of password:{ColorsBash.WARNING} ").lower()

            if process == "one" or process == "multiple" and passwordLen.isnumeric() and int(passwordLen) >= 8:
                sys.argv[1] = process
                if len(sys.argv) == 2:
                    sys.argv.append(int())

                sys.argv[2] = passwordLen
                break

    if len(sys.argv) == 2:
        PasswordGenerator(process=sys.argv[1])

    elif len(sys.argv) >= 3:
        while True:
            if sys.argv[2].isnumeric() and int(sys.argv[2]) >= 8:
                sys.argv[2] = int(sys.argv[2])
                break

            print(f"{ColorsBash.WARNING}The number must be greater than or equal 8")
            sys.argv[2] = input(
                f"{ColorsBash.OKGREEN}Inform a number:{ColorsBash.WARNING}")

        PasswordGenerator(process=sys.argv[1], passwordLen=sys.argv[2])

    else:
        PasswordGenerator()
