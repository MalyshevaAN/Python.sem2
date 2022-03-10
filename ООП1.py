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
        if self.hours >=6 and self.hours < 12:
            self.partoftime = 'утро'
            print(True)
        else:
            print(False)
    def isday(self):
        if self.hours >=12 and self.hours <18:
            self.partoftime = 'день'
            print(True)
        else:
            print(False)
    def isevening(self):
        if self.hours >=18 and self.hours < 22:
            self.partoftime = 'вечер'
            print(True)
        else:
            print(False)
    def isnight(self):
        if self.hours >=22 and self.hours <= 24 or self.hours >= 0 and self.hours <= 5:
            self.partoftime = 'ночи'
            print(True)
        else:
            print(False)
    def sayhello(self):
        if self.partoftime != 'ночи':
            print(f"Добрый {self.partoftime}!")
        else:
            print(f"Доброй {self.partoftime}!")

    def addition(self,min):
        b = (self.minutes + min) // 60
        self.hours = (self.hours + b)
        self.minutes = (self.minutes + min)%60



t1 = Time(12, 30)
t1.show()
t1.ismorning()
t1.isday()
t1.isevening()
t1.isnight()
t1.sayhello()
t1.addition(120)
t1.show()

