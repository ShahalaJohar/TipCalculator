# Read the input heights as a list of strings
student_height = input("Enter the student heights separated by spaces: ").split()

# Convert each height from string to integer
for n in range(len(student_height)):
    student_height[n] = int(student_height[n])

# Calculate the total height
t_height = 0
for height in student_height:
    t_height += height

# Print the total height
print("Total height =", t_height)
 
