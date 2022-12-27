# class vehicle():
#     def __init__(self):
#         self.vehicle_number = None
#         self.color = None
#         self.manufactured_date = None

#     def drive(self):
#         print(f'{self.brand} is driving.')


# class car(vehicle):
#     def __init__(self):
#         self.number_of_wheels = 4
#         self.has_ac = False
#         self.has_music_system = False  

# class bike(vehicle):
#     def __init__(self):
#         self.number_of_wheels = 2
#         self.has_slipper_clutch = False

# honda_shine = bike()
# honda_shine.has_slipper_clutch = True
# honda_shine.color = 'Red'
# honda_shine.brand = 'Honda'

# print(honda_shine.color)
# honda_shine.drive()


# hyundai_creta = car()
# hyundai_creta.manufactured_date = 2019
# hyundai_creta.brand = 'Hyundai'
# hyundai_creta.drive()

#using super function

# class vehicle():
#     def __init__(self):
#         self.vehicle_number = None
#         self.color = None
#         self.manufactured_date = None

#     def drive(self):
#         self.start_engine()
    
#     def start_engine(self):
#         print(f'{self.brand} is driving.')


# class car(vehicle):
#     def __init__(self):
#         self.number_of_wheels = 4
#         self.has_ac = False
#         self.has_music_system = False  

# class bike(vehicle):
#     def __init__(self):
#         self.number_of_wheels = 2
#         self.has_slipper_clutch = False

#make a save method which appends the record of the user in csv file
# import csv
# class User:
#     def __init__(self,name,surname,age,gender):
#         self.first_name = name
#         self.last_name = surname
#         self.age = age
#         self.gender = gender
    
#     def full_details(self):
#         return f'{self.first_name}  {self.last_name}'
    
#     def save(self):
#         with open("test.csv",'a') as csvfile:
#             writer = csv.writer(csvfile)
#             writer.writerow(['First Name','Last Name','Age','Gender'])
#             writer.writerow([self.first_name,self.last_name,self.age,self.gender])
#             writer.writerow([self.full_details()])

# user =User('Ishan','Sapkota',23,'Male')

# user.save()



# import csv

# class csvsaver:

#     def save(self, filename):
#         self.id = super().id
#         self.username = super().username
#         self.surname = super().surname
#         self.age = super().age
#         self.gender = super().gender
#         self.animalname = super().animalname
#         self.species = super().species

#         with open(filename,'wt') as file:
#             writer = csv.writer(file)

#             if filename == 'user.csv':
#                 writer.writerow(['ID','Name','Surname','Age','Gender'])
#                 writer.writerow([self.username,self.surname,self.age,self.gender])
#             elif filename == 'animal.csv':
#                 writer.writerow(['ID','Name',"Species"])
#                 writer.writerow([self.id,self.animalname,self.species])
        
    

# class User(csvsaver):
    
#     def __init__(self,id,username,surname,age,gender):
#         self.id = id
#         self.username = username
#         self.surname = surname
#         self.age = age
#         self.gender = gender

#     def getrecords(self):
#         filename = 'user.csv'
#         list_of_records = []
#         with open(filename,'wt') as file:
#             writer = csv.writer(file)
#             writer.writerow["ID",'Name','Surname',"Age","Gender"]
#             print([self.id,self.username,self.surname,self.age,self.gender])
        
# class Animal(csvsaver):
#     def __init__(self,id,animalname,species):
#         self.id = id
#         self.animalname = animalname
#         self.species = species

#     def getrecords(self):
#         filename = 'animal.csv'
#         list_of_records1 = []
#         with open(filename,'a') as file:
#             writer = csv.writer(file)
#             writer.writerow(["ID",'Name','Species'])
#             print([self.id, self.animalname, self.species])

# lion = Animal(1,'Lion',"Cat")
# lion.save('animal.csv')

# lion.getrecords()

a = {}
n = int(input())
sum = 0
for i in range(0,n):
    a[i]=1
    sum = sum + (a[i]*a[i]*a[i])
    a[i] = a[i]+1
print(sum)