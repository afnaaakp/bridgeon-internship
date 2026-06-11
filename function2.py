def safe_divide(a,b):
    if b==0:
       raise ZeroDivisionError("cannot divided by zero")
    return a/b        
try:
     print(safe_divide(16,4))
except ZeroDivisionError:
    print("cannot divided by zero")






