import os
os.system('cls' if os.name == "nt" else "clear")

'''
class ClassName:
    variable_for_class = 'value' #Attribute/Property

    def example_function(parametre, arguman):

         # if (conditions) ... wrong using
        
        variable_for_func = 'value' #Parametre

'''

# class Person:
#     name = 'TOST'
#     surname = 'Parkinson'

#     #print(Person)
# print(Person.name)

# personel = Person()
# print(personel)
# print(personel.name)

# personel.name = 'tarik'
# personel.surname = 'Salvator'
# personel.age = 40

# print(personel.name)
# print(personel.surname)
# print(personel.age)


# class Person:
#     name = 'TOST'
#     surname = 'Parkinson'

# personel_1 = Person()

# print(personel_1.name)

# Person.name = 'Migael'

# print(personel_1.name)


# class Person:
#     name = 'TOST'
#     surname = 'Parkinson'
#     __location = 'Deutschland'

#     def get_location(self):
#        return self.__location
#     def set_location(self , new_val):
#        self.__location = new_val

#        personel = Person()
#        print(personel.get_location())
#        personel.set_location('Germany')
#        print(personel.get_location())

# class SendMail:
#     __is_sent = False

#     def set_send(self):
#         self.__is_sent = True

#     def get_status(self):
#         return self.__is_sent    

# mail = SendMail()
# print('mail gonderildi mi?',mail.get_status())
# mail.send()
# print('mail gitti mi?',mail.set_status())


# class  Person:
#     name  = 'TOST'
#     surname = 'Parkinson'
    
#     @staticmethod
#     def test():
#         print('hallo')

#     @staticmethod
#     def hallo(name,surname):
#         print('Hallo' + ' ' + name + '  ' + surname)    

# personel =  Person()
# personel.test()
# personel.hallo('tost' , 'birmingham')

# class  Person:
#     name  = 'TOST'
#     surname = 'Parkinson'
    
#     def __str__(self) -> str:
#         return 'a class that I wrote'
    
#     def __init__(self) -> None:
#        self.name = 'Damon'
#        self.surname = "Salvatore"

# print(Person)    
# personel = Person()
# print(personel)
