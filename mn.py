size_table = 1200
kods = ['N'] * size_table
kods_dict = dict()


def add_symbols(symbols, k):
    # add value k = {0, 1} for everybody symbol of line: symbols
    for a in str(symbols):
        if kods[ord(a)] == 'N':
            kods[ord(a)] = k
        else:
            kods[ord(a)] = k + kods[ord(a)]


def encode_h(code_of_symbol):
    bin_str = str()
    text = open('text.txt', 'r')
    for lines in text:
        for z in lines:
            bin_str = bin_str + code_of_symbol[z]
    rem = []
    bin_str = len(bin_str) % 8 * '0' + bin_str
    for q in range(0, len(bin_str) - 8, 8):
        rem.append(int(bin_str[q: q + 8], 2))
    text.close()
    return rem


class Helper:
    def __init__(self):
        self.freq = None
        self.word = None

    def creat(self, freq, stroka):
        self.freq = freq
        self.word = stroka

    def frequency(self):
        return self.freq

    def st(self):
        return self.word

    def output(self):
        print(self.frequency(), " '", self.st(), "' ", sep='')

    def __add__(self, other):
        add_symbols(str(self.word), '1')
        add_symbols(str(other.word), '0')
        self.freq += other.freq
        self.word += other.word
        return self


def adaptive(line_text, ctf=0):
    # input
    fout_alphabet = open('out_alphabet' + str(ctf)+'.txt', 'w')
    ver_of_symbol = [0] * size_table
    size = 0
    for i in range(size_table):
        kol = line_text.count(chr(i))
        size += kol
        ver_of_symbol[i] += kol

    # output
    for i in range(size_table):
        if ver_of_symbol[i]:
            print('[', chr(i), ']=', ver_of_symbol[i], file=fout_alphabet)

    fout_alphabet.close()

    #  array
    basis = [] * size_table
    for i in range(size_table):
        if ver_of_symbol[i] != 0:
            temp = Helper()
            temp.creat(ver_of_symbol[i] / size, chr(i))
            basis.append(temp)

    # main algorithm
    while len(basis) > 1:
        basis = sorted(basis, key=lambda ed: ed.frequency(), reverse=True)
        tmp1 = basis.pop()
        tmp2 = basis.pop()
        basis.append(tmp1 + tmp2)

    out_codes_s = open('out_codes_of_symbol' + str(ctf)+'.txt', 'w')
    for i in range(len(kods)):
        if kods[i] != 'N':
            kods_dict[chr(i)] = kods[i]
            print(chr(i), kods[i], file=out_codes_s)
    print(bytes(encode_h(kods_dict)))


cmd = ''
ct = 0
out_tx = open('text.txt', 'w')
out_tx.close()
while cmd != 'EXIT':
    out_tx = open('text.txt', 'a')
    print(cmd, file=out_tx, end="")
    out_tx.close()
    adaptive(cmd, ct)
    ct += 1
    cmd = input()
print("It is END")

