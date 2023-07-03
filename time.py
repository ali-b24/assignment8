def sum(x, y):
    result = {}
    result['s'] = x['s'] + y['s']
    result['m'] = x['m'] + y['m']
    result['h'] = x['h'] + y['h']
    
    if ( result['s'] >= 60 ) :
        result['s'] -= 60
        result['m'] += 1
        
    if ( result['m'] >= 60 ) :
        result['m'] -= 60
        result['h'] += 1
        
    return result

def sub(x, y):
    result = {}
    result['s'] = x['s'] - y['s']
    result['m'] = x['m'] - y['m']
    result['h'] = x['h'] - y['h']
    
    if ( result['m'] < 0 ) :
        result['m'] += 60
        result['h'] -= 1
        
    if ( result['s'] < 0 ) :
        result['s'] += 60
        result['m'] -= 1
           
    return result

def SecondToTime(second):
    result = {}
    result['h'] = second // 3600
    second = second - (result['h'] * 3600)
    result['m'] = second // 60 
    result['s'] = second - (result['m'] * 60)
    
    return result

def timeToSecond(time):
    second = ( time['h'] * 3600 ) + ( time['m'] * 60 ) + ( time['s'] )
    return second

def show(x):

    print(x['h'], " : ", x['m'], " : ", x['s'])

def menu():
    print ("Menu:")
    print ("1- Sum")
    print ("2- Sub")
    print ("3- Second to Time")
    print ("4- Time to Second")

def time_set(data):
    splited = data.split(":")
    time ={}
    time['h'] = int(splited[0])
    time['m'] = int(splited[1])
    time['s'] = int(splited[2])
    T.append(time)

T =[]
menu()
n = int(input('Select:'))
while n<1 or n>4:
    print("wrong input! try again:")
    n = int(input())

match n:
    case 1:
        time1 = input("enter time 1 like 00:00:00: ")
        time_set(time1)

        time2 = input("enter time 2 like 00:00:00: ")
        time_set(time2)

        sum = sum(T[0], T[1])
        print(" sum: ", end='')
        show(sum)
    case 2:
        time1 = input("enter time 1 like 00:00:00: ")
        time_set(time1)

        time2 = input("enter time 2 like 00:00:00: ")
        time_set(time2)
        sub = sub(T[0], T[1])
        print(" sub: ", end='')
        show(sub)
    case 3:
        data = int(input("enter seconds: "))
        time = SecondToTime(data)
        print('time: ', end='')
        show(time)
    case 4:
        data = input("enter time like 00:00:00: ")
        time_set(data)
        seconds = timeToSecond(T[0])
        print('seconds: ', seconds)
