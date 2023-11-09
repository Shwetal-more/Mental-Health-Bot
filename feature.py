import os
import anxiety
import depression
import EatingDisorder
import Hyperactivity
import personalityTest

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
    

  if (score >=40):
    BigTest()
  else:
    endPart()

#Big test is to identify specific Disorder
def BigTest():
  print("\nNow we are going to have diffferent tests for different aspects in mental health")
  print("Apppearing for anxiety test  (Please answer in (y/n)form ) ")
  questions = ("1. Have you been feeling unusually anxious or worried most days for at least six months?",
             "2.Do you often experience physical symptoms like racing heart, sweating,or trembling when you're anxious? ",
             "3.Are you avoiding certain situations or activities because of your anxiety?",
             "4. Have you naticed a significant changes in your sleep patterns, such as difficulty falling asleep or staying asleep due to anxiety ?",
             "5. Do you find it challenging to control your worry or anxious thoughts , even when you try to redirect your focus?")
  options = (("A.Yes","B.No"),
             ("A.Yes","B.No"),
             ("A.Yes","B.No"),
             ("A.Yes","B.No"),
             ("A.Yes","B.No"),)
  Guesses = []
  anxiety = 0
  Question_number=0
  
  for question in questions:
    print("---------------------------------------------------------------------------")
    print(question)
    for option in options[Question_number]:
        print(option)
    
     
    Guess = input("Enter the Answer (A,B):").upper()
    Guesses.append(Guess)
    if Guess == 'A':
     anxiety = anxiety + 1
    elif Guess == 'B':
      anxiety = anxiety + 0
    else:
     print("please,Enter the right answer!!")
     
    Question_number+=1
    while Question_number==5:
      print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
      if (anxiety>=2 and anxiety<=3):
         print(" We have seen some symptoms in you so are here to give some relevant information to you Please read that carefully ")
         result=anxiety.moderate()
         print(result)
      elif(anxiety>=4 and anxiety==5):
         result=anxiety.dangerous() 
         print(result)
      else:
         print("Ohh goood , You don't have such a symptoms regarding anxiety")  
      break
  
  print("Apppearing for Depression test (Please answer in (y/n)form )")
  questions = ("1. Have you been persistently feeling sad or down for most of the day,\n nearly every day, for at least two weeks or longer?",
             "2.Are you experiencing a significant decrease in interest or \npleasure in activities that you used to enjoy?",
             "3.Have you noticed changes in your sleep patterns, \nsuch as trouble falling asleep, staying asleep, or oversleeping?",
             "4.Have there been changes in your appetite or weight,\n like significant changes in eating habits or weight gain/loss?",
             "5. Do you find it challenging to concentrate,\n make decisions, or have you experienced a decrease in your ability to think clearly?")
  options = (("A.Yes","B.No"),
             ("A.Yes","B.No"),
             ("A.Yes","B.No"),
             ("A.Yes","B.No"),
             ("A.Yes","B.No"),)
  Guesses = []
  deprees=0
  Question_number=0
  
  for question in questions:
    print("---------------------------------------------------------------------------")
    print(question)
    for option in options[Question_number]:
        print(option)
    
     
    Guess = input("Enter the Answer (A,B):").upper()
    Guesses.append(Guess)
    if Guess == 'A':
       deprees = deprees + 1
    elif Guess == 'B':
       deprees = deprees + 0
    else:
       print("please,Enter the right answer!!")
     
    Question_number+=1
    while Question_number==5:
      print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
      if deprees >= 2 and deprees <= 3:
        print(" We have seen some symptoms in you so are here to give some relevant information to you Please read that carefully ")
        result=depression.moderate()
        print(result)
        break
      elif deprees >= 4 and deprees==5:
        result=depression.dangerous() 
        print(result)
        break
      else:
        print("Ohh goood , You don't have such a symptoms regarding Depression") 
        break
      break

  while True:
    test=print("Are you inerested to give another tests  (Please answer in (y/n)form ) ? ")
    if test.lower() == 'y':
      print("Apppearing for Eating Disorder test (Please answer in (y/n)form )")
      questions = ("1. Have you noticed any significant changes in your eating habits, such as eating much less or much more than usual?",
             "2.Do you often feel a strong need to control your weight or body shape through dieting or excessive exercise?",
             "3.3.Have you experienced any physical or emotional health issues that you suspect might be related to your eating habits?",
             "4.Are you often dissatisfied with your appearance and body image?",
             "5. Have you ever made yourself vomit, used laxatives, or engaged in other behaviors to compensate for the amount of food you've eaten?")
      options = (("A.Yes","B.No"),
             ("A.Yes","B.No"),
             ("A.Yes","B.No"),
             ("A.Yes","B.No"),
             ("A.Yes","B.No"),)
      Guesses = []
      Eating=0
      Question_number=0
  
      for question in questions:
          print("---------------------------------------------------------------------------")
          print(question)
          for option in options[Question_number]:
            print(option)
    
     
          Guess = input("Enter the Answer (A,B):").upper()
          Guesses.append(Guess)
          if Guess == 'A':
             Eating += 1
          elif Guess == 'B':
             Eating += 0
          else:
             print("please,Enter the right answer!!")
     
          Question_number+=1
          while Question_number==5:
             print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
             if ( Eating>=2 and Eating<=3):
                print(" We have seen some symptoms in you so are here to give some relevant information to you Please read that carefully ")
                result=EatingDisorder.moderate()
                print(result)
                break
             elif( Eating>=4 and  Eating==5):
                print(" We have seen some symptoms in you so are here to give some relevant information to you Please read that carefully ")  
                result=EatingDisorder.dangerous() 
                print(result)
                break
             else:
                print("Ohh goood , You don't have such a symptoms regarding Eating Dosorder")   
                break
    break   

  while True:
     test=print("Are you inerested to give another tests  (Please answer in (y/n)form ) ? ")
     if test.lower() == 'y':
        print("Apppearing for Hyperactivity Disorder test (Please answer in (y/n)form )")
        questions = ("1. Do you often find it challenging to stay focused on tasks or\n activities that require sustained attention?",
             "2. Do you frequently make careless mistakes in school or work?",
             "3. Do you find it difficult to organize tasks and activities?",
             "4. Are you often forgetful in your daily routines?",
             "5. Do you tend to feel restless or fidgety,\n such as tapping your hands or feet when you need to sit still?")
        options = (("A.Yes","B.No"),
             ("A.Yes","B.No"),
             ("A.Yes","B.No"),
             ("A.Yes","B.No"),
             ("A.Yes","B.No"),)
        Guesses = []
        hyper=0
        Question_number=0
  
        for question in questions:
              print("---------------------------------------------------------------------------")
              print(question)
              for option in options[Question_number]:
                print(option)
              
              Guess = input("Enter the Answer (A,B):").upper()
              Guesses.append(Guess)
              if Guess == 'A':
                 hyper  += 1
              elif Guess == 'B':
                 hyper += 0
              else:
                 print("please,Enter the right answer!!")
     
              Question_number+=1
              while Question_number==5:
                print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
                if ( hyper>=2 and hyper<=3):
                   print(" We have seen some symptoms in you so are here to give some relevant information to you Please read that carefully ")
                   result=Hyperactivity.moderate()
                   print(result)
       
                elif( hyper>=4 and  hyper==5):
                   result=Hyperactivity.dangerous() 
                   print(result)
                else:
                   print("Ohh goood , You don't have such a symptoms regarding Hyperactivity Dosorder") 
              break
     break

while True:
     test1=print("Are you inerested to give another tests  (Please answer in (y/n)form ) ? :")
     if test1 == 'y':      
          print(" Appearing for test 5 i.e Personality Disorder test  (Please answer in (y/n)form ) ") 
          questions = ("1. Do you often find it challenging to stay focused on tasks or\n activities that require sustained attention?",
             "2. Do you frequently make careless mistakes in school or work?",
             "3. Do you find it difficult to organize tasks and activities?",
             "4.Are you often forgetful in your daily routines?",
             "5. Do you tend to feel restless or fidgety, \nsuch as tapping your hands or feet when you need to sit still?")
          options = (("A.Yes","B.No"),
             ("A.Yes","B.No"),
             ("A.Yes","B.No"),
             ("A.Yes","B.No"),
             ("A.Yes","B.No"),)
          Guesses = []
          personality=0
          Question_number=0
  
          for question in questions:
               print("---------------------------------------------------------------------------")
               print(question)
               for option in options[Question_number]:
                  print(option)
    
     
               Guess = input("Enter the Answer (A,B):").upper()
               Guesses.append(Guess)
               if Guess == 'A':
                  personality += 1
               elif Guess == 'B':
                  personality += 0
               else:
                  print("please,Enter the right answer!!")

               Question_number+=1
               while Question_number==5:
                  print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
                  if  personality>=2 and personality<=3:
                     print(" We have seen some symptoms in you so are here to give some relevant information to you Please read that carefully ")
                     result=personalityTest.moderate()
                     print(result)
        
                  elif personality>=4 and personality==5:
                     result=personalityTest.dangerous() 
                     print(result)
                  else:
                     print("Ohh goood , You don't have such a symptoms regarding Hyperactivity Dosorder")  
                  break
     break

# end part regarding awreness
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





  
     

           


