from lfsr import LFSR
from shrinking import SelfShrinking


def encrypt(filename, key):
    data = None
    with open(filename, 'rb') as file:
        data = file.read()
    lfsr = LFSR(x, key)
    self_sh = SelfShrinking(lfsr, 8 * len(data))
    seq = self_sh.generate()
    with open('encrypt.txt', 'wb') as file:
        for i in range(0, len(seq), 8):
            # print(seq[i:i+8])
            symb = ''.join(str(e) for e in seq[i:i+8])
            symb = int(symb, 2)
            symb = (symb ^ data[i//8]).to_bytes(1, byteorder="big")
            file.write(symb)


if __name__ == "__main__":
    x = 2**64 + 27      # многочлен
    s = 9348798729764   # начальное заполнение (пароль)

    print('Выберите действие:\n\t1. Сгенерировать последовательность при помощи самосжимающего генератора'
          '\n\t2. Зашифровать файл при помощи поточной криптосистемы с использованием гаммы')
    choose = int(input("<<"))
    if choose == 1:
        L = int(input('введите длину последовательности: '))
        lfsr = LFSR(x, s)
        self_sh = SelfShrinking(lfsr, L)
        res = self_sh.generate()
        print(' --- Сгенерированная последовательнось ---\n', res, '\n\nпоследовательность записана в файл seq.txt')
        with open('seq.txt', 'w') as file:
            cnt = 0
            for item in res:
                file.write("%s " % item)
                if cnt == 79:
                    file.write("\n")
                    cnt = 1
                else:
                    cnt += 1
    elif choose == 2:
        filename = input("Введите имя файла: ")
        key = int(input("Введите ключ: "))
        encrypt(filename, key)
    else:
        print("Выход")
