def open_and_print_file(file):
    with open(file, "r") as opened_file:
        for line in opened_file:
            print(line.rstrip("\n"))

open_and_print_file("order.txt")