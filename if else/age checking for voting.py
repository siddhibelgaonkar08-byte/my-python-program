# Age checking for voting

currentYear = 2026

BirthYear= int (input(" Enter Your Birth Year:"))

Age = currentYear - BirthYear

print(" Your Current Age:",Age)

if Age>=18:
    print(" You are Eligible for Voting")
else:
    print(" You are not Eligible for Voting")