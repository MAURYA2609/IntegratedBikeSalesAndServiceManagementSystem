import curses
from admin import InsuranceCompany

admin_options = [
    "Insurance Company",
    "Handle Bikes",
    "Handle Employees"
]

selected_option = 0


def print_options(stdscr, index, options):
    stdscr.clear()
    stdscr.addstr("What do you want to do:\n\n")
    for i, option in enumerate(options):
        radio = "( )" if i != index else "(*)"
        stdscr.addstr(f"{radio} {option}\n")
    stdscr.refresh()


def print_admin_options():
    curses.wrapper(main)
    if selected_option == 0:
        InsuranceCompany.start()
    elif selected_option == 1:
        print("Selected option: Handle Bikes")
        # handle Handle Bikes functionality
    elif selected_option == 2:
        print("Selected option: Handle Employees")
        # handle Handle Employees functionality


def main(stdscr):
    curses.curs_set(0)
    global selected_option
    print_options(stdscr, selected_option, admin_options)
    while True:
        key = stdscr.getch()
        if key == ord("\n"):  # enter key
            break
        elif key == curses.KEY_UP:
            selected_option = (selected_option - 1) % len(admin_options)
        elif key == curses.KEY_DOWN:
            selected_option = (selected_option + 1) % len(admin_options)
        print_options(stdscr, selected_option, admin_options)
