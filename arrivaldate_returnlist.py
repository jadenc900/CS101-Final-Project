# Jaden Chee 2023-02-11

from calendar import *
from datetime import *
from logging.config import stopListening

def return_deadlines():
    print("Enter Date/Intended Date of Arrival (YYYY-MM-DD):\n\n")
    year = int(input('Year: '))
    month = int(input('Month: '))
    day = int(input('Day: ')) 

    if not 0 < month < 13:
       print('enter a valid month')
       raise Exception('month must be 01-12')
    elif not 0 < day < 32:
       print('enter a valid date')
       raise Exception(f'{day} is not a valid date in {month}') 

    arrivalDate = datetime(year, month, day)

    # calculating the deadline for 24hr Form
    deadline24hr = arrivalDate + timedelta(days = 1)

    # calulating the deadline for Residence Permit Appointment
    permit_date = datetime(year, month+1, day)

    res_permit_deadline = permit_date - timedelta(days = 1)

    # Health Checkup suggested last day
    health_check_deadline = permit_date - timedelta(days = 7)

    # need to do all other deadlines

    ### Maybe attempt table / calendar output ??? 
    print(f'Your Arrival Date: {year}-{month}-{day}')
    
    print('\nNon-negotiable Deadlines:\n')

    print("24 hour form by the end of the day", deadline24hr)

    print("\nSuggested Deadlines and Due-Dates:\n")
    
    print("Health Checkup Appointment (best) by", health_check_deadline)

    print("Last Day for Residence Permit Appointment: ", res_permit_deadline)

return_deadlines()