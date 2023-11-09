import anxiety
import depression
import EatingDisorder
import Hyperactivity
import personalityTest

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
  print("Apppearing for anxiety test  (Please answer in (y/n)form ) ")
  anxious=0
  while True:
      res1=str(input("Have you been feeling unusually anxious or worried most days for at least six months?"))
      if res1.lower() == 'y':
        anxious+=1
        break
      elif res1.lower() == 'n':
        print("Thank you!!")
        break
      else:
        print(" Please enter the correct answer")  
  while True:
      res2=str(input("2.Do you often experience physical symptoms like racing heart, sweating,or trembling when you're anxious? "))
      if res2.lower() == 'y':
        anxious+=1
        break
      elif res2.lower() == 'n':
        print("Thank you!!")
        break
  while True:
      res3=str(input("3.Are you avoiding certain situations or activities because of your anxiety?"))
      if res3.lower() == 'y':
        anxious+=1
        break
      elif res3.lower() == 'n':
        print("Thank you!!")
        break
      else:
        print(" Please enter the correct answer")    
  while True:
      res4=str(input("4. Have you naticed a significant changes in your sleep patterns, such as difficulty falling asleep or staying asleep due to anxiety ?"))
      if res4.lower() == 'y':
        anxious+=1
        break
      elif res4.lower() == 'n':
        print("Thank you!!")
        break    
      else:
        print(" Please enter the correct answer")     
  while True:
      res5=str(input("5. Do you find it challenging to control your worry or anxious thoughts , even when you try to redirect your focus? "))
      if res5.lower() == 'y':
        anxious+=1
        break
      elif res5.lower() == 'n':
        print("Thank you!!")
        break
      else:
        print(" Please enter the correct answer")

  if (anxious>=2 and anxious<=3):
    print(" We have seen some symptoms in you so are here to give some relevant information to you Please read that carefully ")
    result=anxiety.moderate()
    print(result)
  elif(anxious>=4 and anxious==5):
    result=anxiety.dangerous() 
    print(result)
  else:
    print("Ohh goood , You don't have such a symptoms regarding anxiety")  


  print("Apppearing for Depression test (Please answer in (y/n)form )")
  deprees=0
  while True:
      deprees=0
      res1=str(input("1. Have you been persistently feeling sad or down for most of the day, nearly every day, for at least two weeks or longer?"))
      if res1.lower() == 'y':
        deprees+=1
        break
      elif res1.lower() == 'n':
        print("Thank you!!")
        break
      else:
        print(" Please enter the correct answer")  
  while True:
      res2=str(input("2.Are you experiencing a significant decrease in interest or pleasure in activities that you used to enjoy? "))
      if res2.lower() == 'y':
        deprees+=1
        break
      elif res2.lower() == 'n':
        print("Thank you!!")
        break
  while True:
      res3=str(input("3.Have you noticed changes in your sleep patterns, such as trouble falling asleep, staying asleep, or oversleeping?"))
      if res3.lower() == 'y':
        deprees+=1
        break
      elif res3.lower() == 'n':
        print("Thank you!!")
        break
      else:
        print(" Please enter the correct answer")    
  while True:
      res4=str(input("4.Have there been changes in your appetite or weight, like significant changes in eating habits or weight gain/loss?"))
      if res4.lower() == 'y':
        deprees+=1
        break
      elif res4.lower() == 'n':
        print("Thank you!!")  
        break  
      else:
        print(" Please enter the correct answer")     
  while True:
      res5=str(input("5. Do you find it challenging to concentrate, make decisions, or have you experienced a decrease in your ability to think clearly? "))
      if res5.lower() == 'y':
        deprees+=1
        break
      elif res5.lower() == 'n':
        print("Thank you!!")
        break
      else:
        print(" Please enter the correct answer")

  if (deprees>=2 and deprees<=3):
    print(" We have seen some symptoms in you so are here to give some relevant information to you Please read that carefully ")
    result=depression.moderate()
    print(result)
  elif(deprees>=4 and deprees==5):
    result=depression.dangerous() 
    print(result)
  else:
    print("Ohh goood , You don't have such a symptoms regarding Depression") 


  print("Apppearing for Eating Disorder test (Please answer in (y/n)form )")
  Eating=0
  while True:
      res1=str(input("1. Have you noticed any significant changes in your eating habits, such as eating much less or much more than usual?"))
      if res1.lower() == 'y':
         Eating+=1
         break
      elif res1.lower() == 'n':
        print("Thank you!!")
        break
      else:
        print(" Please enter the correct answer")  
  while True:
      res2=str(input("2.Do you often feel a strong need to control your weight or body shape through dieting or excessive exercise?"))
      if res2.lower() == 'y':
         Eating+=1
         break
      elif res2.lower() == 'n':
        print("Thank you!!")
        break
  while True:
      res3=str(input("3.Have you experienced any physical or emotional health issues that you suspect might be related to your eating habits?"))
      if res3.lower() == 'y':
         Eating+=1
         break
      elif res3.lower() == 'n':
        print("Thank you!!")
        break
      else:
        print(" Please enter the correct answer")    
  while True:
      res4=str(input("4.Are you often dissatisfied with your appearance and body image?"))
      if res4.lower() == 'y':
         Eating+=1
         break
      elif res4.lower() == 'n':
        print("Thank you!!") 
        break   
      else:
        print(" Please enter the correct answer")     
  while True:
      res5=str(input("5. Have you ever made yourself vomit, used laxatives, or engaged in other behaviors to compensate for the amount of food you've eaten? "))
      if res5.lower() == 'y':
         Eating+=1
         break
      elif res5.lower() == 'n':
        print("Thank you!!")
        break
      else:
        print(" Please enter the correct answer")

  if ( Eating>=2 and Eating<=3):
    print(" We have seen some symptoms in you so are here to give some relevant information to you Please read that carefully ")
    result=EatingDisorder.moderate()
    print(result)
  elif( Eating>=4 and  Eating==5):
    result=EatingDisorder.dangerous() 
    print(result)
  else:
    print("Ohh goood , You don't have such a symptoms regarding Eating Dosorder")   
    
    
  while True:
    test=print("Are you inerested to give another tests  (Please answer in (y/n)form ) ? ")
    if test.lower() == 'y':
      print("Apppearing for Hyperactivity Disorder test (Please answer in (y/n)form )")
      hyper=0
      while True:
        res1=str(input("1. Do you often find it challenging to stay focused on tasks or activities that require sustained attention?"))
        if res1.lower() == 'y':
           hyper+=1
           break
        elif res1.lower() == 'n':
          print("Thank you!!")
          break
        else:
          print(" Please enter the correct answer")  
      while True:
        res2=str(input("2. Do you frequently make careless mistakes in school or work?? "))
        if res2.lower() == 'y':
           hyper+=1
           break
        elif res2.lower() == 'n':
          print("Thank you!!")
          break
      while True:
        res3=str(input("3. Do you find it difficult to organize tasks and activities?"))
        if res3.lower() == 'y':
           hyper+=1
           break
        elif res3.lower() == 'n':
          print("Thank you!!")
          break
        else:
          print(" Please enter the correct answer")    
      while True:
        res4=str(input("4.Are you often forgetful in your daily routines?"))
        if res4.lower() == 'y':
           hyper+=1
           break
        elif res4.lower() == 'n':
          print("Thank you!!") 
          break   
        else:
          print(" Please enter the correct answer")     
      while True:
        res5=str(input("5. Do you tend to feel restless or fidgety, such as tapping your hands or feet when you need to sit still? "))
        if res5.lower() == 'y':
           hyper+=1
           break  
        elif res5.lower() == 'n':
          print("Thank you!!")
          break
        else:
          print(" Please enter the correct answer")

      if ( hyper>=2 and hyper<=3):
        print(" We have seen some symptoms in you so are here to give some relevant information to you Please read that carefully ")
        result=Hyperactivity.moderate()
        print(result)
      elif( hyper>=4 and  hyper==5):
        result=Hyperactivity.dangerous() 
        print(result)
      else:
        print("Ohh goood , You don't have such a symptoms regarding Hyperactivity Dosorder") 


      print(" Appearing for test 5 i.e Personality Disorder test  (Please answer in (y/n)form ) ") 
      personality=0
      while True:
        res1=str(input("1. Do you often find it challenging to stay focused on tasks or activities that require sustained attention?"))
        if res1.lower() == 'y':
           personality+=1
           break
        elif res1.lower() == 'n':
          print("Thank you!!")
          break
        else:
          print(" Please enter the correct answer")  
      while True:
        res2=str(input("2. Do you frequently make careless mistakes in school or work?? "))
        if res2.lower() == 'y':
          personality+=1
          break
        elif res2.lower() == 'n':
          print("Thank you!!")
          break
      while True:
        res3=str(input("3. Do you find it difficult to organize tasks and activities?"))
        if res3.lower() == 'y':
           personality+=1
           break
        elif res3.lower() == 'n':
          print("Thank you!!")
          break
        else:
          print(" Please enter the correct answer")    
      while True:
        res4=str(input("4.Are you often forgetful in your daily routines?"))
        if res4.lower() == 'y':
           personality+=1
           break
        elif res4.lower() == 'n':
          print("Thank you!!") 
          break   
        else:
          print(" Please enter the correct answer")     
      while True:
        res5=str(input("5. Do you tend to feel restless or fidgety, such as tapping your hands or feet when you need to sit still? "))
        if res5.lower() == 'y':
           personality+=1
           break  
        elif res5.lower() == 'n':
          print("Thank you!!")
          break
        else:
          print(" Please enter the correct answer")

      if (  personality>=2 and  personality<=3):
        print(" We have seen some symptoms in you so are here to give some relevant information to you Please read that carefully ")
        result=personalityTest.moderate()
        print(result)
      elif(  personality>=4 and   personality==5):
        result=personalityTest.dangerous() 
        print(result)
      else:
        print("Ohh goood , You don't have such a symptoms regarding Hyperactivity Dosorder")  



    




    elif test.lower()== 'n':
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





  
     

           


