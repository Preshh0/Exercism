
# def two_fer():

#     if two_fer != "":
#         print ("One for " + two_fer + " one for me." )
#     elif two_fer == str() :
#         print ("One for you, one for me.")
#     else:
#         raise Exception("Meaningful message indicating the source of the error")

# two_fer("name")


def two_fer():
    name = input("Please input name: ")
    print("One for " + name + ", one for me.")
    
def no():
    if two_fer() == True:
        print (two_fer())
    elif no() == None:
        print ("One for you, one for me.")
    else:
        print("Nothing.")


no()
'''
#This one's wrong too.

def name():
    user_input = input("What is your name?")
    print("One for " + user_input + ", one for you.")

def two_fer():
    print("One for you, one for me.")

if name() == True:
    print(name())
elif name() == False:
    print(two_fer())
'''

'''
#This too. Omo.
def name():
    user_input = input("What is your name?")
    print("One for " + name + ", one for me.")

def two_fer():
    if str(name()) == True:
        print(name())
    else:
        print("One for you, one for me.")
two_fer()

'''
# output = input("please input name: ")
# print(output)