
from transformers import pipeline

def moderate():
    
    question_answering = pipeline("question-answering")
    context = """An eating disorder is a serious, complex, mental health issue that one's affects emotional and physical health.
                People with eating disorders develop an unhealthy relationships with food, their weight or appearance. 
                  type of eating disorder? Anorexia, bulimia and binge eating disorder are all types of eating disorders. 
                  Anorexia nervosa: People with anorexia nervosa greatly restrict food and calories sometimes to the point of self-starvation.
                  Bulimia nervosa: People diagnosed with bulimia nervosa binge or eat, or perceive they ate, large amounts of food over a short time.
                  Binge eating disorder (BED): People who have a binge eating disorder experience compulsory eating behaviors. 
                  Symptoms of eating disorder:Mood swings, Fatigue, fainting or dizziness, Thinning hair or hair loss, Frequent bathroom breaks after eating, Unexplained weight changes or drastic weight loss, Unusual sweating or hot flashes.
                  Treatments include:
                  Psychotherapy:A mental health professional can determine the best psychotherapy for your situation.
                  Medications: Some people with eating disorders have other conditions, like anxiety or depression.
                  Nutrition counseling: A registered dietitian with training in eating disorders can help improve eating habits and develop nutritious meal plans. 
                  """
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
    context = """An eating disorder is a serious, complex, mental health issue that one's affects emotional and physical health.
                People with eating disorders develop an unhealthy relationships with food, their weight or appearance. 
                  type of eating disorder? Anorexia, bulimia and binge eating disorder are all types of eating disorders. 
                  Anorexia nervosa: People with anorexia nervosa greatly restrict food and calories sometimes to the point of self-starvation.
                  Bulimia nervosa: People diagnosed with bulimia nervosa binge or eat, or perceive they ate, large amounts of food over a short time.
                  Binge eating disorder (BED): People who have a binge eating disorder experience compulsory eating behaviors. 
                  Symptoms of eating disorder:Mood swings, Fatigue, fainting or dizziness, Thinning hair or hair loss, Frequent bathroom breaks after eating, Unexplained weight changes or drastic weight loss, Unusual sweating or hot flashes.
                  Treatments include:
                  Psychotherapy:A mental health professional can determine the best psychotherapy for your situation.
                  Medications: Some people with eating disorders have other conditions, like anxiety or depression.
                  Nutrition counseling: A registered dietitian with training in eating disorders can help improve eating habits and develop nutritious meal plans. 
                  """
    print("Please enter Exit to Exit the Question and answer bot")
    while True:
      question = input("user: ")
      if(question=='exit' or question=='Exit'):
        return
      else:
        result = question_answering(question=question, context=context)
        print("Answer:", result['answer']) 


       
