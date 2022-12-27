#an information collector
#coluring text or word in sentences
#things they like
liked_things=input('Tell us the things you like')
#things they hate
hated_things=input('Tell us the things you hate')
#their name
name =input('What is your name')
#father's name
Father_name=input("What is your father's name")
#friend's name
Friends_name=input('What is your friends name')
print("""Welcome to the information collector in python, in this collector we will convert it into a story and or audience will definitely enjoy it.
""")
print('Mr.','\033[31m',name,'\033[0m','son of',Father_name,'and friend of',Friends_name,'likes',liked_things,'and hates',hated_things)
