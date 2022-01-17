class Converters:
    @staticmethod
    def dec_to_bin(value: float):
        return f"{bin(value)[2:]}"

    @staticmethod
    def bin_to_dec(string):
        return int(string, 2)

    @staticmethod
    def bin_to_gray(string):
        binary = Converters.bin_to_dec(string)
        binary ^= (binary >> 1)
        return bin(binary)[2:]

    @staticmethod
    def gray_to_bin(string):
        n = Converters.bin_to_dec(string)
        mask = n
        while mask != 0:
            mask >>= 1
            n ^= mask
        return bin(n)[2:]

    @staticmethod
    def gray_to_dec(string):
        binary = Converters.gray_to_bin(string)
        value = Converters.bin_to_dec(binary)
        return value

    @staticmethod
    def dec_to_gray(value, chromosome_size):
        binary = Converters.dec_to_bin(value)
        string = Converters.bin_to_gray(binary).zfill(chromosome_size)
        return f"{string}"
