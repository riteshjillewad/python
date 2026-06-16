count = 5

def show_count():
    global count
    # If we don't mention count as global, it cannot be accessed as it is the local varialbe
    # global tells the interpreter to use the global variable count, and not the local one
    count += 1
    print(count)

show_count()