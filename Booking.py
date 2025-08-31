from abc import ABC, abstractmethod

"""
Stafflist variable here (require text file)
"""

StaffList = [

]

# class Booking(ABC):
#     @abstractmethod
#     def Job_Specialty_Staff(self):
#         pass

#     def Date(self):
#         pass

#     def Start_Time(self):
#         pass

#     def Staff(self):
#         pass

#     def Appointment(self):
#         pass

#     def Status(self, Checking_Booked):
#         pass

#     def End_Time(self):
#         pass

class Start_Booking:
    def __init__(self, staff_name, date, appointment, start_time, end_time):
        self._staff_name = staff_name
        self._date = date
        self._appointment = appointment
        self._start_time = start_time
        self._end_time = end_time

    def Set_Date(self, set_date):
        self._date = set_date

    """
    Sets the date of the booking
    """

    def Set_Start_Time(self, new_time):
        self._date = new_time
        
    """
    Sets the Starting time of the booking appointment
    """
    
    def Change_Appointment(self, New_Appointment_Type):
        self._Appointment

    """
    Changes the appointment type(the medical staff like nurse, GP or psychologist)
    """

    def Set_Staff(self, set_staff):
        pass

    """
    It sets a new staff for the person
    """

    def Change_Staff(self, New_Staff):
        pass
    
    """
    Changes the Staff of the booking
    """

    def Get_Date(self):
        pass

    """
    Get the date of the booking
    """

    def Get_Start_Time(self):
        pass

    """
    Get the Start Time of the appointment
    """

    def Get_End_Time(self):
        pass
    """
    Get the End Time of the appointment
    """

    def Get_Status(self):
        pass
    """
    Get the Status of the Booking (Booking is cancelled or not)
    """

    def Get_Staff(self):
        pass
    """
    Get the Medical Staff (Nurse, GP, Psychologist)
    """

    def Get_Appointment(self):
        pass

    """
    Get the the Appointment for the medical staff
    """

    def Cancel_Appointment(self):
        pass

    """
    Cancel the Appointment
    """

    def Reschedule_Appointment(self, Date, Time):
        pass

    """
    Change time for the appointment
    """

    def __str__(self):
        pass
