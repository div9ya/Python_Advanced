class MyClass:
    var1="Divya"
    var2="Verma"

    # instance variables
    def __init__(self,dyn1,dyn2,dyn3):
        self.dyn1=dyn1 #Public variable
        self.__dyn2=dyn2 #Private variable
        self._dyn3=dyn3 #Protected

    def func1(self):
        print(f"Hello World, {self.dyn1}")

    def func2(self):
        print(f"Hello Globe, {self.__dyn2}")

    def func3(self):
        print(f"Hello India, {self.dyn3}")

obj=MyClass("abc","def","xyz")

#This will not create new varibale it will create an ew dyn2 variable in the object and assign the value"pqr" to it
obj.dyn2="pqr"
print(obj.dyn1, obj.dyn2)
obj.func2()

# Protected variable are accessible outside the class. it is not just recommended. it is a kind of warning

print(obj._dyn3)