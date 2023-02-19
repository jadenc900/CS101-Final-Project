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

    # Health Check recommended day 
    health_check_date = arrivalDate + timedelta(days = 6)

    # Health Checkup suggested last day
    health_check_deadline = permit_date - timedelta(days = 7)

    # SIM Card suggested timeline
    simdate = arrivalDate + timedelta(days = 2)

    # Bank Account suggested
    bankdate = arrivalDate + timedelta(days = 3)

    ### Maybe attempt table / calendar output ??? 
    print(f'Your Arrival Date: {year}-{month}-{day}')
    
    print('\nNon-negotiable Deadlines:\n')

    print("Submit 24 hour form application by the end of the day", deadline24hr)
    print("You will need this form to apply for your residence permit")

    print("Health Checkup Appointment by", health_check_deadline)

    print("Last Day for Residence Permit Appointment: ", res_permit_deadline)

    print("\nSuggested Deadlines and Due-Dates:\n")

    print("Try to obtain your SIM card by", simdate)
    print("You will need a Chinese phone number to open a bank account")

    print("Try to open your bank account by", bankdate)
    print("You will need a bank account to use Wechat Pay and in some instances," \
        "to use Alipay.")

    print("try to schedule your health appointment on", health_check_date)
    print("new appointments are added on Thursday each week")

    print("This is the ISS recommended timeline")

    

return_deadlines()