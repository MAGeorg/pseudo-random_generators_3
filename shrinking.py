# самосжимающий генератор
class SelfShrinking:
    # на вход ЛРП и длина генерируемой последовательности
    def __init__(self, lfsr, L):
        self.lfsr = lfsr
        self.L = L

    def generate(self):
        result = list()
        i = 0
        while i < self.L:
            symbol = str(self.lfsr.generate()) + str(self.lfsr.generate())
            if symbol == '10':
                result.append(0)
                i += 1
            elif symbol == '11':
                result.append(1)
                i += 1
        return result
