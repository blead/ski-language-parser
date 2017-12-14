import sys

def main():
    if len(sys.argv) == 0:
        print("Usage: python parser.py [FILE]")
        print("Parse the source code in FILE.")
    if len(sys.argv) < 2:
        print("Usage: python {} [FILE]".format(sys.argv[0]))
        print("Parse the source code in FILE.")
        return 0
    filename = sys.argv[1]
    with open(filename) as source:
        tokens = source.read().replace('\n', ' ').strip().split(' ')
        try:
            parse(tokens)
            print("Source code parsed successfully")
        except Exception as e:
            print(e)

def parse(tokens):
    exp(tokens, 0)

def match(token, matches, pos):
    if token in matches:
        return pos + 1
    else:
        error(pos, token)

def error(pos, token):
    raise Exception("Invalid character at position {}: {}".format(pos, token))

def exp(tokens, pos):
    if tokens[pos] == '`':
        pos = match(tokens[pos], ['`'], pos)
        return fun(tokens, pos)
    elif tokens[pos] == 'X':
        return match(tokens[pos], ['X'], pos)
    else:
        error(pos, tokens[pos])
def fun(tokens, pos):
    if tokens[pos] == 'I' or tokens[pos] == 'W' or tokens[pos] == 'N':
        return one(tokens, pos)
    elif tokens[pos] == 'K' or tokens[pos] == 'O':
        return two(tokens, pos)
    elif tokens[pos] == 'S':
        return thr(tokens, pos)
    elif tokens[pos] == '`' or tokens[pos] == 'X':
        return exp(tokens, pos)
    else:
        error(pos, tokens[pos])
def one(tokens, pos):
    if tokens[pos] == 'I':
        pos = match(tokens[pos], ['I'], pos)
        return fun(tokens, pos)
    elif tokens[pos] == 'W':
        pos = match(tokens[pos], ['W'], pos)
        return fun(tokens, pos)
    elif tokens[pos] == 'N':
        pos = match(tokens[pos], ['N'], pos)
        return fun(tokens, pos)
    else:
        error(pos, tokens[pos])
def two(tokens, pos):
    if tokens[pos] == 'K':
        pos = match(tokens[pos], ['K'], pos)
        pos = fun(tokens, pos)
        return fun(tokens, pos)
    elif tokens[pos] == 'O':
        pos = match(tokens[pos], ['O'], pos)
        pos = lit(tokens, pos)
        return fun(tokens, pos)
    else:
        error(pos, tokens[pos])
def thr(tokens, pos):
    if tokens[pos] == 'S':
        pos = match(tokens[pos], ['S'], pos)
        pos = fun(tokens, pos)
        pos = fun(tokens, pos)
        return fun(tokens, pos)
    else:
        error(pos, tokens[pos])
def lit(tokens, pos):
    literals = ''.join(chr(x) for x in range(128))
    if tokens[pos] in literals:
        return match(tokens[pos], literals, pos)
    else:
        error(pos, tokens[pos])

if __name__ == "__main__":
    main()
