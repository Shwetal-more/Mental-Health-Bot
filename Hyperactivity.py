from transformers import pipeline

def moderate():
    
    question_answering = pipeline("question-answering")
    context = "what is hyperactivity?1 Hyperactivity means a person may seem to move about constantly including in situations when it is not appropriate or excessively fidgets taps or talks In adults hyperactivity may mean extreme restlessness or talking too much.How to reduce hyperactivity?1 Give clear effective directions or commands Establish healthy habits 2 Develop routines around homework and chores 3 Help your child build relationships strong social skills and maintain friendships.What is an example of hyperactivity disorder?The main signs of hyperactivity and impulsiveness are :1  being unable to sit still especially in calm or quiet surroundings constantly fidgeting 2 being unable to concentrate on tasks.Is hyperactive child normal?Most healthy children are inattentive, hyperactive or impulsive at one time or another.Can hyperactive go away with age? People may find that their symptoms lessen and increase at times throughout their life.Is hyperactive good or bad?Hyperactivity is often considered more of a problem for schools and parents than it is for the child.Is hyperactivity serious? The symptoms of ADHD can interfere significantly with an individual's daily activities and relationships. What foods decrease hyperactivity?A high-protein diet like Beans, cheese, eggs, meat, and nuts can be good sources of protein.Is hyperactivity Treatable?Standard treatments for ADHD in adults typically involve medication, education, skills training and psychological counseling.Is hyperactive a mental disorder?Attention-deficit/hyperactivity disorder (ADHD) is one of the most common mental disorders affecting children."

    question = input("user: ")
    while True:
       result = question_answering(question=question, context=context)
       print("Answer:", result['answer'])
       break
    if (question=='Exit' and question=='exit'):
           return

def dangerous():
    
    question_answering = pipeline("question-answering")
    context = "what is hyperactivity?1 Hyperactivity means a person may seem to move about constantly including in situations when it is not appropriate or excessively fidgets taps or talks In adults hyperactivity may mean extreme restlessness or talking too much.Can hyperactivity be dangerous?if not addressed, these risks can lead to injury, disease, or even an earlier-than-expected death.Is hyperactive child abnormal?Hyperactivity is a state of being unusually or abnormally active.How to reduce hyperactivity?1 Give clear effective directions or commands Establish healthy habits 2 Develop routines around homework and chores 3 Help your child build relationships strong social skills and maintain friendships.What is an example of hyperactivity disorder?The main signs of hyperactivity and impulsiveness are :1  being unable to sit still especially in calm or quiet surroundings constantly fidgeting 2 being unable to concentrate on tasks.Is hyperactive child normal?Most healthy children are inattentive, hyperactive or impulsive at one time or another.Can hyperactive go away with age? People may find that their symptoms lessen and increase at times throughout their life.Is hyperactive good or bad?Hyperactivity is often considered more of a problem for schools and parents than it is for the child.Is hyperactivity serious? The symptoms of ADHD can interfere significantly with an individual's daily activities and relationships. What foods decrease hyperactivity?A high-protein diet like Beans, cheese, eggs, meat, and nuts can be good sources of protein.Is hyperactivity Treatable?Standard treatments for ADHD in adults typically involve medication, education, skills training and psychological counseling.Is hyperactive a mental disorder?Attention-deficit/hyperactivity disorder (ADHD) is one of the most common mental disorders affecting children."

    question = input("user: ")
    while True:
       result = question_answering(question=question, context=context)
       print("Answer:", result['answer'])
       break
    if (question=='Exit' and question=='exit'):
           return
