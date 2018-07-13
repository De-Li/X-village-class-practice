# class Ball: 
#     color = 'BLACK'
#     def set_radius(self, radius_arg):
#         self.radius = radius_arg
        
#     def calculate_volume(self): # 計算球體體積
#         volume1 = 4/3 * 3.14 * (self.radius*self.radius*self.radius)
#         return volume1

#     def calculate_surface_area(self): # 計算球體表面積
#         self.surface_area = 4 * 3.14 * (self.radius*self.radius)
        
# x = Ball() # 建立 instance object

# x.set_radius(5)
# volume2 = x.calculate_volume()
#  # 呼叫計算體積method
# print('球體體積', volume2) 

# x.calculate_surface_area() # 呼叫計算表面積method
# print('球體表面積', x.surface_area) 
#--------------------------------------------------------------------------------------------------------------------
# class health:
#     weight = 100
#     height = 170
#     def setdata(self,weightarg,heightarg):
#         self.weight=weightarg
#         self.height=heightarg
#     def BMI(self):
#         self.bmi = (self.weight/(self.height**2))*10000
#         print(self.bmi)
#     def Name(self,namearg):
#         self.name = namearg
#     def judge(self):
#         if self.bmi > 26.0:
#             print(self.name + "你過肥")
#         elif self.bmi <26.0 and self.bmi >18.0:
#             print(self.name + "身材剛好呢！")
#         else :
#             print(self.name + "過瘦")
# man = health()
# man.Name('peter')
# man.setdata(100,200)
# man.BMI()
# man.judge()
#-------------------------------------------------------------------------------------------------
# class shape:
#     def set_edge(self,edgearg):
#         self.edge=edgearg
#     def display(self):
#         for i in range(self.edge+1):
#             print('* '*i)
# tri=shape()
# input_=int(input("input edge: "))
# tri.set_edge(input_)
# tri.display()