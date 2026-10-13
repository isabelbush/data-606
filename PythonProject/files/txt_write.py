def update_file(file, order_item):
    with open(file, "a") as opened_file:
        opened_file.write(order_item + "\n")

update_file("order.txt", "butter")