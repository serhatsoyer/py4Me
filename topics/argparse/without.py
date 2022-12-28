def nice_print(explanation, expression, width=0):
    str = explanation + ': '
    print(f'{str.ljust(len(str) if width < len(str) else width)}{expression}')


if __name__ == '__main__': nice_print('without', 1)