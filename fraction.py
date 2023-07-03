def sum(x, y):
    result = {}
    result['n'] = x['n'] * y['d'] + x['d'] * y['n']
    result['d'] = x['d'] * y['d']
    return result


def sub(x, y):
    result = {}
    result['n'] = x['n'] * y['d'] - x['d'] * y['n']
    result['d'] = x['d'] * y['d']
    return result


def mul(x, y):
    result = {}
    result['n'] = x['n'] * y['n']
    result['d'] = x['d'] * y['d']
    return result

def div(x, y):
    result = {}
    result['n'] = x['n'] / y['n']
    result['d'] = x['d'] / y['d']
    return result

def show(x):
    print(x['n'], '/', x['d'])

F = []
def fracs():
    n = int(input(" enter numerator: "))
    d = int(input(" enter denominator: "))
    fraction = {}
    fraction['n'] = n
    fraction['d'] = d
    F.append(fraction)

print("fraction 1:")
fracs()

print("fraction 2:")
fracs()

sum = sum(F[0], F[1])
sub = sub(F[0], F[1])
mul = mul(F[0], F[1])
div = div(F[0], F[1])



print('sum : ', end='')
show(sum)

print('sub : ' , end='')
show(sub)

print('multiplication : ' , end='')
show(mul)

print('division : ' , end='')
show(div)