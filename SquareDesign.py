print('Please, input the number:')
number = int(input())
temp = number

while number > 0:
    count = temp
    while count > 0:
        print('*', end='')
        count -= 1
    print()
    number -= 1