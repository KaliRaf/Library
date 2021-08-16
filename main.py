from cli import CLI
from time import sleep

if __name__ == '__main__':
    prog = CLI()
    prog.load_archived_data()
    while True:
        prog.print_menu()
        sleep(1)
        prog.switch()
