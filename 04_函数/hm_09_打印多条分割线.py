def print_line(char, times):
    """打印单条分割线"""

    print(char * times)

def print_lines(char, times):
    """
    打印多条分割线
    """


    row = 0

    while row < 5:

        print_line(char, times)

        row += 1

print_lines('-',24)