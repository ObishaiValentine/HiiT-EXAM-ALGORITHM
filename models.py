"""
Obishai Valentine code
400 level
HiiT plc Abuja

"""
import random
import json
import datetime
import user_crud
filename = "save.json"
"""
the chef speaker class with the number of participants necessary for the program
with also trying the use the execpt handling method to prevent errors 
"""

class chief_speaker:
    def _init_(self, name, email, mobile_number):
        self.name = name
        self.email = email
        self.mobile_number = mobile_number
        self.data = []

    def register(self):
        def _init_(self, name, email, mobile_number):
            super()._init_(name, email, mobile_number)
            self.__id = "CHF-" + str(random.randint(000, 999))
            self.__month = datetime.datetime.strp.month
            try:
                if self.email == True:
                    return("Email already exists")

                if len(mobile_number) > 11 or len(mobile_number) < 11:
                    return("Mobile number must be 11 digits")

                if name == "" or email == "" or mobile_number == "":
                    return("All fields are required")

                if len(mobile_number) == 11 and self.email == False:
                    return "Your account has been successfully created\n Your id:" + self.__id

                self.data = []
                with open(filename, "a") as file:
                    details = {
                        "name": self.name,
                        "email": self.email,
                        "mobile_number": self.mobile_number,
                        "id": self.__id,
                        "month": self.__month
                    }
                    for details in self.data:
                        json.dump(details, file)
            except:
                return("An error occured")


