def Average(*args):
    if(len(args))==0:
        print("no marks provided")
        return 0
    else:
        total=sum(args)
        count=len(args)
        Average= total/count
        return(Average)
print(Average(58,87,73,90,89))



