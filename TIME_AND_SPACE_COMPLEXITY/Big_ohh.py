# Time complexity is the amount of time it takes to run a program.
# Big O notation is a way of representing the time complexity of a program.

for i in range(1,6):
    print("Pradeepkumar B C")

# 3 Rules for Time complexity:

# Always calculate the time complexity of the worst case scenario.
# Example
age = 20
if age >= 80:
    print("Super Senior")
elif age >= 60 and age <= 80:
    print("Senior")
elif age >= 40 and age <= 60:
    print("Middle")
elif age >= 20 and age <= 40:
    print("Young")
else:
    print("Kid")



# Avoid the constant values
# Avoid the Lower Bound