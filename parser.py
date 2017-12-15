#!/usr/bin/env python3
import sys

LITERALS = ''.join(chr(x) for x in range(128))

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
    
def isLiteral(token, literals):
    return token != '`' and token != '~' and token in literals

def exp(tokens, pos):
    if tokens[pos] == '`':
        pos = match(tokens[pos], ['`'], pos)
        pos = fun(tokens, pos)
        return arg(tokens, pos)
    else:
        error(pos, tokens[pos])
def fun(tokens, pos):
    if tokens[pos] == 'K':
        return match(tokens[pos], ['K'], pos)
    elif tokens[pos] == 'S':
        return match(tokens[pos], ['S'], pos)
    elif tokens[pos] == 'I':
        return match(tokens[pos], ['I'], pos)
    elif tokens[pos] == 'O':
        return match(tokens[pos], ['O'], pos)
    elif tokens[pos] == 'W':
        return match(tokens[pos], ['W'], pos)
    elif tokens[pos] == 'N':
        return match(tokens[pos], ['N'], pos)
    elif tokens[pos] == '`':
        return exp(tokens, pos)
    else:
        error(pos, tokens[pos])
def arg(tokens, pos):
    if tokens[pos] == '`':
        return exp(tokens, pos)
    elif tokens[pos] == '~':
        return match(tokens[pos], ['~'], pos)
    elif isLiteral(tokens[pos], LITERALS):
        return lit(tokens, pos)
    else:
        error(pos, tokens[pos])
def lit(tokens, pos):
    if isLiteral(tokens[pos], LITERALS):
        return match(tokens[pos], LITERALS, pos)
    else:
        error(pos, tokens[pos])

if __name__ == "__main__":
    main()
