from transformers import pipeline

def moderate():
    print("Definition:\nExcessive, uncontrolled levels of physical activity.\nOften associated with conditions like ADHD (Attention Deficit Hyperactivity Disorder).\n\nSymptoms:\nPhysical: Inability to sit still, fidgeting, restlessness.\nCognitive: Impulsivity, difficulty focusing.\nBehavioral: Difficulty engaging in quiet activities, excessive talking.\n\nTreatment\nBehavioral Therapy: Applied Behavioral Analysis (ABA).\nMedications: Stimulants (e.g., methylphenidate), non-stimulants (e.g., atomoxetine).\nParental Training: Techniques for managing behavior at home.\n\nSelf-Help at Different Levels:\nMild Hyperactivity: Incorporate regular breaks in activities.\nModerate Hyperactivity: Establish structured routines, use visual aids.\nSevere Hyperactivity: Seek professional help, consider medication under supervision.\n\nWeekend Activities for Relief:\nStructured physical activities (sports, swimming).\nMindfulness activities, such as yoga or meditation.\nEngage in hobbies that channel energy constructively.\n\nDiet Recommendations:\nBalanced meals with a focus on protein, complex carbohydrates, and healthy fats.\nLimit artificial additives and sugars.\nEnsure adequate hydration.\n\nConclusion:\nAddressing hyperactivity involves a combination of behavioral interventions, medications when appropriate, and creating a supportive environment. Consulting with healthcare professionals, including behavioral therapists and pediatricians, is crucial for tailored guidance.")


    question_answering = pipeline("question-answering")
    context = ""

    question = input("user: ")
    while True:
       result = question_answering(question=question, context=context)
       print("Answer:", result['answer'])
       break
    if (question=='Exit' and question=='exit'):
           return

def dangerous():
    print("Definition:\nExcessive, uncontrolled levels of physical activity.\nOften associated with conditions like ADHD (Attention Deficit Hyperactivity Disorder).\n\nSymptoms:\nPhysical: Inability to sit still, fidgeting, restlessness.\nCognitive: Impulsivity, difficulty focusing.\nBehavioral: Difficulty engaging in quiet activities, excessive talking.\n\nTreatment\nBehavioral Therapy: Applied Behavioral Analysis (ABA).\nMedications: Stimulants (e.g., methylphenidate), non-stimulants (e.g., atomoxetine).\nParental Training: Techniques for managing behavior at home.\n\nSelf-Help at Different Levels:\nMild Hyperactivity: Incorporate regular breaks in activities.\nModerate Hyperactivity: Establish structured routines, use visual aids.\nSevere Hyperactivity: Seek professional help, consider medication under supervision.\n\nWeekend Activities for Relief:\nStructured physical activities (sports, swimming).\nMindfulness activities, such as yoga or meditation.\nEngage in hobbies that channel energy constructively.\n\nDiet Recommendations:\nBalanced meals with a focus on protein, complex carbohydrates, and healthy fats.\nLimit artificial additives and sugars.\nEnsure adequate hydration.\n\nConclusion:\nAddressing hyperactivity involves a combination of behavioral interventions, medications when appropriate, and creating a supportive environment. Consulting with healthcare professionals, including behavioral therapists and pediatricians, is crucial for tailored guidance.")
    question_answering = pipeline("question-answering")
    context = ""

    question = input("user: ")
    while True:
       result = question_answering(question=question, context=context)
       print("Answer:", result['answer'])
       break
    if (question=='Exit' and question=='exit'):
           return
