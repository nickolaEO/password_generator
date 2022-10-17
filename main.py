import random
import secrets
import string


def using_random_lib(chars, length, quantity):
    for i in range(quantity):
        password = random.sample(set(chars), length)
        print(''.join(password))


def using_secrets_lib(chars, length, quantity):
    for i in range(quantity):
        password = ''.join(secrets.choice(chars) for i in range(length))
        print(password)


def main(mode):
    password_length = int(input('\nEnter the length of password: '))

    passwords_quantity = int(input('\nHow many passwords to generate: '))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    summary = lower + upper + numbers + symbols

    print('\nTake your passwords: ')

    if mode == '1':
        using_random_lib(summary, password_length, passwords_quantity)
    if mode == '2':
        using_secrets_lib(summary, password_length, passwords_quantity)


if __name__ == '__main__':
    print('\n=====GENERATE YOUR UNIQUE STRONG PASSWORD=====')
    print('\nThe program uses two modes for generating passwords.'
          '\n>>>"MODE 1" uses standard algorithm by random python module.'
          '\n   This module implements pseudo-random number generators.'
          '\n>>>"MODE 2" uses the secrets module used for generating '
          '\n   cryptographically strong random numbers suitable for '
          '\n   managing data such as passwords, account authentication, '
          '\n   security tokens, and related secrets.')
    generator_mode = input('\nChoose generator mode (press number 1 or 2): ')
    main(generator_mode)
