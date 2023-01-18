yourstring = input("Please Enter a string: ")
lowadd = ""
upadd = ""


for x in yourstring:

    if x.islower():
        lowadd += x

    if x.isupper():
        upadd += x


print(
    lowadd+upadd)
