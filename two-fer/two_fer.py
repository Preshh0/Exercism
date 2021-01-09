def two_fer(name):
   # name = "Alice"

    if name != "":
        return("One for " + name + ", one for me.")
    else:
        return("One for you, one for me.")

print(two_fer("Alice"))

'''
    default parameter argument example

    # def two_fer(name = "Alice"):
    #     if name != "":
    #         print("One for " + name + ", one for me.")
    #     else:
    #         print("One for you, one for me.")

    # two_fer("")
    # two_fer()

'''