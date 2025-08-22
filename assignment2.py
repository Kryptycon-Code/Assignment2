from abc import ABC, abstractmethod

class Medical_Staff(ABC):
    @abstractmethod
    def Staff_Name(self):
        pass
    
    @abstractmethod
    def Job_Description(self):
        pass
    
    @abstractmethod
    def Booking_list(self):
        pass

class Appointment(ABC):
    @abstractmethod
    def Client_Name(self):
        pass

    @abstractmethod
    def Contact_Number(self):
        pass

    @abstractmethod
    def Appointment_Type(self):
        pass


class GP(Medical_Staff):
    def __init__(self, name: str, JobDesc:str, bookinglist: list):
        self.NameOfStaff = name
        self._JobDescription = JobDesc
        self._booking_list = bookinglist

    def Staff_Name(self):
        return self.NameOfStaff
    
    def Job_Description(self):
        return self._JobDescription
    
    def Get_Booking_List(self):
        return self._booking_list
    
    def Modify_Job_Description(self, NewJobDesc):
        self._JobDescription = NewJobDesc
        return self._JobDescription
    
    
    
class GPAppointment:
    def __init__(self, TypeOfAppointment, ReasonOfAppointment):
        self.AppointmentType = TypeOfAppointment
        self.ReasonForAppointment = ReasonOfAppointment

    def Reason_For_Visit(self):
        return self.ReasonForAppointment
    
    def Type_Of_Appointment(self):
        return self.AppointmentType

class NurseAppointment:
    def __init__(self, TypeOfAppointment, VaccineType):
        self.AppointmentType = TypeOfAppointment
        self.Vaccine = VaccineType
    
    def Type_Of_Appointment(self):
        return self.AppointmentType
    
    def Vaccine_Type(self):
        pass