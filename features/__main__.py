import sys
from .build import build

def main():
    args = sys.argv[1:]
    
    for arg in args:
        argument, value = arg.split(sep='=')
        if argument == 'build':
            build(value)

if __name__ == '__main__':
    main()