import curses
from admin import insurance_company
from admin import handle_employees
from admin import handle_showrooms
from admin import handle_bikes

admin_options = [
    "Insurance Company",
    "Handle Bikes",
    "Handle Employees",
    "Handle Showrooms"
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
        insurance_company.start()
    elif selected_option == 1:
        handle_bikes.start()
    elif selected_option == 2:
        handle_employees.start()
    elif selected_option == 3:
        handle_showrooms.start()


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

