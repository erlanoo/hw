from erlan_hw4 import pacage
class Car:
    def __init__(self,title,model,weight:int,hp:int,nm:int,max_speed:int,color):
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

    def car_info(self):
        print(f""" 
        {self.title} Title  
        {self.model} Model  
        {self.weight} Weight 
        {self.hp} Hp 
        {self.nm} Nm  
        {self.max_speed}  Max speed 
        {self.color} Color 
        """)


# def create_car(title: str,
#                 model: str,
#                 weight: int,
#                 hp: int,
#                 nm: int,
#                 max_speed: int,
#                 color:str
# )-> Car:
#    return Car(title, model, weight, hp, nm, max_speed, color)


bmw = Car('BMV_M6','sclass',5,6,19,250,"Белый")
mers = Car('banan','AMG',3,6,12,280,"Черный")
camry = Car('camry-360','turbo',2,7,15,190,"Синий")
def pacage():
    pakage_car = [bmw,mers,camry]

    for i in pakage_car:
        i.car_info()

bmw.start_engine()
bmw.stop_engine()