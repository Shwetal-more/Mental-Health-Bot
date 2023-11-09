import os
import anxiety
import depression
import EatingDisorder

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
    print("---------------------------------------------------------------------------")
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
    while Question_number==11:
      print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
      print("Your mental Health is(in percentage)",score) 
      break
  

  if (response >=40):
    BigTest()
  else:
    endPart()

#Big test is to identify specific Disorder
def BigTest():
  print("Now we are going to have diffferent tests for different aspects in mental health")
  print("Apppearing for anxiety test  (Please answer in (y/n)form ) ")
  while True:
      anxious=0
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
  while True:
      Eating=0
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





  
     

           


