name = input("Name: ")
age = int(input("age: "))
GPA = floatinput("Enter you GPA (on a scale 4.0): "))
field = input ("Field of Interest:")
graduated = input("have you graduated? ")
if age < 25 and GPA >= 3.5 and graduated ==
"yes":
print("You are eligible for a scholarship.")
elif age < 30 and GPA >= 2.5:
print("You are eligible for an internship.")
else:
print("Please apply again later.")