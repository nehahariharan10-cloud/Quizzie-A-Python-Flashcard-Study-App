import random

mathCards = [ # math problems
    ["Area of a circle", "pi r^2"],
    ["Pythagorean Theorem", "a^2 + b^2 = c^2"],
    ["Slope-intercept form", "y = mx + b"],
    ["Value of pi (2 decimal places)", "3.14"],
    ["Square root of 144", "12"],
    ["Sum of angles in a triangle", "180°"],
    ["Prime number after 7", "11"]]
scienceCards = [
    ["Chemical symbol for Gold", "au"],
    ["The powerhouse of the cell", "mitochondria"],
    ["Speed of light (approximate)", "300,000 km/s"],
    ["Common name for H2O", "water"],
    ["Planet closest to the Sun", "mercury"],
    ["Gas humans breathe out", "carbon dioxide"],
    ["Boiling point of water", "100°C"],
    ["The center of an atom", "nucleus"]
]
vocabCards = [ # vocab problems
    ["Ephemeral", "lasting for a very short time"],
    ["Eloquent", "fluent or persuasive in speaking or writing"],
    ["Pragmatic", "dealing with things sensibly and realistically"],
    ["Ambiguous", "open to more than one interpretation"],
    ["Benevolent", "well meaning and kindly"],
    ["Mitigate", "make less severe, serious, or painful"],
    ["Resilient", "able to recover quickly from difficulties"],
    ["Enigma", "something mysterious or difficult to understand"]
]
spanishCards = [ # spanish problems
    ["el cubo", "the cube"],
    ["la biblioteca", "the library"],
    ["el desayuno", "the breakfast"],
    ["siempre", "always"],
    ["la mariposa", "the butterfly"],
    ["izquierda", "left"],
    ["derecha", "right"],
    ["¿Cómo te llamas?", "what is your name?"]
]
customCards = [] # custom questions the user can make

correctCards = [] # questions the user got right
wrongCards = [] # questions the user got wrong
# both will be appended to

# Welcome/instructions
print ("Welcome to Quizzie!")
print("")
print ("Your #1 study buddy to ace your tests and build knowledge.")
print ("Type \"quit\" to quit the app.")
print ("Study one of our study sets (Math, Science, Vocab, Spanish) or create your own with \"Custom\"!")
print("Or, study cards you \"mastered\" or need more \"practice\" with!")
print("")

# function that checks the user's input for what they want to do.
def checkInput(x):
    if x == "math":
        for i in range (iterations): # user is asked how many problems of that topic they want, so they don't get asked what topic they want every time
            card = random.choice(mathCards) # picks a random card from the math set
            print(card[0]) # prints the question. each question is actually a list in the format [question, answer].
            answer = input("Answer: ") # asks user for their answer
            checkAnswer(answer, card) # checks the answer (this is a separate function)
    elif x == "science":
        for i in range (iterations):
            card = random.choice(scienceCards)
            print(card[0])
            answer = input("Answer: ")
            checkAnswer(answer, card)
    elif x == "vocab":
        for i in range (iterations):
            card = random.choice(vocabCards)
            print(card[0])
            answer = input("Answer: ")
            checkAnswer(answer, card)
    elif x == "spanish":
        for i in range (iterations):
            card = random.choice(spanishCards)
            print(card[0])
            answer = input("Answer: ")
            checkAnswer(answer, card)
    elif x == "custom": # custom options for the user
        customChoice = input("\"Make\" custom cards or \"study\" them? ").lower() # asks user if they want to make cards or study them
        for i in range (iterations):
            if customChoice == "make":
                customQuestion = input("Question: ") # collects question
                customAnswer = input ("Answer: ") # collects answer 
                customCards.append([customQuestion, customAnswer]) # appends list of custom questions with the new q and a
                print("Card saved!") # tells user their card is saved
            elif customChoice == "study":
                if customCards == []: # no custom cards to study
                    print("You haven't created any cards to study yet!")
                else: # custom cards avaliable to study
                    card = random.choice(customCards)
                    print(card[0])
                    answer = input("Answer: ")
                    checkAnswer(answer, card)
        else: # this is the else in CUSTOM: no other valid inputs
            print("Sorry, that is not a valid input. Please try again.")
    elif x == "mastered": # user practices the cards they already got right
        if correctCards == []: # no correct cards to practice
            print ("You haven't gotten any cards correct yet!")
        else: # correct cards available to practice
            card = random.choice(correctCards)
            print(card[0])
            answer = input("Answer: ")
            checkAnswer(answer, card)
    elif x == "practice":
        if wrongCards == []: # no wrong cards to practice
            print("You haven't missed any cards yet!")
        else: # wrong cards available to practice
            card = random.choice(wrongCards)
            print(card[0])
            answer = input("Answer: ")
            checkAnswer(answer, card)
    else:
        print("Sorry, that is not a valid input. Please try again.")
        
def checkAnswer(y, QandA): # procedure to check the answer
    if y.lower() == QandA[1]:
        print("Correct!")
        correctCards.append(QandA)
    else:
        print("That's not right. Correct answer: " + QandA[1])
        wrongCards.append(QandA)
    print("")

# actually running the program       
while True:
    cardType = (input("[•_•] What would you like to do? ")).lower()
    if cardType == "quit":
        print("[^_^] Thanks for studying!")
        break
    else:
        iterations = int(input("[•_•] How many problems? "))
        checkInput(cardType)