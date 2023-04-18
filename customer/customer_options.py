import curses

from customer import buy_motorcycles

customer_options = [
    "Buy Motorcycle"
]


selected_option = 0


def print_options(stdscr, index, options):
    stdscr.clear()
    stdscr.addstr("What do you want to do:\n\n")
    for i, option in enumerate(options):
        radio = "( )" if i != index else "(*)"
        stdscr.addstr(f"{radio} {option}\n")
    stdscr.refresh()


def print_customer_options():
    curses.wrapper(main)
    if selected_option == 0:
        buy_motorcycles.start()


def main(stdscr):
    curses.curs_set(0)
    global selected_option
    print_options(stdscr, selected_option, customer_options)
    while True:
        key = stdscr.getch()
        if key == ord("\n"):  # enter key
            break
        elif key == curses.KEY_UP:
            selected_option = (selected_option - 1) % len(customer_options)
        elif key == curses.KEY_DOWN:
            selected_option = (selected_option + 1) % len(customer_options)
        print_options(stdscr, selected_option, customer_options)