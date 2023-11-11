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


def moderate():
    question_answering = pipeline("question-answering")
    context = """ Depression appears as a persistent sad mood, reduced interest in your favorite activities, and having symptoms that negatively interfere with your daily functioning. 
     Causes of depression are Childhood experiences, Life events, Styles of thinking, Other mental health problems, Physical health problems, Family history, Medication, Recreational drugs and alcohol.
    Treatment of depression is Doing exercise,geeting 8 to 9 hre sleep,meditation and yoga and doing relaxtation tecnique.
     Symptoms of depression are Feeling unusually tired,feeling hopeless,feeling guilty or worthless,feeling overwhelmingly sad,having difficulty focusing and feeling unmotivated """
    print(color.YELLOW+color.BOLD+"Please enter Exit to Exit the Question and answer bot"+color.END)
    while True:
      question = input("user: ")
      if (question=='Exit' or question=='exit'):
        while True:
          print(color.ORANGE+"-----------------------------------------------------------------------------------"+color.END)
          print(color.DARKCYAN+"Some more important points:")
          print("DEPRESSION OVERVIEW:\nDefinition: Persistent feeling of sadness, emptiness, or a loss of interest in daily activities.\nAffects mood, cognition, and physical well-being.\n\nSymptoms:\nEmotional: Prolonged sadness, hopelessness, irritability.\nCognitive: Difficulty concentrating, negative thoughts, feelings of worthlessness.\nPhysical: Changes in appetite, sleep disturbances, fatigue.\n\nTreatment:\nTherapy: Cognitive-behavioral therapy (CBT), psychodynamic therapy.\nMedications: Antidepressants (SSRIs, SNRIs, tricyclics).\nElectroconvulsive Therapy (ECT): For severe cases not responsive to other treatments.\n\nSelf-Help at Different Levels:\nMild Depression: Establish a routine, engage in pleasurable activities.\nModerate Depression: Reach out to friends and family for support, consider self-help resources.\nSevere Depression: Seek professional help immediately, involve a mental health professional.\n\nWeekend Activities for Relief:\nOutdoor activities and exposure to natural light.\nEngage in hobbies or activities that bring joy.\nAttend social events, even in a small and supportive setting.\n\nLifestyle Recommendations:\nRegular exercise to boost mood and energy.\nHealthy and balanced nutrition.\nEnsure adequate sleep and establish a consistent sleep routine.\n\nConclusion:\nDepression is a complex condition, and a combination of therapy, medication, and lifestyle changes can be effective. Seeking professional help is crucial, and early intervention enhances the likelihood of successful management and recovery."+color.END)
          break 
  
        return
      else:
        result = question_answering(question=question, context=context)
        print("Answer:", result['answer'])


def dangerous():
    question_answering = pipeline("question-answering")
    context = """ Depression appears as a persistent sad mood, reduced interest in your favorite activities, and having symptoms that negatively interfere with your daily functioning. 
    Symptoms of depression of feeling sad or irritable more often than not,seem tired,lack energy,give up easily, put little effort into schoolwork, have trouble concentrating in class, fail to turn in work, get lower grades, seem not to enjoy things, withdraw from friends or activities, miss school or collage, or be frequently late. 
    Treatment of depression are Cognitive behavioral therapy,interpersonal therapy and psychodynamic therapy. 
    Cognitive behavioral therapy: Common CBT techniques used for depression include cognitive restructuring,thought journaling, and mindful meditation.
    Many of these techniques are used together to show the connections between thoughts, emotions, and behaviors.
     The 2 professional methods of treatment for depression are Medications and psychotherapy ."""
    
    print(color.YELLOW+color.BLUE+"Please enter Exit to Exit the Question and answer bot"+color.END)
    while True:
      question = input("user: ")
      if (question=='Exit' or question=='exit'):
        while True:
          print(color.ORANGE+"-----------------------------------------------------------------------------------"+color.END)
          print(color.DARKCYAN+"Some more important points:")
          print("DEPRESSION OVERVIEW:\n Definition: Persistent feeling of sadness, emptiness, or a loss of interest in daily activities.\nAffects mood, cognition, and physical well-being.\n\nSymptoms:\nEmotional: Prolonged sadness, hopelessness, irritability.\nCognitive: Difficulty concentrating, negative thoughts, feelings of worthlessness.\nPhysical: Changes in appetite, sleep disturbances, fatigue.\n\nTreatment:\nTherapy: Cognitive-behavioral therapy (CBT), psychodynamic therapy.\nMedications: Antidepressants (SSRIs, SNRIs, tricyclics).\nElectroconvulsive Therapy (ECT): For severe cases not responsive to other treatments.\n\nSelf-Help at Different Levels:\nMild Depression: Establish a routine, engage in pleasurable activities.\nModerate Depression: Reach out to friends and family for support, consider self-help resources.\nSevere Depression: Seek professional help immediately, involve a mental health professional.\n\nWeekend Activities for Relief:\nOutdoor activities and exposure to natural light.\nEngage in hobbies or activities that bring joy.\nAttend social events, even in a small and supportive setting.\n\nLifestyle Recommendations:\nRegular exercise to boost mood and energy.\nHealthy and balanced nutrition.\nEnsure adequate sleep and establish a consistent sleep routine.\n\nConclusion:\nDepression is a complex condition, and a combination of therapy, medication, and lifestyle changes can be effective. Seeking professional help is crucial, and early intervention enhances the likelihood of successful management and recovery."+color.END)
          break 
        return
      else:
        result = question_answering(question=question, context=context)
        print("Answer:", result['answer'])
