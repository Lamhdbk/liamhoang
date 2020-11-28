from sys import argv
script, user_name = argv
prompt ='n'
print("Hi %s, I'm the %s script." %(user_name, script))
print("I'd like to ask you a few question.")
print("Do you like me %s" %user_name)
likes= input()
print("Where do you live %s" %user_name)
lives = input()
print("WHat kind of computer do you have?")
computer = input()

print("""Ok, you sai %r about linking me."
      "you live in %r. Not sure that is."
      "And you have a %r computer. Nice""" %(likes, lives, computer))