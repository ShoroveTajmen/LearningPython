a = int(input("Enter a amount:"))
b = a
temp = a//1000
print(temp, '1000 Taka note(s).')
if temp > 0:
    a = a%1000
    b = a
else:
    a = b
    temp = a // 500
    print("500 taka note is: ", temp)
    if temp > 0:
        a = a % 500
        b = a
    else:
        a=b
        temp = a // 100
        print("100 taka note is: ", temp)
        if temp > 0:
            a = a % 100
            b = a
        else:
            a = b
            temp = a // 50
            print("50 taka note is: ", temp)
            if temp > 0:
                a = a % 50
                b = a
            else:
                a = b
                temp = a // 20
                print("20 taka note is: ", temp)
                if temp > 0:
                    a = a % 20
                    b = a
                else:
                    a = b
                    temp = a // 10
                    print("10 taka note is: ", temp)
                    if temp > 0:
                        a = a % 10
                        b = a
                    else:
                        a = b
                        temp = a // 5
                        print("5 taka note is: ", temp)
                        if temp > 0:
                            a = a % 5
                            b = a
                        else:
                            a = b
                            temp = a // 2
                            print("2 taka note is: ", temp)
                            if temp > 0:
                                a = a % 2
                                b = a
                            else:
                                a = b
                                temp = a // 1
                                print("1 taka note is: ", temp)









