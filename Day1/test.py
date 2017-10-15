age_of_oldboy = 56
guess_age == int(input("guess age:"))

if guess_age == age_of_oldboy:
    print("yes,you got it")
elif guess_age > age_of_oldboy:
    print("think,small")
else guess_age < age_of_oldboy:
    print("think,big")