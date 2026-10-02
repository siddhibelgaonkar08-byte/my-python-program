# calculate student percentage
marathi= int(input ("Enter the marks marathi:"))
english= int(input ("Enter the marks english:"))
hindi= int(input ("Enter the marks hindi:"))
science= int(input ("Enter the marks science:"))

total= marathi+ english+ hindi+ science
percentage = total/4.0

print(f" percentage of all subject: { percentage}%")