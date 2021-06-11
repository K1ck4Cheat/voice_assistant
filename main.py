import greeting_module as gm
import file_actions as fa
import os


def main():
    
    clear = lambda: os.system('cls') 
    gm.greeting()


if __name__ == '__main__':
    main()
