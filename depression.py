from transformers import pipeline

print("Definition:\n\Persistent feeling of sadness, emptiness, or a loss of interest in daily activities.\nAffects mood, cognition, and physical well-being.\n\nSymptoms:\nEmotional: Prolonged sadness, hopelessness, irritability.\nCognitive: Difficulty concentrating, negative thoughts, feelings of worthlessness.\nPhysical: Changes in appetite, sleep disturbances, fatigue.\n\nTreatment:\nTherapy: Cognitive-behavioral therapy (CBT), psychodynamic therapy.\nMedications: Antidepressants (SSRIs, SNRIs, tricyclics).\nElectroconvulsive Therapy (ECT): For severe cases not responsive to other treatments.\n\nSelf-Help at Different Levels:\nMild Depression: Establish a routine, engage in pleasurable activities.\nModerate Depression: Reach out to friends and family for support, consider self-help resources.\nSevere Depression: Seek professional help immediately, involve a mental health professional.\n\nWeekend Activities for Relief:\nOutdoor activities and exposure to natural light.\nEngage in hobbies or activities that bring joy.\nAttend social events, even in a small and supportive setting.\n\nLifestyle Recommendations:\nRegular exercise to boost mood and energy.\nHealthy and balanced nutrition.\nEnsure adequate sleep and establish a consistent sleep routine.\n\nConclusion:\nDepression is a complex condition, and a combination of therapy, medication, and lifestyle changes can be effective. Seeking professional help is crucial, and early intervention enhances the likelihood of successful management and recovery.")
def moderate():
    question_answering = pipeline("question-answering")
    context = "What Is Depression? it appears as a persistent sad mood, reduced interest in your favorite activities, and having symptoms that negatively interfere with your daily functioning. What causes depression? Childhood experiences, Life events, Styles of thinking, Other mental health problems, Physical health problems, Family history, Medication, Recreational drugs and alcohol. How to treat depression? Doing exercise 2. geeting 8 to 9 hre sleep 3. meditation and yoga 4.doing relaxtation tecnique. what are symptoms of depression? Feeling unusually tired, feeling hopeless, feeling guilty or worthless, feeling overwhelmingly sad, having difficulty focusing, feeling unmotivated "
    question = input("user: ")
    while True:
       result = question_answering(question=question, context=context)
       print("Answer:", result['answer'])
       break
    if (question=='Exit' and question=='exit'):
           return

def dangerous():
    question_answering = pipeline("question-answering")
    context = "What Is Depression?it appears as a persistent sad mood, reduced interest in your favorite activities, and having symptoms that negatively interfere with your daily functioning. What are symptoms of depression? Seem sad or irritable more often than not, seem tired, lack energy, give up easily, put little effort into schoolwork, have trouble concentrating in class, fail to turn in work, get lower grades, seem not to enjoy things, withdraw from friends or activities, miss school or collage, or be frequently late. How to treat depression? Cognitive behavioral therapy for depression is a type of psychotherapy that modifies thought patterns to change moods and behaviors \n Three of the more common methods used in depression treatment include cognitive behavioral therapy, interpersonal therapy, and psychodynamic therapy. What is cognitive behavioral therapy? Common CBT techniques used for depression include cognitive restructuring, thought journaling, and mindful meditation\n Many of these techniques are used together to show the connections between thoughts, emotions, and behaviors.What are the 2 professional methods of treatment for depression? Medications and psychotherapy are effective for most people with depression."
    
    question = input("user: ")
    while True:
       result = question_answering(question=question, context=context)
       print("Answer:", result['answer'])
       break
    if (question=='Exit' and question=='exit'):
           return
       
