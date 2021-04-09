# ЛРП
class LFSR:
    def __init__(self, x, s):
        self.x = self.__num_to_bin_list(x)
        self.s = self.__list_to_num(self.__num_to_bin_list(s))

    @staticmethod
    def __num_to_bin_list(num: int):
        return [int(i) for i in bin(num)[2:]][::-1]

    @staticmethod
    def __list_to_num(lnum: list):
        res = 0
        for i in range(0, len(lnum) - 1):
            res = (res + lnum[i]) * 2
        return res + lnum[-1]

    def generate(self):
        res = list()
        len_x = len(self.x)
        lfsr = self.s
        bit = 0
        for j in range(1, len_x):
            if self.x[j] != 0:
                bit ^= (lfsr >> (len_x - 1 - j)) % 2 ** (len_x - 1)
        res = lfsr % 2
        self.s = ((lfsr >> 1) | (bit << len_x - 2)) % 2 ** (len_x - 1)
        return res
