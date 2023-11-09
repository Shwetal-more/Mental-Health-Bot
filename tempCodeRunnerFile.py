 while True:
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