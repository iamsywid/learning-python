def new_line():
    print('.')


def three_lines():
    new_line()
    new_line()
    new_line()


def nine_lines():
    three_lines()
    three_lines()
    three_lines()


def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()


print('Printing nine lines')
nine_lines()

print('Calling clear_screen()')
clear_screen()
