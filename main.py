# # class User:
# #     def __init__(self,id,name,lastname,age,email):
# #         self.id = id
# #         self.name = name
# #         self.lastname = lastname
# #         self.age = age
# #         self.email = email
# #
# #
# #
# #
# #
# # users = (1,'Toxir','Toxirov',28,'toxir@gmail.com')
# #
# # user = User(users[0],users[1],users[2],users[3],users[4])
# # print(user.name)
# # -----------------------------------------------------------------------------
#
#
# # class User:
# #     def __init__(self,id,name,lastname,age,email):
# #         self.id = id
# #         self.name = name
# #         self.lastname = lastname
# #         self.age = age
# #         self.email = email
# #
# #
# #
# #
# #
# # users = (1,'Toxir','Toxirov',28,'toxir@gmail.com')
# #
# # user = User(users[0],users[1],users[2],users[3],users[4])
# # print(user.name)
#
# # from collections import namedtuple
# # User = namedtuple('User','id name lastname age email')
# #
# # users = [
# #     (1,'Toxir','Toxirov',28,'toxir@gmail.com'),
# #     (2,'Toxir','Toxirov',18,'toxir@gmail.com'),
# #     (3,'Toxir','Toxirov',35,'toxir@gmail.com'),
# # ]
# #
# # for user in users:
# #     us = User(*user)
# #     print(us.id,us.name,us.lastname,us.age,us.email)
#
#
# from collections import namedtuple
#
# Car_menu = namedtuple('Car','name color speed km place how')
#
# car = ('Malibu','Red','300kmh',20000,4,'Avtomat')
#
# car_data = Car_menu(*car)
# print(car_data.name,car_data.color,car_data.speed,car_data.km,car_data.place,car_data.how)