import re
match=input("Enter a identifier")
pattern=re.fullmatch('^[a-k]{1}[0369]{1}[a-zA-Z0-9#]*',match)
if pattern==None:
    print("Your Identifier is not accepted")
else:
    print("Identifier accepted")