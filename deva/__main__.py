import sys
from .build import build
# from .funcmodule import my_function
def main():
    args = sys.argv[1:]
    
    for arg in args:
        if arg == 'build':
            build()

if __name__ == '__main__':
    main()