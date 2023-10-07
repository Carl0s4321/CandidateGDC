answerYes = ["Yes", "Y", "yes", "y"]
answerNo = ["No", "N", "no", "n"]

while True:
    userInput = input(">>")
    if userInput in answerYes:
        print("YES!")
        break
    elif userInput in answerNo:
        print("NO!")
        break


