class MyClass:
    """a simple class"""
    i = 12345

    def hello(self):
        return 'hello world'

my_object = MyClass()
print(my_object.i)
print(MyClass.__doc__)
print(my_object.hello())