#use of elif statement
print('LOGIN TO YOUR ACCOUNT')
print('---------------------')
user_name = input('Enter your username')
password = input('Enter your password')
if user_name == 'ali' and password == 'ali':
    print('Hello! ali we have been waiting for you')
elif user_name == 'asad' and password == 'asad':
    print('Hello! welcome to your account')
elif user_name == 'zubair' and password == 'zubair':
    print('Hello! zubair you have loggedin to your account')
else:
    print('sorry your username and password did not match')
