pos = 0

def search(list,num):

    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low+high)//2

        if list[mid] == num:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < num:
                low = mid + 1
            else:
                high = mid - 1


list = [1,4,6,8,9,10]
num = 11

if search(list,num):
    print("Found at index: ",pos+1)
else:
    print("Not found")