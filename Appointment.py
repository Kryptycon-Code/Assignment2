from abc import ABC, abstractmethod

class Appointment(ABC):
    @property
    @abstractmethod
    def client_name(self):
        pass

    @property
    @abstractmethod
    def contact_number(self):
        pass
    
    @property
    @abstractmethod
    def appointment_type(self):
        pass

class GPAppointment(Appointment):
    def __init__(self, type_of_appointment, reason_for_appointment, contact_number, client_name, mode):
        self._type_of_appointment = type_of_appointment
        self._reason_for_appointment = reason_for_appointment
        self._contact_number = contact_number
        self._client_name = client_name
        self._mode = mode
        self._duration = self._calculate_duration_with_mode()


    @property
    def reason_for_appointment(self):
        return self._reason_for_appointment
    
    @property
    def appointment_type(self):
        return self._type_of_appointment
    
    @appointment_type.setter
    def appointment_type(self, new_appointment_type):
        self._type_of_appointment = new_appointment_type
    
    @property
    def contact_number(self):
        return self._contact_number
    
    @contact_number.setter
    def contact_number(self, new_contact):
        self._contact_number = new_contact

    @property
    def client_name(self):
        return self._client_name
    
    @client_name.setter
    def client_name(self, new_client_name):
        self._client_name = new_client_name


    #-----------Duration Section------------------

    @property
    def mode(self):
        return self._mode
    
    @mode.setter
    def mode(self, change_mode):
        self._mode = change_mode
        self._duration = self._calculate_duration_with_mode()

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, changed_value):
        self._duration = changed_value

    #calculating the duration depending witht he mode
    def _calculate_duration_with_mode(self):
        if self._mode in ("Telehealth" or "Standard"):
            return 15
        elif self._mode == "Long":
            return 60
