author = 'john'

def greetme():
    print("Hello EY!")

def getnetpay(rh,h,d):
    np = (rh * h) - d
    # print(f'netpay is {np}')
    return np

def getjanuarysales():
    x = 300000
    return x

def getfebuarysales():
    x = 400000
    return x

def getmarchsales():
    x = 500000
    return x

def overalltotal():
    jan = getjanuarysales()
    feb = getfebuarysales()
    mar = getmarchsales()
    return jan + feb + mar