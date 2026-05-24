class MyClass:
    var1="Divya"
    var2="Verma"

    # instance variables
    def __init__(self,dyn1,dyn2,dyn3):
        self.dyn1=dyn1
        self.dyn2=dyn2
        self.dyn3=dyn3

    def func1(self):
        print(f"Hello World, {self.dyn1}")

    def func2(self):
        print(f"Hello Globe, {self.dyn2}")

    def func3(self):
        print(f"Hello India, {self.dyn3}")

obj=MyClass("abc","def","xyz")
obj.func1()
obj.func2()
obj.func3()

obj_new=MyClass("pqr","stu","vwx")
obj_new.var2="changed"
print(obj_new.var2)