#Range and casting practise
Birth_year =int(input('Kindly enter your birth year'))
if Birth_year in range(1925,1946):
  print('You belong to the traditionalist gen')
elif Birth_year in range(1947,1964):
    print('You belong to the baby boomers gen')
elif Birth_year in range(1965,1981):
    print('You belong to the generation X')
elif Birth_year in range(1982,1995):
    print('You belong to the millenials gen')
elif Birth_year in range(1996,2015):
    print('You belong to the generation Z')
else:
    print('jao bacho mazay karo')

