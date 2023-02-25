from datetime import *
from logging.config import stopListening

def return_deadlines():
    # this will be changed to take from the database
    print("Enter Date/Intended Date of Arrival (YYYY-MM-DD):\n\n")
    year = int(input('Year: '))
    month = int(input('Month: '))
    day = int(input('Day: ')) 
    print() 

    today = datetime.now()
    today = today.strftime("%Y-%m-%d")
    print("Today's Date:", today, "\n")

    if not 0 < month < 13:
       print('enter a valid month')
       raise Exception('month must be 01-12')
    elif not 0 < day < 32:
       print('enter a valid date')
       raise Exception(f'{day} is not a valid date in {month}') 

    arrivalDate = datetime(year, month, day)

    # submit health insurance form
    health_insurance = arrivalDate - timedelta(days = 3)
    health_insurance = health_insurance.strftime("%Y-%m-%d")

    # calculating the deadline for 24hr Form
    deadline24hr = arrivalDate + timedelta(days = 1)
    deadline24hr = deadline24hr.strftime("%Y-%m-%d")

    # calulating the deadline for Residence Permit Appointment
    permit_date = datetime(year, month+1, day)
    permit_date = permit_date.strftime("%Y-%m-%d")

    permit_date = datetime.strptime(permit_date,"%Y-%m-%d")

    res_permit_deadline = permit_date - timedelta(days = 1)
    res_permit_deadline = res_permit_deadline.strftime("%Y-%m-%d")

    # Health Check recommended day 
    health_check_date = arrivalDate + timedelta(days = 6)
    health_check_date = health_check_date.strftime("%Y-%m-%d")

    # Health Checkup suggested last day
    health_check_deadline = permit_date - timedelta(days = 7)
    health_check_deadline = health_check_deadline.strftime("%Y-%m-%d")

    # SIM Card suggested timeline
    simdate = arrivalDate + timedelta(days = 2)
    simdate = simdate.strftime("%Y-%m-%d")

    # Bank Account suggested
    bankdate = arrivalDate + timedelta(days = 3)
    bankdate = bankdate.strftime("%Y-%m-%d")

    ### Maybe attempt table / calendar output ??? 
    print(f'Your Arrival Date: {year}-{month}-{day}\n')

    print("Pre-Arrival to-dos:\n")
    
    print("Submit Health Insurance Form (3 days before arrival):\n", \
          health_insurance)

    print('\nNon-negotiable Deadlines:\n')

    print("Submit 24 hour form application by the end of the day", deadline24hr)
    print("You will need this form to apply for your residence permit\n")

    print("Health Checkup Appointment by", health_check_deadline,"\n")

    print("Last Day for Residence Permit Appointment: ", res_permit_deadline,"\n")

    print("\nSuggested Deadlines and Due-Dates:\n")

    print("Try to obtain your SIM card by", simdate)
    print("You will need a Chinese phone number to open a bank account","\n")

    print("Try to open your bank account by", bankdate)
    print("You will need a bank account to use Wechat Pay and in some instances," \
        "to use Alipay.\n")

    print("try to schedule your health appointment on", health_check_date,". \n")
    print("New appointments are added on Thursday each week")

    print("\n This is the ISS recommended timeline \n")

return_deadlines()

# push[userID, 'bankdate', bankdate]