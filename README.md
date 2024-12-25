# Birthday Emailer

This is a Python project that automatically sends personalized birthday emails to people based on the information submitted through a Google Forms survey (https://forms.gle/VqQTUJZtyxqurMEZ9). The script checks the current date, matches it with the birthday data from the form, and sends an email to those celebrating their birthday on that day.

The script is meant to run automatically via **crontab** for background scheduling, but I have disabled it for now. You can still manually run the script as needed.

## Features

- **Google Sheets Integration**: The script connects to a Google Sheet where responses to a Google Form are stored. It retrieves names, email addresses, and birthdates of participants.
- **Birthday Check**: The script compares today's date with the birthdates of the people listed in the form.
- **Email Sending**: If it’s someone's birthday today, the script sends a personalized email wishing them a happy birthday.
- **Customizable**: You can easily adapt this for different purposes, such as automated birthday wishes for teams or communities.
