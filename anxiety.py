from transformers import pipeline

def moderate():
    
    question_answering = pipeline("question-answering")
    context = "What is anxiety?Anxiety is your body’s natural response to stress. What is considered severe anxiety? People with severe anxiety usually experience more distress and less ability to function. A person with this condition may also report symptoms similar to those of major depression, such as fatigue, headaches, and impaired concentration and memory. How do i help myself?1.Talk to someone you trust add, Talking to someone you trust about what's making you anxious could be a relief 2.Look after your physical health 3.Try breathing exercises 4.Keep a diary 5.Complementary and alternative therapies.What is the 3 3 3 rule for anxiety? The 333 rule for anxiety is an easy technique to remember and use in the moment if something is triggering your anxiety. It involves looking around your environment to identify three objects and three sounds, then moving three body parts.What are the 4 stages of anxiety? Levels of anxiety can be influenced by personality, coping strategies, life experiences, and gender. Anxiety levels are typically classified by the level of distress and impairment experienced into four categories: mild anxiety, moderate anxiety, severe anxiety and panic level anxiety.What is panic anxiety? Panic disorder is an anxiety disorder where you regularly have sudden attacks of panic or fear. Everyone experiences feelings of anxiety and panic at certain times. It's a natural response to stressful or dangerous situations.How do you stop panic attacks? 1.Remember that it will pass 2.Take deep breaths 3.Smell some lavender 4.Find a peaceful spot 5.Focus on an object 6.Repeat a mantra 7.Walk or do some light exercise."
    while True:
        question = input("user: ")

        result = question_answering(question=question, context=context)
        print("Answer:", result['answer'])


def dangerous():
    question_answering = pipeline("question-answering")
    context = "What is anxiety? Anxiety is your body’s natural response to stress. How do you treat anxiety? Some ways to manage anxiety disorders include learning about anxiety, mindfulness, relaxation techniques, correct breathing techniques, dietary adjustments, exercise, learning to be assertive, building self-esteem, cognitive therapy, exposure therapy, structured problem solving, medication and support groups.What is the most successful treatment for anxiety? Cognitive behavioral therapy (CBT) is the most effective form of psychotherapy for anxiety disorders. Effects of anxiety on your body: a fast, thumping or irregular heartbeat, sweating or hot flushes, sleep problems, grinding your teeth, especially at night, nausea (feeling sick), needing the toilet more or less often, changes in your sex drive, having panic attacks. What is panic anxiety? Panic disorder is an anxiety disorder where you regularly have sudden attacks of panic or fear. Everyone experiences feelings of anxiety and panic at certain times. It's a natural response to stressful or dangerous situations.How do you stop panic attacks? 1.Remember that it will pass 2.Take deep breaths 3.Smell some lavender 4.Find a peaceful spot 5.Focus on an object 6.Repeat a mantra 7.Walk or do some light exercise.What tablets calm you down? Benzodiazepines,Benzodiazepines are a type of sedative that may sometimes be used as a short-term treatment during a particularly severe period of anxiety."
    while True:
        question = input("user: ")

        result = question_answering(question=question, context=context)
        print("Answer:", result['answer'])


