
#! 1. Classes and Objects
class Car:
    def __init__(self, brand, model):  # Constructor method to initialize object properties
        self.brand = brand  # Instance variable to store car brand
        self.model = model  # Instance variable to store car model

    def honk(self):  # Method to simulate horn sound
        return f"{self.brand} {self.model} says: Honk!"


my_car = Car("Toyota", "Corolla")  # Creating an instance of the Car class
print(my_car.brand, my_car.model)  # Accessing instance variables


#! 2. Class Attributes, Methods and variables
class Rectangle:
    num_objects = 0  # Class-level attribute to count instances

    def __init__(self, width, height):
        self.width = width  # Instance variable for width
        self.height = height  # Instance variable for height
        Rectangle.num_objects += 1  # Incrementing class attribute

    def area(self):
        return self.width * self.height  # Calculating area using instance variables


rect1 = Rectangle(5, 3)
rect2 = Rectangle(4, 6)
print(rect1.area())  # Calling method on instance
print(Rectangle.num_objects)  # Accessing class attribute


#! 3. Constructors
class Person:
    def __init__(self, name, age):  # Constructor to initialize person object
        self.name = name  # Setting instance variable for name
        self.age = age  # Setting instance variable for age


person1 = Person("Alice", 30)
print(person1.name, person1.age)  # Accessing instance variables


#! 4. Constructor Overloading (Python doesn't support true constructor overloading)
class CarOverload:
    def __init__(self, brand):  # First constructor
        self.brand = brand  # Setting instance variable for brand

    def __init__(self, brand, model):  # Second constructor (simulating overload)
        self.brand = brand  # Setting instance variable for brand
        self.model = model  # Setting instance variable for model


car1 = CarOverload("Toyota")
car2 = CarOverload("Honda", "Civic")
print(car1.brand)  # Accessing instance variable
print(car2.brand, car2.model)  # Accessing multiple instance variables


#! 5. Inheritance and Polymorphism
class Animal:
    def sound(self):  # Abstract method for animal sound
        pass  # Placeholder implementation


class Dog(Animal):
    def sound(self):  # Overriding abstract method
        return "Woof!"  # Specific implementation for dog


class Cat(Animal):
    def sound(self):  # Overriding abstract method
        return "Meow!"  # Specific implementation for cat


def animal_sound(animal):  # Function using polymorphism
    print(animal.sound())  # Calling overridden method


dog = Dog()
cat = Cat()

animal_sound(dog)  # Passing instance of Dog
animal_sound(cat)  # Passing instance of Cat


#! 6. Abstraction and Encapsulation
class BankAccount:
    def __init__(self, account_number, balance=0):  # Constructor with default balance
        self.__account_number = account_number  # Private attribute for account number
        self.__balance = balance  # Private attribute for balance

    def deposit(self, amount):  # Method to deposit money
        if amount > 0:  # Basic validation
            self.__balance += amount  # Updating private balance
            print(f"Deposited ${amount}. New balance: ${self.__balance}")

    def get_balance(self):  # Method to access balance (encapsulation)
        return self.__balance


account = BankAccount("12345", 1000)  # Creating account with initial balance
account.deposit(500)  # Using encapsulated method
print(account.get_balance())  # Accessing encapsulated attribute


#! 7. Static Methods and Class Methods
class Math:
    @staticmethod  # Decorator for static methods
    def add(a, b):
        return a + b  # Simple addition without object

    @classmethod  # Decorator for class methods
    def multiply(cls, a, b):  # First parameter is always the class itself
        return a * b  # Multiplication using class


print(Math.add(3, 4))  # Calling static method
print(Math.multiply(3, 4))  # Calling class method
