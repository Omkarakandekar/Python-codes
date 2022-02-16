class X:
    
    x = "X"

new_func()

class Y(X)

y= "Y"

obj1 = X()

obj2 = Y()

print(issubclass (X,Y))

print(issubclass(Y.X))

print(isinstance(obj1,Y))

print (isinstance(obj2.X))