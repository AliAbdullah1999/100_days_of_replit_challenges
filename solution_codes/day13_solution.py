#grade generator
total_marks = int(input('Please enter the total marks'))
marks_obtained = int(input('Enter the marks you obtained'))
aribitrary_marks = marks_obtained / total_marks
percentage = aribitrary_marks * 100
if percentage < 50:
    print('your grade is: "U"')
elif percentage in range(50, 59):
    print('your grade is: "D"')
elif percentage in range(60, 69):
    print('your grade is: "C"')
elif percentage in range(70, 79):
    print('your grade is: "B"')
elif percentage in range(80, 89):
    print('your grade is "A"')
else:
    print('your grade is "A++"')
