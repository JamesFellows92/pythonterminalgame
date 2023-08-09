import Questions_data
import sys
import os
import subprocess

#Prize Money

prize_money = {
1: "£100",
2: "£200",
3: "£300",
4: "£500",
5: "£1,000",
6: "£2,000",
7: "£4,000",
8: "£8,000",
9: "£16,000",
10: "£32,000",
11: "£64,000",
12: "£125,000",
13: "£250,000",
14: "£500,000",
15: "£1,000,000",
}

# Welcome statements
print("Welcome to 'Who Wants to be a Millionaire'")
print("The rules are simple, answer 15 questions correctly to win the £1 million jackpot")
print("As we progress through the questions will get harder, and you can walk away at certain intervals with your winnings")
print("The prize money increments are as follows:")
print("Question 1 = £100\nQuestion 2 = £200\nQuestion 3 = £300\nQuestion 4 = £500\nQuestion 5 = £1,000\nQuestion 6 = £2,000\nQuestion 7 = £4,000\nQuestion 8 = £8,000\nQuestion 9 = £16,000\nQuestion 10 = £32,000\nQuestion 11 = £64,000\nQuestion 12 = £125,000\nQuestion 13 = £250,000\nQuestion 14 = £500,000\nQuestion 15 = £1,000,000")
print("You can choose to walk away after winning £1,000 and £32,000")
print("A wrong answer will leave you with nothing")
player_name = input("Please enter your name to get started ")
print("Ok " + player_name + ". Let's play, 'Who Wants to be a Millionaire'")

for question in Questions_data.quiz_questions:
    if question.multiple_choice_options != None:
        print(f"{question.question_text}")
        for option in question.multiple_choice_options:
            print(option)
        user_input = input()
    else:
        print(f"{question.question_text}?")
        user_input = input()
    if user_input.lower() == question.answer.lower():
        print("That is correct")
        print("You have answered Question " + str(question.question_counter) + " correctly")
        print("You have won " + (prize_money[question.question_counter]))
    else:
        print(f"Sorry, that is incorrect. The correct answer is {question.answer}")
        break
    if question.question_counter == 5:
        go_home = input(player_name + " you have reached £1,000. Would you like to walk away with what you have? Please type 'Y' or 'N' ")
        if go_home == "Y":
            print("Thanks for playing! You go home today with " + prize_money[question.question_counter] + " .Spend it wisely!")
            break
        else:
            continue
    if question.question_counter == 10:
        go_home = input(player_name + " you have reached £32,000. Would you like to walk away with what you have? Please type 'Y' or 'N' ")
        if go_home == "Y":
            print("Thanks for playing! You go home today with " + prize_money[question.question_counter] + " .Spend it wisely!")
            break
        else:
            continue
    if question.question_counter == 15:
        print("YOU ARE A MILLIONAIRE!!")

replay = input("Do you want to play again? Please type 'Y' or 'N' ")
if replay == "Y":
    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
           
