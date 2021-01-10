
def two_fer(name = "Alice"):

    if name != "":
        return(f"One for {name}, one for me.")
    else:
        return("One for you, one for me.")

print(two_fer())
print(two_fer("Bob"))
print(two_fer(""))


