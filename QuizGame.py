import random

questions = {
    "python": {
        "easy":[
            {"question": "What is the correct file extension for Python files?",
             "options": ["A) .py","B) .python","C) .pyt","D) .pt"],
             "answer":"A"},
            {"question": "Which of the following is a valid variable name in Python?",
             "options": ["A) 2variable","B) variable_name","C) variable-name","D) variable.name"],
             "answer":"B"},
            {"question": "Which keyword is used to define a function in Python?",
             "options": ["A) function","B) define","C) def","D) func"],
             "answer":"C"}
            ],
        "medium": [
            {"question": "Which of the following is true about Python's lambda functions?",
            "options": [
            "A) They are also known as anonymous functions.",
            "B) They can contain multiple expressions.",
            "C) They can have statements in their body.",
            "D) They are defined using the `def` keyword."],
            "answer": "A"},
            {"question": "What will be the output of the following code?"
             '''python
            def func(a, b=[]):
                b.append(a)
                return b
            result = func(1)
            result = func(2, [])
            result = func(3)
            print(result)
            ''',
            "options": [
            "A) [1, 2, 3]",
            "B) [3]",
            "C) [1, 3]",
            "D) [3, 1]"],
            "answer": "C"},
            {"question": "What is the result of the following operation?\n"
            '''python
             'a'* 5''',
            "options": [
            "A) 'aaaaa'",
            "B) 'a5'",
            "C) Error",
            "D) None of the above"],
            "answer": "A"}
            ],
        "hard": [
            {"question": "Which of the following statements is true about Python’s @staticmethod decorator?",
             "options": ["A) A static method can access instance variables.","B)  A static method does not take self as its first parameter.","C) A static method is bound to the instance of the class.","D) A static method can access the class variables."],
             "answer":"B"},
            {"question": "Which of the following will create an empty NumPy array?",
             "options": ["A) numpy.array([])","B) numpy.empty([])","C) numpy.zeros([])","D) numpy.zeros(0)"],
             "answer":"A"},
            {"question": "What is the output of the following code snippet?"
             '''def f(x, lst=[]):
                    for i in range(x):
                    lst.append(i*i)
                    print(lst)
                f(2)
                f(3, [3, 2, 1])
                f(3)'''
             ,
             "options":
                 ["A) '[0, 1] [3, 2, 1, 0, 1, 4] [0, 1, 4]'",
                  "B) '[0, 1] [3, 2, 1, 0, 1, 4] [0, 1]'",
                  "C) '[0, 1] [3, 2, 1, 0, 1, 4] [0, 1, 4, 9]'",
                  "D) '[0, 1] [3, 2, 1, 0, 1] [0, 1, 4, 9]'"],
             "answer":"C"}
            ],
    },
    "java": {
        "easy": [
            {"question": "Which of the following is a valid declaration of an array in Java?",
             "options": ["A) int arr[];","B) int arr;","C) arr[10];","D) array int arr[];"],
             "answer": "A"},
            {"question": "Which of these cannot be used for a variable name in Java?",
             "options": ["A) identifier","B) variable","C) 1variable","D) var"],
             "answer": "C"},
            {"question": "Which of the following is used to handle exceptions in Java?",
             "options": ["A) try-catch","B) do-while","C) for","D) if-else"],
             "answer": "A"}
            ],
        "medium": [
            {"question": "Which keyword is used to inherit a class in Java?",
             "options": ["A) extends","B) implements","C) inherits","D) super"],
             "answer": "A"},
            {"question": "What is the purpose of the 'this' keyword in Java?",
             "options": [
                 "A) Refers to the current object instance",
                 "B) Refers to the superclass",
                 "C) Refers to the constructor",
                 "D) Refers to the method parameter"],
             "answer": "A"},
            {"question": "Which method must be implemented by a class implementing the Runnable interface?",
             "options": ["A) start()","B) run()","C) execute()","D)) init()"],
             "answer": "B"}
            ],
        "hard": [
            {
            "question": "What is the default encoding used for byte to string conversion in Java?",
            "options": [
            "A) UTF-16",
            "B) UTF-8",
            "C) ISO-8859-1",
            "D) US-ASCII"
            ],
            "answer": "B"},
            {
            "question": "What is the output of the following code?"
             '''
            public class Main
            {
                public static void main(String[] args) {
                        int x = 5;
                        x = x++ * 2 + 3 * --x;
                        System.out.println(x);
                }
            }
            ''',
            "options": [
            "A) 30",
            "B) 31",
            "C) 33",
            "D) 34"
            ],
            "answer": "C"},
            {
            "question": "In Java, which of the following statements about the 'finally' block is true?",
            "options": [
            "A) It is executed only when an exception is thrown.",
            "B) It can be used to end the loop.",
            "C) It is executed whether an exception is thrown or not.",
            "D) It can contain the return statement."
            ],
            "answer": "C"}
            ]
    }
}

def quiz_game():
    print("Welcome to the Quiz Game!")
    name = input("Enter your name: ")
    
    print(f"Hello, {name}! Choose a topic: python or java")
    topic = input("Topic: ").lower()
    
    if topic not in questions:
        print("Invalid topic. Please choose python or java.")
        return
    
    print(f"Choose a difficulty level: easy, medium, or hard")
    difficulty = input("Difficulty: ").lower()
    
    if difficulty not in questions[topic]:
        print("Invalid difficulty level. Please choose easy, medium, or hard.")
        return
    
    score = 0
    questions_list = questions[topic][difficulty]
    random.shuffle(questions_list)
    
    for q in questions_list:
        print(f"Question: {q['question']}")
        for option in q['options']:
            print(option)
        user_answer = input("Your answer: ")
        if user_answer.strip().upper() == q['answer'].strip().upper():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {q['answer']}")
    
    print(f"Your final score is: {score}/{len(questions[topic][difficulty])}")
    print("Thank you for playing the Quiz Game!")

quiz_game()
