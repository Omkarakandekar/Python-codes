mydict ={
    "english":"rohan",
    "hindi": "rakesh",
    "marathi":"poonam",
    "tamil":"sagar"
}
print("languages are",mydict.keys())
a = input ("enter the favorite language\n" )
print("This language is favourite of:",mydict.get(a))
