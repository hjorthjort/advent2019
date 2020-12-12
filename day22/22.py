import re

with open('input.txt') as f:
    inp = f.read()

inp = [ re.compile('([-0-9]+)').split(x) for x in inp.splitlines()]


def shuffle(instr, pos, length):
    typ = instr[0]
    if typ == 'deal into new stack':
        return -(pos + 1)
    if typ == 'cut ':
        x = int(instr[1])
        return (pos - x)
    if typ == 'deal with increment ':
        x = int(instr[1])
        return (pos * x)
    raise Exception()


pos = 2019
Y = sym.Symbol('Y')
pos = Y
length = 10007
for instr in inp:
    pos = shuffle(instr, pos, length)

print(sym.collect_const(pos % length).subs(Y, 2019))

# Part 2
# The length is prime.
# So we are working in a prime field.
# Addition, subtraction and multiplication work like normal.
# Instead of division, we have multiplication by the multiplicative inverse.

length = 119315717514047


def pow(a, b):
    """Fast exponentiation algorithm in the prime field for `length`.
    returns a^b mod length
    """
    if b == 0:
        return 1
    rem = pow(a**2 % length, b // 2) % length
    if b % 2 == 1:
        return a * rem
    return rem


def inv(x):
    """Inverse of x in the `length` prime field.

    By Fermat's Little theorem, a^p == a mod p.
    So a^(-1) == a*a^(-2) == a^(p-2) mod p
    """
    return pow(x, length-2)


def rev_shuffle(instr, length, fac, term):
    """Give back the factor to multply with and the term to add to achieve a
    single _reverse_ shuffle."""
    typ = instr[0]
    if typ == 'deal into new stack':
        fac = -fac
        term = -term - 1
    if typ == 'cut ':
        x = int(instr[1])
        term += x
    if typ == 'deal with increment ':
        x = int(instr[1])
        fac *= inv(x)
        term *= inv(x)
    return (fac % length, term % length)


# Figure out a symbolic expression for a full _reverse_ run-through of the
# input. That is, starting at the end position of a shuffle, which was the
# starting position?

fac = 1
term = 0
for j in range(len(inp)):
    instr = inp[len(inp) - j - 1]
    (fac, term) = rev_shuffle(instr, length, fac, term)

pos = 2020
iters = 101741582076661

# Result is:
# ((pos * fac + term) * fac + term) * fac + term ... (repeat iters times)
# = pos*fac^iters + (term*fac^(iters-1) + term*fac^(iters-2) + ... + term)
# = pos*fac^iters + term*(fac^(iters+) - 1)/(fac - 1)
# The `terms` part is a geometric sum:
# https://en.wikipedia.org/wiki/Geometric_series#Formula

geo = (pow(fac, iters) - 1) * inv((fac - 1))
res = (pos * pow(fac, iters) + term * geo) % length

print(res)
