marks=[]
pass_count=0
for i in range(5):
    i=int(input("enter your marks"))
    marks.append(i)
sum=0
highest=max(marks)
lowest=min(marks)
sum=sum+i
average=sum/5
for i in marks:
    if i > 50:
       pass_count+=1
print("marks:",marks)
print("highest marks:",highest)
print("lowest marks:",lowest)
print("average is:",average)
print("pass_count is:",pass_count)
      
