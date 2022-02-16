letter='''dear <|name|>,
    You Are Selected!
    date:<|date|>'''
    
Name=input("enter your name\n")
date=input("enter date \n")

letter = letter.replace("<|name|>", name)
letter = letter.replace("<|date|>", date)

print (letter)