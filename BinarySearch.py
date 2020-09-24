mylist = [1, 3, 5, 7, 11, 13, 15, 17, 20, 26, 31, 44, 54, 56, 65, 77, 94, 100]

num = int(input("Enter a number: "))

first = 0
last = len(mylist)-1
found = False
cycle = 0

while first<=last and not found:
    midpoint = (first + last)//2
    if mylist[midpoint] == num:
        found = True
    else:
        if num < mylist[midpoint]:
            last = midpoint-1
        else:
            first = midpoint+1
    cycle+=1

print('Found after', cycle, 'cycle')



