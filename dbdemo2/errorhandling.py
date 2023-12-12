
try:
    x = 12 + 22
    print(y)
except ZeroDivisionError as zde:
    # action?    
    print('mali ang divide mo, tawagan mo si sir alwin')
except TypeError as te:
    # action?
    print(te)
except Exception as e:
    print("mali")
