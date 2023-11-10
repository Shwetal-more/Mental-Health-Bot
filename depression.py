from transformers import pipeline

def moderate():
    
    question_answering = pipeline("question-answering")
    context = """What Is Depression? it appears as a persistent sad mood, reduced interest in your favorite activities, and having symptoms that negatively interfere with your daily functioning.
      What causes depression? Childhood experiences, Life events, Styles of thinking, Other mental health problems, Physical health problems, Family history, Medication, Recreational drugs and alcohol. 
      How to treat depression? Doing exercise 2. geeting 8 to 9 hre sleep 3. meditation and yoga 4.doing relaxtation tecnique. 
    what are symptoms of depression? Feeling unusually tired, feeling hopeless, feeling guilty or worthless, feeling overwhelmingly sad, having difficulty focusing, feeling unmotivated """
    print("Please enter Exit to Exit the Question and answer bot")
    while True:
      question = input("user: ")
      if(question=='exit' or question=='Exit'):
        return
      else:
        result = question_answering(question=question, context=context)
        print("Answer:", result['answer']) 

def dangerous():
    
    question_answering = pipeline("question-answering")
    context = """What Is Depression?it appears as a persistent sad mood, reduced interest in your favorite activities, and having symptoms that negatively interfere with your daily functioning.
    What are symptoms of depression? Seem sad or irritable more often than not, seem tired, lack energy, give up easily, put little effort into schoolwork, have trouble concentrating in class, fail to turn in work, get lower grades, seem not to enjoy things, withdraw from friends or activities, miss school or collage, or be frequently late.
    How to treat depression? Cognitive behavioral therapy for depression is a type of psychotherapy that modifies thought patterns to change moods and behaviors 
    Three of the more common methods used in depression treatment include cognitive behavioral therapy, interpersonal therapy, and psychodynamic therapy. 
    What is cognitive behavioral therapy? Common CBT techniques used for depression include cognitive restructuring, thought journaling, and mindful meditation
    Many of these techniques are used together to show the connections between thoughts, emotions, and behaviors.What are the 2 professional methods of treatment for depression? Medications and psychotherapy are effective for most people with depression."""
    
    print("Please enter Exit to Exit the Question and answer bot")
    while True:
      question = input("user: ")
      if(question=='exit' or question=='Exit'):
        return
      else:
        result = question_answering(question=question, context=context)
        print("Answer:", result['answer']) 

