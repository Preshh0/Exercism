
# def two_fer():

#     if two_fer != "":
#         print ("One for " + two_fer + " one for me." )
#     elif two_fer == str() :
#         print ("One for you, one for me.")
#     else:
#         raise Exception("Meaningful message indicating the source of the error")

# two_fer("name")


def two_fer():
    # name = input("Please input name: ")

    if two_fer() == True:
        print ("One for " + two_fer() + ", one for you.")
    elif two_fer() == "":
        print ("One for you, one for me.")
    else:
        raise Exception("Supposed to print out hello greetings.")


two_fer()

# output = input("please input name: ")
# print(output)