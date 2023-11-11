from transformers import pipeline
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   ORANGE = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
def modarate():
     
    question_answering = pipeline("question-answering")
    context = """Anxiety is your body's natural response to stress. 
     Severe anxiety is People with severe anxiety usually experience more distress and less ability to function. 
    A person with this condition may also report symptoms similar to those of major depression, such as fatigue, headaches, and impaired concentration and memory. 
    Treatment of anxiety is Talk to someone you trust add,Talking to someone you trust about what's making you anxious could be a relief.
    Another treatment is Look after your physical health,Try breathing exercises,Keep a diary and Complementary and alternative therapies.
    The 3 3 3 rule for anxiety ismto identify three objects and three sounds,then moving three body parts.
    The 4 stages of anxiety are  mild anxiety, moderate anxiety, severe anxiety and panic level anxiety.
    Panic disorder is an anxiety disorder where you regularly have sudden attacks of panic or fear. Everyone experiences feelings of anxiety and panic at certain times. It's a natural response to stressful or dangerous situations.
    To stop panic attacks Remember that it will pass,Take deep breaths,Smell some lavender,Find a peaceful spot,Focus on an object,Repeat a mantra and Walk or do some light exercise."""
    
    print(color.YELLOW+color.BOLD+"Please enter Exit to Exit the Question and answer bot"+color.END)
    while True:
       question = input("user: ")
       if (question=='Exit' or question=='exit'):
        while True:
          print(color.ORANGE+"-----------------------------------------------------------------------------------"+color.END)
          print(color.DARKCYAN+"Some more important points:")
          print("ANXIETY OVERVIEW: \nDefinition:  Normal emotion of worry, fear, or unease.\n Becomes a concern when excessive, persistent, and disruptive (anxiety disorders).\n\n Symptoms:Physical: Rapid heartbeat, muscle tension, sweating.Cognitive: Excessive worrying, racing thoughts.\n Emotional: Restlessness, irritability, trouble sleeping.\n\nTreatment:\nTherapy: Cognitive-behavioral therapy (CBT), exposure therapy.\nMedications: Antidepressants, benzodiazepines (short-term), beta-blockers.\nLifestyle Changes: Exercise, healthy diet, adequate sleep, stress management.\n\nSelf-Help at Different Levels:\nMild Anxiety: Deep breathing, challenging irrational thoughts.\nModerate Anxiety: Journaling, physical activities.\nSevere Anxiety: Seek professional help, consider medication.\n\nWeekend Activities for Relief:Nature walks, creative outlets, socializing, relaxation techniques.\n\nDiet Recommendations:\nOmega-3 fatty acids (fish, flaxseeds, walnuts).\nWhole grains for steady energy.\nFruits and vegetables for antioxidants and vitamins.\nLimit caffeine and sugar intake.\n\nConclusion:\nIndividual responses vary, and consulting a healthcare professional for personalized advice is crucial. Implementing a holistic approach involving therapy, medication (if necessary), and lifestyle changes can contribute to managing anxiety effectively."+color.END)      
          break      
        return
       else:
        result = question_answering(question=question, context=context)
        print("Answer:", result['answer'])
      
       
def dangerous():
  
   
    question_answering = pipeline("question-answering")
    context = """ Anxiety is your body's natural response to stress. 
     Severe anxiety is People with severe anxiety usually experience more distress and less ability to function. 
    A person with this condition may also report symptoms similar to those of major depression, such as fatigue, headaches, and impaired concentration and memory. 
    Treatment of anxiety is Talk to someone you trust add,Talking to someone you trust about what's making you anxious could be a relief.
    Another treatment is Look after your physical health,Try breathing exercises,Keep a diary and Complementary and alternative therapies.
    The 3 3 3 rule for anxiety ismto identify three objects and three sounds,then moving three body parts.
    The 4 stages of anxiety are  mild anxiety, moderate anxiety, severe anxiety and panic level anxiety.
    Panic disorder is an anxiety disorder where you regularly have sudden attacks of panic or fear. Everyone experiences feelings of anxiety and panic at certain times. It's a natural response to stressful or dangerous situations.
    To stop panic attacks Remember that it will pass,Take deep breaths,Smell some lavender,Find a peaceful spot,Focus on an object,Repeat a mantra and Walk or do some light exercise.
    Tablets to calm down are Benzodiazepines,Benzodiazepines are a type of sedative that may sometimes be used as a short-term treatment during a particularly severe period of anxiety."""
    
    print(color.YELLOW+color.BOLD+"Please enter Exit to Exit the Question and answer bot"+color.END)
    while True:
       question = input("user: ")
       if (question=='Exit' or question=='exit'):
        while True:
          print(color.ORANGE+"-----------------------------------------------------------------------------------"+color.END)
          print(color.DARKCYAN+"Some more important points:")
          print("ANXIETY OVERVIEW: Definition:  Normal emotion of worry, fear, or unease.\n Becomes a concern when excessive, persistent, and disruptive (anxiety disorders).\n\n Symptoms:Physical: Rapid heartbeat, muscle tension, sweating.Cognitive: Excessive worrying, racing thoughts.\n Emotional: Restlessness, irritability, trouble sleeping.\n\nTreatment:\nTherapy: Cognitive-behavioral therapy (CBT), exposure therapy.\nMedications: Antidepressants, benzodiazepines (short-term), beta-blockers.\nLifestyle Changes: Exercise, healthy diet, adequate sleep, stress management.\n\nSelf-Help at Different Levels:\nMild Anxiety: Deep breathing, challenging irrational thoughts.\nModerate Anxiety: Journaling, physical activities.\nSevere Anxiety: Seek professional help, consider medication.\n\nWeekend Activities for Relief:Nature walks, creative outlets, socializing, relaxation techniques.\n\nDiet Recommendations:\nOmega-3 fatty acids (fish, flaxseeds, walnuts).\nWhole grains for steady energy.\nFruits and vegetables for antioxidants and vitamins.\nLimit caffeine and sugar intake.\n\nConclusion:\nIndividual responses vary, and consulting a healthcare professional for personalized advice is crucial. Implementing a holistic approach involving therapy, medication (if necessary), and lifestyle changes can contribute to managing anxiety effectively."+color.END)      
          break 
        return
       else:
        result = question_answering(question=question, context=context)
        print("Answer:", result['answer'])
