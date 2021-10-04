class Citizen:
    def __init__(self, name, age, dob, id_number):
        self.Citizen_name = name
        self.Citizen_age = age 
        self.Citizen_dob = dob
        self.Citizen_id_number = id_number
        
    def add_citizen(self):
        print("Name:" + self.Citizen_name)                                             
        print("Age:" + str(self.Citizen_age))
        print("Date of birth:" + self.Citizen_dob)
        print("Citizen id:" + self.Citizen_id_number)
        print("Citizen Added")
        
citizen1 = Citizen("Peter", "8", "19th October 2012", "0198")
citizen1.add_citizen()

citizen2 = Citizen("Sohpia", "10", "19th October 2010", "0199")
citizen2.add_citizen()