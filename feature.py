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
    if res2>0 and res2<10:
      response=response+ res2
      break
    else:
      print("Please give answer in correct range")


  while True:
      res3=int(input("3. On a scale of 0 to 10 , how would you rate your overall modd today?"))
      if res3>0 and res3<10:
        response=response+ res3
        break
      else:
        print("Please give answer in correct range")  

  if (response >=30):
    BigTest()
  else:
    endPart()

#Big test is to identify specific Disorder
def BigTest():
  print("Now we are going to have diffferent tests for different aspects in mental health")
  print("Apppearing for anxiety test")
  while True:
      anxious=0
      res1=str(input("Have you been feeling unusually anxious or worried most days for at least six months?"))
      if res1.lower() == 'y':
        anxious+=1
      elif res1.lower() == 'n':
        print("Thank you!!")
      else:
        print(" Please enter the correct answer")  
  while True:
      res2=str(input("2.Do you often experience physical symptoms like racing heart, sweating,or trembling when you're anxious? "))
      if res2.lower() == 'y':
        anxious+=1
      elif res2.lower() == 'n':
        print("Thank you!!")
  while True:
      res3=str(input("3.Are you avoiding certain situations or activities because of your anxiety?"))
      if res3.lower() == 'y':
        anxious+=1
      elif res3.lower() == 'n':
        print("Thank you!!")
      else:
        print(" Please enter the correct answer")    
  while True:
      res4=str(input("4. Have you naticed a significant changes in your sleep patterns, such as difficulty falling asleep or staying asleep due to anxiety ?"))
      if res4.lower() == 'y':
        anxious+=1
      elif res4.lower() == 'n':
        print("Thank you!!")    
      else:
        print(" Please enter the correct answer")     
  while True:
      res5=str(input("5. Do you find it challenging to control your worry or anxious thoughts , even when you try to redirect your focus? "))
      if res5.lower() == 'y':
        anxious+=1
      elif res5.lower() == 'n':
        print("Thank you!!")
      else:
        print(" Please enter the correct answer")

  if (anxious>=3):
    pass

  



#end part regarding awreness
def endPart():
  pass

#Starting of the main code
print("***********Welcome to our Student friendly quik and easy Mental Health testing game**************")
user=str(input("Are you interested in giving the small test(y/Y) or not(N/n) ? "))
if user.lower() == 'y':
    smalltest()
elif user.lower() == 'n':
    print("Thank you!!")
    endPart()





  
     

           


