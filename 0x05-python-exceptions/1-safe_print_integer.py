def safe_print_integer(value):
    while True:
        try:
            x = int(value)
            print("{:d}".format(value))
            return True
        except ValueError:
            return False
