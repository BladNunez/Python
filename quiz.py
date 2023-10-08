#Quiz Game (Countries and Continents)

questions = {"Question 1" : {"Question" : "What is the capital of France?" ,
                             "Answer" : "Paris"},
             "Question 2" : {"Question" : "What Continent is Brazil in?" ,
                             "Answer" : "South America"},
             "Question 3" : {"Question" : "What is the capital of Spain?" , 
                             "Answer" : "Madrid"},
             "Question 4" : {"Question" : "Austria is in what Continent?" ,
                             "Answer" : "Europe"},
             "Question 5" : {"Question" : "Will you move oversees?" , 
                             "Answer" : "Yes"},
                             }

score = 0

for key, value in questions.items():
        print(value["Question"])
        answer = raw_input("Answer: ")

        if answer == value['Answer']:
                print("Correct!")
                score += 1
                print("Your Score is " + str(score))
        else:
                print("Wrong Answer! Correct answer was " + value["Answer"])

print("Quiz Final Score: " + str(score))

