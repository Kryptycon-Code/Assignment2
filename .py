from abc import ABC, abstractmethod

class Medical_Staff(ABC):
    def Staff_Name(self):
        pass
    
    def Job_Description(self):
        pass
    
    def Booking_list(self):
        pass
    
    @abstractmethod
    def Get_Daily_Capacity(self):
        pass

    def __init__(self):
        pass

    def __str__(self):
        pass

    def Get_Name(self):
        pass

    def Get_Description(self):
        pass

    def Set_Description(self, NewDescription):
        pass

    def Get_Booking_List(self):
        pass
    
    def Can_Book(self, Apointment: bool):
        pass

    def Add_Booking(self, Book):
        pass

class GP(Medical_Staff):
    def __init__(self):
        pass




