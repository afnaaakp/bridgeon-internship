import json 
while True:
   print("expenses")
   print("summary")
   print("view all")
   print("exit") 
   choice=input("enter your choice")
   if choice=="expenses":
      print("adding expense")
      expenselist=[]
      category="shoes"
      amount=3000 
      expense={
         "category":category,
         "amount":amount}
      expenselist.append(expense)
      with open ("expenses.json","w")as f:
        json.dump(expenselist,f)
   if choice=="summary":
    summary={}
    with open("expenses.json", "r") as f:
            expenses = json.load(f)
    for expense in expenses:
        category=expense["category"]
        amount=expense["amount"]
        if category in summary:
            summary[category]+=amount
        else: 
            summary[category]=amount
   print(summary)
   if choice=="view all":
    with open("expense.json","r")as file:
     expenses=json.load(file)
     for expense in expenses:
      print(f"Category:{expense['category']},Amount:{expense['amount']}")
   if choice=="exit":
      print("end of the program")
      break

        




