def fibbanocci(num):
    f3 = 0
    f2 = 1
    f1=1
    if(num==1 or num==0):
        print("Given number is in the fibonaci series")
    else:
        while f3 < num:
            f3=f1+f2
            f2=f1
            f1=f3
        if f3 == num:
            print("Given number is in the fibonaci series")
        else:
            print("Given number is not in the fibonaci series")

fibbanocci(34)