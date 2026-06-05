numbers=[]
sum=0
even_count=0
odd_count=0
for i in range(5):
   i=int(input("enter a number:"))
   numbers.append(i)
   sum=sum+i 
   if  i%2==0:
    even_count+=1
else:
 odd_count+=1
 largest=max(numbers)
 smallest=min(numbers)
 print("numbers:",numbers)
 print("largest number",largest)
 print("smallest number",smallest)
 print("sum of the numbers",sum)
 print("count of even is",even_count )
 print("count of odd is",odd_count)
         
         
    
