def sum(x, y):
    result = {}
    result['r'] = x['r'] + y['r']
    result['i'] = x['i'] + y['i']
    return result


def sub(x, y):
    result = {}
    result['r'] = x['r'] - y['r']
    result['i'] = x['i'] - y['i']
    return result


def mul(x, y):
    result = {}
    result['r'] = ( x['r'] * y['r'] ) - ( x['i'] * y['i'] )
    result['i'] = ( x['i'] * y['r'] ) + ( x['r'] * y['i'] )
    return result

def show(x):
    print(x['r'] , ' + ', x['i'], 'i' )
    
COM = []
def complex():
    a = int(input(" enter a: "))
    b = int(input(" enter b: "))
    com = {}
    com['r'] = a
    com['i'] = b
    COM.append(com)
print("complex 1: ")
complex()

print("complex 2: ")
complex()

sum = sum(COM[0],COM[1])
sub = sub(COM[0],COM[1])
mul = mul(COM[0],COM[1])

print('sum: ', end='')
show(sum)
print('sub: ' , end='')
show(sub)
print('multiplication : ' , end='')
show(mul)