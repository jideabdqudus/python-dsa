x, y, p, q, r = 1,2,3,4, 'pop'

print(str(x))

name = 'brad'
age = 23

print(f"my name is {name}, and I'm {age} years old" )

list1 = [1,2,3,4]
list2 = list((1,2,3,4))

list1.append(9)
print(list1)

def sayHello(name = 'Sam'):
    print(f'say hello {name}')

sayHello('Jide' )

# Lambda Function
getSum = lambda num1, num2 : num1 + num2

print(getSum(2, 4))

# Create Class
class User:
    def __init__(self, name, age, mail):
        self.name = name
        self.age = age
        self.mail = mail

    def greetings(self):
        return f'How are you doing {self.name}'

    def has_birthday(self):
        self.age +=1

brad = User('Brad', 32, 'test@test.com')
brad.has_birthday()
print(brad.age)


# Extend Class
class Customer(User):
    def __init__(self, name, age, mail):
        self.name = name
        self.age = age
        self.mail = mail
        self.balance = 0
    def set_balance(self, balance):
        self.balance = balance
    def greetings(self):
        return f'How are you doing {self.name}, and balance of {self. balance}'
    def bio(self):
        myBio =  {
            "age": self.age,
            "name": self.name,
            "mail": self.mail,
            "balance": self.balance
        }
        return myBio


janet = Customer('Janet', 25, 'kas@kas.com')
janet.set_balance(433)
janet.has_birthday()
print(janet.bio())

