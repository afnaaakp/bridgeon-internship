class InvalidMarkError(Exception):
 pass
def calculate_grade(name,*marks):
 if len(marks)==0:
  print("no marks are provided")
 else:
   mark= input("enter your mark")
 for mark in marks:
  if mark<0 or mark>100:
   raise InvalidMarkError("mark must be between 0 and 100")
 average=sum(marks)/len(marks)
 if average>=90:
  print("grade is A")
 elif average>=75:
  print("grade is B")
 elif average>=50:
  print("grade is C")
 else:
  print("grade is F")
 print(calculate_grade("afna",56,89,73,69))


