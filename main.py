import random
import time

class Car:
    def __init__(self, brand, fuel=100):
        self.brand = brand
        self.fuel = fuel

    def drive(self, distance):
        fuel_needed = distance * 2
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            print(f"You drove {distance} km. Fuel left: {self.fuel}%")
            return True
        else:
            print("Not enough fuel! Go refuel first!")
            return False

    def refuel(self):
        self.fuel = 100
        print("Car refueled to 100%!")

class Passenger:
    def __init__(self):
        self.distance = random.randint(5, 20)
        self.fare = self.distance * random.randint(5, 10)

    def info(self):
        print(f"New passenger wants to go {self.distance} km — fare: ${self.fare}")

class Human:
    def __init__(self, name, car):
        self.name = name
        self.car = car
        self.money = 0

    def take_passenger(self):
        passenger = Passenger()
        passenger.info()
        accept = input("Accept this passenger? (yes/no): ").lower()
        if accept == "yes":
            success = self.car.drive(passenger.distance)
            if success:
                self.money += passenger.fare
                print(f"You earned ${passenger.fare}. Total: ${self.money}")
        else:
            print("Passenger ignored.")

    def play(self):
        print(f"\nWelcome {self.name}! You are a taxi driver with a {self.car.brand}.")
        print("Try to earn as much money as possible!\n")
        time.sleep(1)

        while True:
            action = input("\nChoose action (drive/refuel/status/exit): ").lower()
            if action == "drive":
                self.take_passenger()
            elif action == "refuel":
                self.car.refuel()
            elif action == "status":
                print(f"Car fuel: {self.car.fuel}% | Money: ${self.money}")
            elif action == "exit":
                print(f"\nGame over! You earned a total of ${self.money}.")
                break
            else:
                print("Invalid action!")

car = Car("Toyota")
player = Human("John", car)
player.play()