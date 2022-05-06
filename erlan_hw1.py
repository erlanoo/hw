class Car:
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        print(f"{self.title} {self.model} engine started")

    def stop_engine(self):
        print(f"{self.title} {self.model} engine stopped!")

    def all_info(self):
        print(f""" 
        {self.title} Title  
        {self.model} Model  
        {self.weight} Weighte 
        {self.hp} Hp 
        {self.nm} Nm  
        {self.max_speed}  Max speed 
        {self.color} Color 
        """)


MercedesBenz = Car("Mercedes", "maybach S-Класс", 2360, 621, 2300, 250, "BLACK")
MercedesBenz.start_engine()

MercedesBenz = Car("Mercedes", "maybach S-Класс", 2360, 621, 2300, 250, "BLACK")
MercedesBenz.stop_engine()

MercedesBenz = Car("Mercedes", "maybach S-Класс", 2360, 621, 2300, 250, "BLACK")
MercedesBenz.all_info()

audi = Car("AUDI", "R8", 1560, 602, 108, 330, "red")
audi.start_engine()

audi = Car("AUDI", "R8", 1560, 602, 108, 330, "red")
audi.stop_engine()

audi = Car("AUDI", "R8", 1560, 602, 108, 330, "red")
audi.all_info()
