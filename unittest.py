class Utils:
    def reversed(num):
        return int(str(num)[::-1])

    def formatter(num):
        return bin(num)[2:],oct(num)