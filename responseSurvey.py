import json
f = open("responseSurvey.json", 'r')
contents = json.load(f)
print(contents)
f.close()

f = open("responseSurvey.json", 'w')

Survey = {'moes': 0, 'willys': 0, 'chipotle': 0}

while True:

    addName = input("Hello, what's your name?")
    print("Hello", addName)

    Question = input("Which do you like better, MOES, WILLY'S or CHIPOTLE?")
    if Question == "moes":
        moes = Survey[Question]
        Survey[Question] = moes + 1
        print(Survey)

    elif Question == "willys":
        willys = Survey[Question]
        Survey[Question] = willys + 1
        print(Survey)

    elif Question == "chipotle":
        chipotle = Survey[Question]
        Survey[Question] = chipotle + 1
        print(Survey)

    else:
        print("Sorry,that wasn't an option. Please try again.")

    areWeFinished = input("Has everyone finished the survey? y/n ")
    if areWeFinished == 'y':
        break
print(Survey)
json.dump(Survey, f)
