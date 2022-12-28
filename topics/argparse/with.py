import argparse

parser = argparse.ArgumentParser(description='Nice printer')
parser.add_argument('explanation', type=str, help='Explanation')
parser.add_argument('-r', '--expression', type=str, required=True, help='Expression to show')
parser.add_argument('-w', '--width', type=int, default=0, help='Explanation width')
group = parser.add_mutually_exclusive_group()
group.add_argument('-d', '--double', action='store_true', help='Add empyt space')
group.add_argument('-t', '--triple', action='store_true', help='Add more empty space')
args = parser.parse_args()

def nice_print(explanation, expression, width):
    str = explanation + ': '
    print(f'{str.ljust(len(str) if width < len(str) else width)}{expression}')


if __name__ == '__main__':
    if args.double: args.width = 2 * len(args.explanation)
    elif args.triple: args.width = 3 * len(args.explanation)
    nice_print(args.explanation, args.expression, args.width)