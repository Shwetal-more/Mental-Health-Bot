import anxiety
import depression
import EatingDisorder
import Hyperactivity
import personalityTest
import awareness

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
def smalltest():
  
    questions = ("1. How have you been feeling lately ?",
             "2. On average, how many hours of sleep do you get per night \U0001F634 ?",
             "3. How have you been eating?",
             "4. Do you feel supported by your friends and peers in managing your mental health as a student \U0001F61E ?",
             "5. How will you dcribe your angry control \U0001F621 ?",
             "6. When was the last time you laugh out loud \U0001F923 ?",
             "7. How often do you feel overwhelmed by academic responsibilities and deadlines \U0001F616 ?",
             "8. Have you experienced any symptoms of depression, such as persistent sadness or loss of interest \U0001F64D ?",
             "9. Do you engage in regular physical activity and maintain a healthy lifestyle\U0001F6B6 \U0001F3C3?",
             "10. How would you rate your overall stress levels in your daily life\U0001F64D?",
             "11. Do you feel comfortable expressing your thoughts and emotions to your Friends & Family?\U0001F46A")

    options =(("A. \U0001F604", "B. \U0001F634", "C. \U0001F625", "D. \U0001F912", "E. \U0001F621"),
            ("A.8-9hrs", "B.6-7hrs", "C.3-5hrs", "D.Sleepless night" ),
            ("A.Properly and on Time", "B.occasionally less", "C.frequently, Too Little", "D. frequently, too much", "E. Always Hungry"),
            ("A. Always", "B. most of time", "C. occasionally", "D. No,very rarely", "E. No, not at all"),
            ("A. I don't get angry easily", "B. i can control my angry", "C. i get angry easliy", "D. I can't controlled my angry"),
            ("A. Just sometime earlier", "B. few days earlier", "C. Not in past few days", "D. Been Weeks"),
            ("A. No, not at all", "B. sometimes","C. easily Overwhelmed", "D. Very easily overwhelmed"),
            ("A. No, never", "B. No, rarely",  "C. Yes, occasionally", "D. Yes, frequently"),
            ("A. Yes, frequently", "B. Yes, occasionally", "C. No, rarely", "D. No, never"),
            ("A.Very low",  "B.Low Moderate", "C.High", "D. Very high"),
            ("A.Yes, always", "B.Most of the time", "C.Sometimes", "D. Rarely or never"))
    Guesses = []
    score = 0
    Question_number=0
    for question in questions:
     print(color.PURPLE+"---------------------------------------------------------------------------"+color.END)
     print(question)
     for option in options[Question_number]:
        print(option)
    
     
     Guess = input("Enter the Answer (A,B,C,D,E):").upper()
     Guesses.append(Guess)
    
     if Guess == 'A':
         score=score+2 
     elif Guess == 'B':
        score=score+4 
     elif Guess == 'C':
       score=score+6 
     elif Guess == 'D':
       score=score+8
     elif Guess == 'E':
       score=score+10
     else:
       print("Please give answer in correct range")
     Question_number+=1 
    
    if (score >=30):
      BigTest()
    else:
      EndPart()

#Big test is to identify specific Disorder
def BigTest():
  
  print(color.BLUE+"- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - -"+color.END)
  print(color.BOLD + color.DARKCYAN+"Now we are going to have diffferent tests for different aspects in mental health" + color.END)
  print("\nApppearing for anxiety test  (Please answer in (y/n)form ) ")
  anxious=0
  while True:
      print(color.YELLOW+"--------------------------------------------------------------------------"+ color.END)
      res1=str(input("Have you been feeling unusually anxious or worried most days for at least six months?  Ans: "))
      if res1.lower() == 'y':
        anxious+=1
        break
      elif res1.lower() == 'n':
        print("Thank you!!")
        break
      else:
        print(" Please enter the correct answer")  
  while True:
      print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
      res2=str(input("2.Do you often experience physical symptoms like racing heart, sweating,or trembling when you're anxious? Ans: "))
      if res2.lower() == 'y':
        anxious+=1
        break
      elif res2.lower() == 'n':
        print("Thank you!!")
        break
  while True:
      print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
      res3=str(input("3.Are you avoiding certain situations or activities because of your anxiety? Ans: "))
      if res3.lower() == 'y':
        anxious+=1
        break
      elif res3.lower() == 'n':
        print("Thank you!!")
        break
      else:
        print(" Please enter the correct answer")    
  while True:
      print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
      res4=str(input("4. Have you naticed a significant changes in your sleep patterns, such as difficulty falling asleep or staying asleep due to anxiety ? Ans: "))
      if res4.lower() == 'y':
        anxious+=1
        break
      elif res4.lower() == 'n':
        print("Thank you!!")
        break    
      else:
        print(" Please enter the correct answer")     
  while True:
      print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
      res5=str(input("5. Do you find it challenging to control your worry or anxious thoughts , even when you try to redirect your focus?  Ans: "))
      if res5.lower() == 'y':
        anxious+=1
        break
      elif res5.lower() == 'n':
        print("Thank you!!")
        break
      else:
        print(" Please enter the correct answer")

  if (anxious>=2 and anxious<=3):
    print(color.CYAN+"**************************************"+color.END)
    print(" We have seen some symptoms in you so are here to give some relevant information to you Please read that carefully. ")
    result=anxiety.moderate()
    print(result)
  elif(anxious>=4 and anxious==5):
    print(color.CYAN+"**************************************"+color.END)
    result=anxiety.dangerous() 
    print(result)
  else:
    print(color.CYAN+"**************************************"+color.END)
    print("Ohh goood , You don't have such a symptoms regarding anxiety")  

  print(color.BLUE+"- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - -"+color.END)
  print("Apppearing for Depression test (Please answer in (y/n)form )")
  deprees=0
  
  while True:
      print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
      res1=str(input("1. Have you been persistently feeling sad or down for most of the day, nearly every day, for at least two weeks or longer? Ans: "))
      if res1.lower() == 'y':
        deprees+=1
        break
      elif res1.lower() == 'n':
        print("Thank you!!")
        break
      else:
        print(" Please enter the correct answer")  
  while True:
      print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
      res2=str(input("2.Are you experiencing a significant decrease in interest or pleasure in activities that you used to enjoy? "))
      if res2.lower() == 'y':
        deprees+=1
        break
      elif res2.lower() == 'n':
        print("Thank you!!")
        break
  while True:
      print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
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
      print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
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
      print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
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
    print(color.CYAN+"**************************************"+color.END)
    print(" We have seen some symptoms in you so are here to give some relevant information to you Please read that carefully ")
    result=depression.moderate()
    print(result)
  elif(deprees>=4 and deprees==5):
    print(color.CYAN+"**************************************"+color.END)
    result=depression.dangerous() 
    print(result)
  else:
    print(color.CYAN+"**************************************"+color.END)
    print("Ohh goood , You don't have such a symptoms regarding Depression") 

  print(color.BLUE+"- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - -"+color.END)
  print("Apppearing for Eating Disorder test (Please answer in (y/n)form )")
  Eating=0
  while True:
      print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
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
      print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
      res2=str(input("2.Do you often feel a strong need to control your weight or body shape through dieting or excessive exercise?"))
      if res2.lower() == 'y':
         Eating+=1
         break
      elif res2.lower() == 'n':
        print("Thank you!!")
        break
  while True:
      print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
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
      print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
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
      print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
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
    print(color.CYAN+"**************************************"+color.END)
    print(" We have seen some symptoms in you so are here to give some relevant information to you Please read that carefully ")
    result=EatingDisorder.moderate()
    print(result)
  elif( Eating>=4 and  Eating==5):
    print(color.CYAN+"**************************************"+color.END)
    result=EatingDisorder.dangerous() 
    print(result)
  else:
    print(color.CYAN+"**************************************"+color.END)
    print("Ohh goood , You don't have such a symptoms regarding Eating Dosorder")   
    
  print(color.BLUE+"- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - -"+color.END)  
  while True:
    
    test=str(input("Are you inerested to give another tests  (Please answer in (y/n)form ) ? "))
    if test.lower() == 'y':
      print(color.BLUE+"- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - -"+color.END)
      print("Apppearing for Hyperactivity Disorder test (Please answer in (y/n)form )")
      hyper=0
      while True:
        print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
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
        print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
        res2=str(input("2. Do you frequently make careless mistakes in school or work?? "))
        if res2.lower() == 'y':
           hyper+=1
           break
        elif res2.lower() == 'n':
          print("Thank you!!")
          break
      while True:
        print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
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
        print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
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
        print("--------------------------------------------------------------------------"+color.END)
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
        print(color.CYAN+"**************************************"+color.END)
        print(" We have seen some symptoms in you so are here to give some relevant information to you Please read that carefully ")
        result=Hyperactivity.moderate()
        print(result)
      elif( hyper>=4 and  hyper==5):
        print(color.CYAN+"**************************************"+color.END)
        result=Hyperactivity.dangerous() 
        print(result)
      else:
        print(color.CYAN+"**************************************"+color.END)
        print("Ohh goood , You don't have such a symptoms regarding Hyperactivity Dosorder") 
      

      print(color.BLUE+"- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - -"+color.END)
      print(" Appearing for test 5 i.e Personality Disorder test  (Please answer in (y/n)form ) ") 
      personality=0
      while True:
        print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
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
        print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
        res2=str(input("2. Do you frequently make careless mistakes in school or work?? "))
        if res2.lower() == 'y':
          personality+=1
          break
        elif res2.lower() == 'n':
          print("Thank you!!")
          break
      while True:
        print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
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
        print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
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
        print(color.YELLOW+"--------------------------------------------------------------------------"+color.END)
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
        print(color.CYAN+"**************************************"+color.END)
        print(" We have seen some symptoms in you so are here to give some relevant information to you Please read that carefully ")
        result=personalityTest.moderate()
        print(result)
      elif(  personality>=4 and   personality==5):
        print(color.CYAN+"**************************************"+color.END)
        result=personalityTest.dangerous() 
        print(result)
      else:
        print(color.CYAN+"**************************************"+color.END)
        print("Ohh goood , You don't have such a symptoms regarding Hyperactivity Dosorder")  

      break    
    
    elif test.lower()== 'n':
       break

    
def EndPart():
      result = awareness.movie()
      


#Starting of the main code
print("***********Welcome to our Student friendly quik and easy Mental Health testing game**************")
user=str(input("Are you interested in giving the small test(y/Y) or not(N/n) ? "))
if user.lower() == 'y':
    smalltest()
elif user.lower() == 'n':
     result = awareness.movie()
     print("Thank you!!")
     

   





  
     

           


