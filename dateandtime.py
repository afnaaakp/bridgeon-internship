from datetime import datetime
from collections import Counter 
def log_call(func):
    def wrapper(*args,**kwargs):
      timestamp=datetime.now()
      with open("log.txt","a")as file:
         file.write(f"{func.__name__},{args},{timestamp}\n")
      return func(*args,**kwargs)
    return wrapper
@log_call
def add(a, b):
    return a + b
@log_call
def greet(name):
    print("Hello", name)

@log_call
def square(n):
    return n * n
add(2, 3)
add(5, 7)

greet("Alice")
greet("Bob")
greet("Charlie")

square(4)
square(6)
square(8)


   
