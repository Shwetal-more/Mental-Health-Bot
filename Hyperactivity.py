from transformers import pipeline

def moderate():
    
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
    
    question_answering = pipeline("question-answering")
    context = ""

    question = input("user: ")
    while True:
       result = question_answering(question=question, context=context)
       print("Answer:", result['answer'])
       break
    if (question=='Exit' and question=='exit'):
           return
