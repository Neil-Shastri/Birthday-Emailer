#add yourself to the list using the form below
#https://forms.gle/Nd6BFVNkdocydWek8

import smtplib #smtplib for emailing
import gspread #gspread for connecting to Google Sheets
from datetime import datetime #get current date to check for bdays



#connect to Cloud Console service account and access form 
service_account = gspread.service_account()
sheet = service_account.open("Birthday-Emailer by Neil Shastri (Responses)") #opens the specific form where the peoples birthdays are found
worksheet = sheet.worksheet("Form Responses 1") #connects to exact worksheet in the spreadsheet file

#convert the form data to a list
data = worksheet.get_all_values()


#get the current date in string format and year in int format
now = datetime.now()
current_date = now.date()
cur_year = int(current_date.strftime('%Y'))
cur_date = current_date.strftime('%-m/%-d')



#collect info if it IS their bday
people = []
emails = []
ages = []

for person in data:
    if cur_date in (person[3][:-4]):
        people.append(person[2].upper())
        emails.append(person[1])
        birth_year = int(person[3][-4:])
        age = cur_year - birth_year
        ages.append(age)


sender = "bdaywishesfromneil@gmail.com"

smtp_server = "smtp.gmail.com"
app_pass = "okmm selo vugq ihro"
smtp_port = 587

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls() 
        server.login(sender,app_pass)
        
        for i in range(len(people)):
            receiver = emails[i]
            subject = f"HAPPY BIRTHDAY, {people[i]}!"
            message = f"AYYO {people[i]}! \n\nYOU'RE {ages[i]} YEARS OLD... HAVE A BLAST!\n\nBest Wishes,\nNeil Shastri\n\nThis is part of my Birthday-Emailer project. You can check out the code at the link below.\n(https://github.com/Neil-Shastri/Birthday-Emailer)"
            full_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(sender, receiver, full_message)


        server.quit()

except Exception as e:
    
    print("Error: ", e)
    
    

