
def two_fer():
    name = "Jane"
    if name == "Jane":
        print ("One for %r, one for me." %name)
    elif name == "" :
        print ("One for you, one for me.")
    else:
        raise Exception("Meaningful message indicating the source of the error")

two_fer()