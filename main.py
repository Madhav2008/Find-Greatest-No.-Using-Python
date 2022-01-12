# Find the greatest no among four numbers

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
c = int(input('Enter 3rd number: '))
d = int(input('Enter 4th number: '))

def greater(a, b, c, d):
    if a > b:
        if a > c:
            if a > d:
                print(f'Num 1 that is {a} is Greater No.')
            else:
                print(f'Num 4 that is {d} is Greater No.')
        else:
            if c > d:
                print(f'Num 3 that is {c} is Greater No.')
    else:
        if b > c:
            if b > d:
                print(f'Num 2 that is {b} is Greater No.')
            else:
                print(f'Num 4 that is {d} is Greater No.')
                    
greater(a, b, c, d)
