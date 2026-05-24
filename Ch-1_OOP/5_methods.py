class MyClass:

    my_var=100

    # def __init__(self,value):
    #     self.value=value

#     def change_value(self,new_value):
#         MyClass.my_var=new_value

# obj1=MyClass()
# obj1.change_value(200)
# print(MyClass.my_var)

# obj2=MyClass()
# print(obj2.my_var)

    # dunder method or magic method 
    def __init__(self):
        print("This is constructor method")

    # dunder method for string
    def __str__(self):
        return "This is the string representation of the object"
    
    @classmethod
    def _change_value(cls,new_value):
        cls.my_var=new_value
    
    @staticmethod
    def dummy():
        print("This is dummy method")

obj1=MyClass()
obj1._change_value(200)
print(MyClass.my_var)

obj2=MyClass()
print(obj2.my_var)       

obj3=MyClass()
obj3.dummy()

obj4=MyClass()
print(obj4.__str__())