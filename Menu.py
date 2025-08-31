# ===========================
# Menu
# ===========================
from Appointment import Appointment, GPAppointment


def main_menu():
# First entry menu (Staff / Client / Exit)
    “””
    Inputs: interactive user input via ‘input()’ (only accept “1”, “2”, and “3”)
    Outputs: 
    - Displayed menu text to the console log 
    - Returns None when user chooses Exit
    ”””
    while True: 
        print(“\n — BeeHealthy Clinic System —”)
        print(“1. Staff Menu”)
        print(“2. Client Menu”)
        print(“3. Exit”)
        
        sel = input(“Select your role:”)

        Main_Menu_Actions = {
            "1": staff_menu,
            "2": client_menu,
            "3": lambda: print("Thank you for visiting BeeHealthy Clinic System!”)
        }

    
        
        # if sel == “1”:
        #     staff_menu()
        # elif sel == “2”:
        #     cient_menu()
        # elif sel == “3”: 
        #     print(“Thank you for visiting BeeHealthy Clinic System!”)
        #     break
        # else:
        #     print(“Invalid. Try again!”)
    
def staff_menu(): 
    # show the staff menu and direct actions to MedicalStaff action handlers
    “””
    Inputs: interactive user input via ‘input’ 
    Outputs: printed placeholders to add, edit, display the availability, and save details of staff
    ”””
    while True: 
        print(“\n — Staff Menu — ”)
        print(“1. Add a new staff”)
        print(“2. Edit the details of an existing staff”)
        print(“3. Display available staff”)
        print(“4. Delete a staff”)
        print(“5. Save details in a text file”)
        print(“6. Return to the main menu”)
        sel = input(“Please Enter Your Choice: ”)
        if sel == “1”: 
            MedicalStaff.add_new_staff()
        elif sel == “2”: 
            MedicalStaff.edit_staff_details()
        elif sel == “3”: 
            MedicalStaff.display_available_staff()
        elif sel == “4”: 
            MedicalStaff.delete_staff()
        elif sel == “5”:
            MedicalStaff.save_details_to_file()
        elif sel == “6”:
            print(“Back to the main menu”)
            return
        else: 
            print(“Invalid! Try again!”)

def client_menu()
# show the client menu and perform booking, cancellation, and editing flows
“””
Inputs: interactive user input via ‘input()’
Outputs: Printed placeholders for book/cancel/edit
”””
while True: 
    print(“\n — Client Menu —”)
    print(“1. Book an appointment”)
    print(“2. Cancel an appointment”)
    print(“3. Edit an appoinment”)
    print(“4. Return to the main menu”)
    sel = input(“Please Enter Your Choice: ”)
    if sel == “1”: 
        MedicalStaff.book()
    elif sel == “2”: 
        Booking.cancel_appointment()
    elif sel == “3”: 
        Booking.edit_appointment()
    elif sel == “4”: 
        print(“Returning to the Main Menu…”)
        return
    else: 
        print(“Invalid. Please try again!”)
