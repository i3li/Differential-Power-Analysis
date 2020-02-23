import sys

_PASSWORD = 'abcdabcdabcdabcd'


def login(password):
    return password == _PASSWORD


def main():
    if (len(sys.argv) == 2):
        password = sys.argv[1]
        print(login(password))
    else:
        print('Usage: login_simulator password')


if __name__ == '__main__':
    main()
