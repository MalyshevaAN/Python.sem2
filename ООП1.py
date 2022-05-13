class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def show(self):
        if self.hours < 10:
            print(f"0{self.hours}:{self.minutes}")
        else:
            print(f"{self.hours}:{self.minutes}")

    def ismorning(self):
        if self.hours >= 6 and self.hours < 12:
            self.partoftime = 'утро'
            return True
        else:
            return False

    def isday(self):
        if self.hours >= 12 and self.hours < 18:
            self.partoftime = 'день'
            return True
        else:
            return False

    def isevening(self):
        if self.hours >= 18 and self.hours < 22:
            self.partoftime = 'вечер'
            return True
        else:
            return False

    def isnight(self):
        if self.hours >= 22 and self.hours <= 24 or self.hours >= 0 and self.hours <= 5:
            self.partoftime = 'ночи'
            return True
        else:
            return False

    def sayhello(self):
        if not (self.isnight()):
            return f"Добрый {self.partoftime}!"
        else:
            return f"Доброй {self.partoftime}!"

    def addition(self, min):
        b = (self.minutes + min) // 60
        self.hours = (self.hours + b)%24
        self.minutes = (self.minutes + min) % 60


t1 = Time(12, 30)
t1.show()
print(t1.ismorning())
print(t1.isday())
print(t1.isevening())
print(t1.isnight())
print(t1.sayhello())
t1.addition(1200)
t1.show()
