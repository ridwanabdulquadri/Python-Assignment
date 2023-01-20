import reandom

def math-quiz
	name = input("Please enter your name to register\n)
if len(name) < 1:

print("Your name is important for registration")
	math-quiz()
 print(f"""
                {name}, welcome to my short quiz
            Your are to answer 5 questions correctly
            """)

    count = 0
    correct = 0
    fail = 0
    while count < 5:
        number1 = random.randint(1, 50)
        number2 = random.randint(1, 50)

        reply = eval(input("\nwhat is " + str(number1) + " + " + str(number2) + " ?\n"))
        result = number1 + number2

        if reply == result:
            print("Excellent!", number1, "+", number2, "=", reply)
            correct += 1
        else:
            print("Oops!", number1, "+", number2, "=", result, "not", reply)
            fail += 1
        count += 1

    if correct == 0:
        print("\n", name, "you be olodo ooo\nYou got", str(correct), "correct and", str(fail), "wrong")
    elif 1 < correct <= 3:
        print("\n", name, " you tried. You could do better next time\nYou got", str(correct), "correct and", str(fail), "wrong")
    elif correct == 4:
        print("\nYou did wonderful", name, "\nYou got", str(correct), "correct and", str(fail), "wrong")
    elif correct == 4:
        print("\nCongratulations perfect", name, "\nYou got", str(correct), "correct and", str(fail), "wrong")


if _name_ == '_main_':
    math_quiz()
def math_quiz():
    name = input("Please enter your name to register\n")
    if len(name) >= 1:

        print(f"""
                        {name}, welcome to my short quiz
                    Your are to answer 5 questions correctly
                    """)

        count = 0
        correct = 0
        fail = 0
        while count < 5:
            number1 = random.randint(1, 50)
            number2 = random.randint(1, 50)

            reply = eval(input("\nwhat is " + str(number1) + " + " + str(number2) + " ?\n"))
            result = number1 + number2

            if reply == result:
                print("Excellent!", number1, "+", number2, "=", reply)
                correct += 1
            else:
                print("Oops!", number1, "+", number2, "=", result, "not", reply)
                fail += 1
            count += 1

        if correct == 0:
            print("\n", name, "you be olodo ooo\nYou got", str(correct), "correct and", str(fail),
"wrong")
        elif 1 < correct <= 3:
            print("\n", name, " you tried. You could do better next time\nYou got", str(correct), "correct and",
                  str(fail), "wrong")
        elif correct == 4:
            print("\nYou did wonderful", name, "\nYou got", str(correct), "correct and", str(fail), "wrong")
        elif correct == 4:
            print("\nCongratulations perfect", name, "\nYou got", str(correct), "correct and", str(fail), "wrong")
    else:
        print("Your name is important for registration")


if _name_ == '_main_':
    math_quiz()