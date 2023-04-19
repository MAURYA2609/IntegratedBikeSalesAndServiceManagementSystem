import curses
import connector
import customer.customer_options

stdscr = curses.initscr()
def start():
    read_bike()


def read_bike():
    conn = connector.connect_to_database()
    cur = conn.cursor()

    cur.callproc('select_all_bikes')
    results = cur.fetchall()

    conn.close()

    curses.wrapper(main, results)


def print_options(stdscr, index, results):
    stdscr.clear()
    stdscr.addstr("Which bike do you want to select:\n\n")
    for i, result in enumerate(results):
        if result[1] == 1:
            radio = "( )" if i != index else "(*)"
            bike_data = f"{result[0]} - {result[2]} ({result[3]})"
            stdscr.addstr(f"{radio} {bike_data}\n")
    stdscr.refresh()



def main(stdscr, results):
    curses.curs_set(0)
    global selected_option
    selected_option = 0
    print_options(stdscr, selected_option, results)
    while True:
        key = stdscr.getch()
        if key == ord("\n"):  # enter key
            break
        elif key == curses.KEY_UP:
            selected_option = (selected_option - 1) % len(results)
        elif key == curses.KEY_DOWN:
            selected_option = (selected_option + 1) % len(results)
        print_options(stdscr, selected_option, results)

        selected_bike = results[selected_option]
        proceed_to_buy(selected_bike)


def proceed_to_buy(selected_bike):
    print(selected_bike)
    conn = connector.connect_to_database()
    cur = conn.cursor()
    cur.callproc('update_bike_availability', (selected_bike[0],))
    key = stdscr.getch()
    cur.close()
    conn.commit()
    if key == ord("\n"):  # enter key
        customer.customer_options.print_customer_options()

