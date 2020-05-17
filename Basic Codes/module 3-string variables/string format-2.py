#Write a program in python to declare four messages to the community 
# of technology that the Python programming language is wonderful 
# but describe python with a different description in each message 
# you will write, so one message with one python description then 
# answer the following questions:

msg1 = 'Python programming language is wonderful'
msg2 = 'The Python is Objective Oriented Programming'
msg3 = 'Python storing lots of module what you can import'
msg4 = 'Python will help you to coding with IntelliSense'

#How long each message you write is?
for strings in [msg1,msg2,msg3,msg4]:
    print(len(strings))

#what is the count of a specific letter in each message you will write?
for a in [msg1,msg2,msg3,msg4]:
    print(a.count('a'))

#are the codes you write end with "l"?
for l in [msg1,msg2,msg3,msg4]:
    print(l.endswith('l'))

#are the codes you write start with "T"?
for T in [msg1,msg2,msg3,msg4]:
    print(T.startswith('T'))