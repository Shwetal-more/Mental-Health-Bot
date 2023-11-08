def smalltest():
  response=0
  while True:
     res1=int(input("1. How have you been feeling lately (Rate in range of 0 to 100%)?"))
     if res1>0 and res1<100:
      response=response+ res1
      break
     else:
      print("Please give answer in correct range")

  while True:
    res2=int(input("2. Are there any specific situations or events causing you stress or anxiety(Rate in range of 0 to 100%)?"))
    if res2>0 and res2<100:
      response=response+ res2
      break
    else:
      print("Please give answer in correct range")


  while True:
      res3=int(input("3. On a scale of 0 to 100 , how would you rate your overall modd today?"))
      if res3>0 and res3<100:
        response=response+ res3
        break
      else:
        print("Please give answer in correct range")    


print("***********Welcome to our Student friendly quik and easy Mental Health testing game**************")
user=str(input("Are you interested in giving the small test(y/Y) or not(N/n) ? "))
if user.lower() == 'y':
    smalltest()
elif user.lower() == 'n':
    print("Thank you!!")
  
     

           


