import login
import curses


options = [
    "Login",
    "Signup",
    "Exit the application."
]

selected_option = 0


def print_options(stdscr, index):
    stdscr.clear()
    stdscr.addstr("What do you want to do:\n\n")
    for i, option in enumerate(options):
        radio = "( )" if i != index else "(*)"
        stdscr.addstr(f"{radio} {option}\n")
    stdscr.refresh()


def proceed_login():
    curses.wrapper(main)
    if selected_option == 0:
        login.do_login()
    elif selected_option == 1:
        login.do_signup()
    elif selected_option == 2:
        print("Thank you for using our system.")
        return

        

def main(stdscr):
    curses.curs_set(0)
    global selected_option
    print_options(stdscr, selected_option)
    while True:
        key = stdscr.getch()
        if key == ord("\n"):  # enter key
            break
        elif key == curses.KEY_UP:
            selected_option = (selected_option - 1) % len(options)
        elif key == curses.KEY_DOWN:
            selected_option = (selected_option + 1) % len(options)
        print_options(stdscr, selected_option)
