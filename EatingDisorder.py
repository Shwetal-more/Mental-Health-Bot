
from transformers import pipeline

def moderate():
    
    question_answering = pipeline("question-answering")
    context = """What is an eating disorder?
               An eating disorder is a serious, complex, mental health issue that one's affects emotional and physical health. 
              Types include:
            Anorexia nervosa: People with anorexia nervosa greatly restrict food and calories sometimes to the point of self-starvation.
           Binge eating disorder (BED): People who have a binge eating disorder experience compulsory eating behaviors.
            Bulimia nervosa: People diagnosed with bulimia nervosa binge or eat, or perceive they ate, large amounts of food over a short time.
         symptoms of eating disorder? Mood swings, Fatigue, fainting or dizziness, Thinning hair or hair loss, Frequent bathroom breaks after eating, Unexplained weight changes or drastic weight loss, Unusual sweating or hot flashes.
         Treatments include:
         Psychotherapy: A mental health professional can determine the best psychotherapy for your situation. 
         Many people with eating disorders improve with cognitive behavioral therapy (CBT). 
         Medications: Taking antidepressants or other medications can improve these conditions, As a result, your thoughts about yourself and food improve.
      Nutrition counseling: A registered dietitian with training in eating disorders can help improve eating habits and develop nutritious meal plans."""
    print("Please enter Exit to Exit the Question and answer bot")
    while True:
      question = input("user: ")
      if (question=='Exit' and question=='exit'):
        while True:
         print("Definition:\nDisruptive eating patterns leading to physical and mental health issues.\nIncludes conditions like anorexia nervosa, bulimia nervosa, and binge-eating disorder.\n\nSymptoms:\nAnorexia Nervosa: Extreme calorie restriction, fear of gaining weight.\nBulimia Nervosa: Binge-eating followed by purging behaviors.\nBinge-Eating Disorder: Consuming large amounts of food rapidly, loss of control.\n\nTreatment:\nTherapy: Cognitive-behavioral therapy (CBT), dialectical behavior therapy (DBT).\nNutritional Counseling: Guidance on healthy eating habits.\nMedical Monitoring: Especially for severe cases requiring hospitalization.\n\nSelf-Help at Different Levels:\nMild Eating Disorder: Maintain regular, balanced meals.\nModerate Eating Disorder: Establish a support network, consider self-help resources.\nSevere Eating Disorder: Seek professional help immediately, involve family or friends.\n\nWeekend Activities for Relief:\nRelaxation activities like reading or listening to music.\nEngage in non-food-related social events.\nOutdoor activities promoting a positive body-mind connection.\n\nDiet Recommendations:\nWork with a nutritionist for a balanced, sustainable meal plan.\nEmphasize a variety of food groups.\nAvoid extreme diets and restrictive eating habits.\n\nConclusion:\nAddressing eating disorders requires a comprehensive approach involving therapy, nutritional support, and medical monitoring. Early intervention is crucial, and individuals should seek professional help to develop a personalized treatment plan.")
         break 
        return
      else:
        result = question_answering(question=question, context=context)
        print("Answer:", result['answer'])




def dangerous():
    question_answering = pipeline("question-answering")
    context = """What is an eating disorder?
               An eating disorder is a serious, complex, mental health issue that one's affects emotional and physical health. 
              Types include:
            Anorexia nervosa: People with anorexia nervosa greatly restrict food and calories sometimes to the point of self-starvation.
           Binge eating disorder (BED): People who have a binge eating disorder experience compulsory eating behaviors.
            Bulimia nervosa: People diagnosed with bulimia nervosa binge or eat, or perceive they ate, large amounts of food over a short time.
         symptoms of eating disorder? Mood swings, Fatigue, fainting or dizziness, Thinning hair or hair loss, Frequent bathroom breaks after eating, Unexplained weight changes or drastic weight loss, Unusual sweating or hot flashes.
         Treatments include:
         Psychotherapy: A mental health professional can determine the best psychotherapy for your situation. 
         Many people with eating disorders improve with cognitive behavioral therapy (CBT). 
         Medications: Taking antidepressants or other medications can improve these conditions, As a result, your thoughts about yourself and food improve.
      Nutrition counseling: A registered dietitian with training in eating disorders can help improve eating habits and develop nutritious meal plans."""
    print("Please enter Exit to Exit the Question and answer bot")
    while True:
      question = input("user: ")
      if (question=='Exit' and question=='exit'):
        while True:
         print("Definition:\nDisruptive eating patterns leading to physical and mental health issues.\nIncludes conditions like anorexia nervosa, bulimia nervosa, and binge-eating disorder.\n\nSymptoms:\nAnorexia Nervosa: Extreme calorie restriction, fear of gaining weight.\nBulimia Nervosa: Binge-eating followed by purging behaviors.\nBinge-Eating Disorder: Consuming large amounts of food rapidly, loss of control.\n\nTreatment:\nTherapy: Cognitive-behavioral therapy (CBT), dialectical behavior therapy (DBT).\nNutritional Counseling: Guidance on healthy eating habits.\nMedical Monitoring: Especially for severe cases requiring hospitalization.\n\nSelf-Help at Different Levels:\nMild Eating Disorder: Maintain regular, balanced meals.\nModerate Eating Disorder: Establish a support network, consider self-help resources.\nSevere Eating Disorder: Seek professional help immediately, involve family or friends.\n\nWeekend Activities for Relief:\nRelaxation activities like reading or listening to music.\nEngage in non-food-related social events.\nOutdoor activities promoting a positive body-mind connection.\n\nDiet Recommendations:\nWork with a nutritionist for a balanced, sustainable meal plan.\nEmphasize a variety of food groups.\nAvoid extreme diets and restrictive eating habits.\n\nConclusion:\nAddressing eating disorders requires a comprehensive approach involving therapy, nutritional support, and medical monitoring. Early intervention is crucial, and individuals should seek professional help to develop a personalized treatment plan.")
         break 
        return
      else:
        result = question_answering(question=question, context=context)
        print("Answer:", result['answer'])


