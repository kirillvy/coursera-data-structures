# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def hash(pattern, prime, multiplier):
    rpattern = 0
    for c in reversed(pattern):
        rpattern = ((rpattern * multiplier + ord(c)) % prime)
    return rpattern


def prehash(text, length, prime, multiplier):
    H = [None] * (len(text) - length + 1)
    S = text[len(text)-length:len(text)]
    H[len(text) - length] = hash(S, prime, multiplier)
    y = 1
    for i in range(length):
        y = (y * multiplier) % prime
    # print(y)
    for i in reversed(range(len(text) - length)):
        H[i] = (multiplier * H[i+1] + ord(text[i]) - y * ord(text[i+length])) % prime
    # print(H)
    return H



def get_occurrences(pattern, text):
    prime = 175549469
    multiplier = 269
    H = prehash(text, len(pattern), prime, multiplier)
    hpattern = hash(pattern, prime, multiplier)
    # print(hpattern)

    return [
        i 
        for i in range(len(text) - len(pattern) + 1)
        if hpattern == H[i] and text[i:i + len(pattern)] == pattern
    ]

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

