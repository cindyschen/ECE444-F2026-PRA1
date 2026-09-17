class Utils:
    def reversed(num):
        if not isinstance(num, int):
            raise TypeError("Input must be an int")
        return int(str(num)[::-1])

    def formatter(num):
        if not isinstance(num, int):
            raise TypeError("Input must be an int")
        return bin(num),oct(num)