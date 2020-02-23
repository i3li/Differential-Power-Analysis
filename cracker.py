import timeit
import textwrap
from collections import Counter


def guess_password_length():

    def step():
        MAX_LENGTH = 100
        costs = []
        for length in range(0 + 1, MAX_LENGTH + 1):
            setup = textwrap.dedent(f'''
                from login_simulator import login
                password = '{'x' * length}'
            ''')
            stmt = textwrap.dedent(f'''
                login(password)
            ''')
            exec_time = timeit.timeit(stmt, setup, number=100)
            costs.append(exec_time)
        length = costs.index(max(costs)) + 1
        return length

    repeats = 100
    return Counter(
            [step() for _ in range(repeats)]
        ).most_common(1)[0][0]


def main():
    length = guess_password_length()
    print(f'Gussed length: {length}')


if __name__ == '__main__':
    main()
