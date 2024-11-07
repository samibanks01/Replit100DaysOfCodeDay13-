print("Exam Grade Calculator")

print()

exam = input("Name of exam: ")

print()

maxScore = int(input("Max. Possible Score: "))

print()

yourScore = int(input("Your score: "))

print()

percentage = round(float(yourScore / maxScore) * 100, 2)

if percentage >= 90:
  print("You got", percentage, "% which is an A+")
elif percentage >= 80 and percentage <= 89:
  print(percentage, "% which is an A-")
elif percentage >= 70 and percentage <= 79:
  print(percentage, "% which is a B")
elif percentage >= 60 and percentage <= 69:
  print(percentage, "% which is a C")
elif percentage >= 50 and percentage <= 59:
  print(percentage, "% which is a D")
elif percentage <= 49:
  print(percentage, "% which is a U")
else:
  print("Try again!")
  
