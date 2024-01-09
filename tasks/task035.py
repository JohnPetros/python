# Task 35 - Write a script that reads the width of the three straight lines of a triangle and informs the user whether they can form a triangle or not

print('-=' * 20)
print('Analisador de triângulo')
print('-=' * 20)

line1 = float(input('First line: '))
line2 = float(input('Second line: '))
line3 = float(input('Third line: '))

if line1 + line2 > line3 and line2 + line3 > line1 and line1 + line3 > line2:
  print('The entered lines CAN FORM a triangle')
else:
  print('The entered lines CAN NOT FORM a triangle')
  