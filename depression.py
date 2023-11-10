from transformers import pipeline

def moderate():
    question_answering = pipeline("question-answering")
    context = ""
    while True:
        question = input("user: ")

        result = question_answering(question=question, context=context)
        print("Answer:", result['answer'])


def dangerous():
    question_answering = pipeline("question-answering")
    context = "" 
    while True:
        question = input("user: ")

        result = question_answering(question=question, context=context)
        print("Answer:", result['answer'])

       
