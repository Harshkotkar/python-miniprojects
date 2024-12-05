import random
def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess !=random.randint:
        guess=int(input(f"Guess a number btn 1 and {x}:"))
        if guess<random_number:
            print("Sorry,guess again.Too low.")
        elif guess>random_number:
            print("Sorry,guess again,Too high.")
        print(f"Congrats, you have made a correct guess {random_number}.")

def comp_guess(x):
    lower=1
    upper=x
    feedback=''
    while feedback !='c':
        guess=random.randint(lower,upper)
        feedback=input(f"{guess} is too high(H),too low(T),correct(C)???").lower()
        if feedback=='h':
            upper=guess-1
        elif feedback=='l':
            lower=guess+1
    print(f"computer guess the correct number,{guess}")

comp_guess(10)

