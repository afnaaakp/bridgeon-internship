
from datetime import datetime
def log_call(func):
    def wrapper(*args,**kwargs):
        timestamp=datetime.now()
        with open("log.txt","a")as file:
            file.write(
                f"{func.__name__}| args={args}|  kwargs={kwargs} |{timestamp}\n"     
               )
        return func(*args,**kwargs)
    return wrapper
    
@log_call
def add(a,b):
    return a+b
@log_call
def greet(name):
    print(f"hello,{name}!")
@log_call
def multiply(a,b):
    return a*b
add(5,10)
add(4,8)
greet("afna")
greet("ammar")
multiply(2,4)
multiply(5,8)
multiply(4,6)
def read_logs():
    call_count={}
    with open ("log.txt","r")as file:
        for line in file:
            function_name=line.split("|")[0].strip()
            if function_name in call_count:
                call_count[function_name]+=1
            else:
                call_count[function_name]=1
    print("function call counts:")
    for name,count in call_count.items():
        print(f"{name}:{count}")
read_logs()