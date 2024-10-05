from steps import *
import random

#words to be used
words = [
    "joel","john","jackson","eugen","rebecca"
]

steps = [step1(),step2(),step3(),step4(),step5(),step6()]
randWord = random.randint(0,len(words))
theWord = words[randWord]
for i in theWord:
    print("-" * len(i), end="")
print()

count = 0
mentioned = []
correct = []

while count != 6:
    #print("The word to be filled is ")
    user = input("Enter your letter of guess for the word: ").lower()[0]

    #listing the letter used
    #the letters got correct

    #adding every letter typed
    mentioned.append(user)

    if user in theWord:
        correct.append(user)
    else:
        print(steps[count])
        count += 1

    print(f"mentioned characers are: {mentioned}")
    print(f"correct characters are: {correct}")

    if len(correct) == len(theWord):
        print(f"You won!, the word is {theWord}")
        break
