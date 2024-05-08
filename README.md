# Automatic Mailing App
 
## Introduction

The Birthday Reminder and Email Automation Script is a Python program designed to automate the process of sending birthday emails to contacts listed in an Excel file. It utilizes the pandas library for data manipulation, datetime for date and time operations, and smtplib along with the email.mime module for sending emails via Gmail's SMTP server.

## Features

- Read Data from Excel File: The script reads contact information including birthdays and email addresses from an Excel file.
- Send Birthday Emails: It checks if any contact has a birthday today and sends a personalized birthday email to their respective email addresses.
- Update Records: After sending birthday emails, the script updates the records by appending the current year to the 'Year' column to indicate that an email has been sent for the current year.

## Requirements

- Python: Ensure that Python is installed on your system.
- pandas: Install pandas library using pip install pandas.
- Excel File: Prepare an Excel file ('data.xlsx') with columns for 'Name', 'Email', 'Birthday', 'Dialogue', and 'Year'.

## Usage

#### Setup Gmail Credentials:
Replace the placeholders GMAIL_ID and GMAIL_PSWD with your Gmail email address and password or app password respectively.

#### Prepare Excel File:
Create an Excel file named 'data.xlsx' with columns 'Name', 'Email', 'Birthday' (date format), 'Dialogue', and 'Year'.

#### Customize Email Content:
Modify the email subject and message content in the send_email() function to personalize the birthday emails.

#### Run the Script:
Execute the script by running it with Python (python script_name.py). Ensure that the Excel file is in the same directory as the script.

## Behavior

- The script sends birthday emails to contacts whose birthday matches the current date and hasn't been recorded for the current year.
- It updates the 'Year' column in the Excel file to indicate that an email has been sent for the current year.

## Note

- Make sure to enable less secure apps access or use app passwords if you're using Gmail for sending emails.
- Ensure that the Excel file is correctly formatted with the specified column names and date format for the 'Birthday' column.

## Conclusion

The Birthday Reminder and Email Automation Script simplifies the process of sending personalized birthday emails to contacts listed in an Excel file. By automating this task, it saves time and ensures that birthday greetings are sent promptly to friends, family, or colleagues.
