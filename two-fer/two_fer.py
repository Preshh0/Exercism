
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

    if name == True:
        print ("One for " + name + ", one for you.")
    elif name == "":
        print ("One for you, one for me.")
    else:
        raise Exception("Meaningful message indicating the source of the error")


two_fer()

# output = input("please input name: ")
# print(output)