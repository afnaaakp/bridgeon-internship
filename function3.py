class WeakPasswordError(Exception):
 pass
def valid_password(password):
 if len(password)<8:
  raise WeakPasswordError("password must contain atleast 8 characters")
 if not any (char.isdigit()for char in password):
  raise WeakPasswordError("password must contain atleast one digit")
 if not any(char.isupper()for char in password):
  raise WeakPasswordError("password must contain atleast one uppercase") 
 return "password is valid" 
try:
  print(valid_password("Afna1234"))
except: 
  print("enter a valid password")

