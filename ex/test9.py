class MyClass:
    name = 'Sam'
    def sayHi(self):
        print("Hello %s" %self.name)
mc = MyClass()
print(mc)
print(mc.name)
mc.name = 'Lily'
mc.sayHi()