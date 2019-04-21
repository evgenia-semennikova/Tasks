def read_input():
    pattern = input()
    text = input()
    return pattern, text


def calc_h(string, x, p):
    """ Calculates hash for string directly """

    length = len(string)
    res = 0
    for i in reversed(string):
        res = ((res * x) % p + ord(i) % p) % p
    return res


def fill_hash_table(text, len_p, x, p):
    len_text = len(text)
    x_p = pow(x, len_p - 1, p)
    h_text = [0] * (len_text - len_p + 1)
    h_text[-1] = calc_h(text[len_text - len_p:], x, p)
    for i in reversed(range(len_text - len_p)):
        h_text[i] = ((((h_text[i + 1] - ((ord(text[i + len_p]) % p) * x_p) % p + p) % p) * x) % p
                     + ord(text[i]) % p) % p
    return h_text


def find_pattern(pattern, text):
    p = 1000000007
    x = 263
    len_text = len(text)
    len_p = len(pattern)
    h_pattern = calc_h(pattern, x, p)
    h_text = fill_hash_table(text, len_p, x, p)
    return [i for i in range(len_text - len_p + 1)
            if h_pattern == h_text[i] and text[i:i + len_p] == pattern]


def main():
    pattern, text = read_input()
    print(*find_pattern(pattern, text))


if __name__ == "__main__":
    main()