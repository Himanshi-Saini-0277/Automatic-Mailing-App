import pandas as pd
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

GMAIL_ID = '  '  # Your Gmail email address
GMAIL_PSWD = '  '  # Your Gmail password or app password

def send_email(to, sub, msg):
    print(f"Email to {to} sent with Subject: {sub} and message {msg}")
    
    # Set up email content
    email = MIMEMultipart()
    email['From'] = GMAIL_ID
    email['To'] = to
    email['Subject'] = sub
    email.attach(MIMEText(msg, 'plain'))
    
    # Connect to SMTP server and send email
    with smtplib.SMTP('smtp.gmail.com', 587) as s:
        s.starttls()
        s.login(GMAIL_ID, GMAIL_PSWD)
        s.sendmail(GMAIL_ID, to, email.as_string())

if __name__ == "__main__":
    # Read data from Excel file
    df = pd.read_excel("data.xlsx")
    
    today = datetime.datetime.now().strftime("%d-%m")
    year_now = datetime.datetime.now().strftime("%Y")
    
    # List to store indices of records to update
    write_ind = []
    
    # Iterate over rows in DataFrame
    for index, row in df.iterrows():
        bday = row['Birthday'].strftime("%d-%m")
        
        # Check if today is the birthday and it's not recorded for this year
        if today == bday and year_now not in str(row['Year']):
            send_email(row['Email'], "Happy Birthday", row['Dialogue'])
            write_ind.append(index)
    
    # Update 'Year' column for records where birthday email was sent
    for i in write_ind:
        df.at[i, 'Year'] = f"{df.at[i, 'Year']}, {year_now}"
                
    # Write updated DataFrame back to Excel file
    df.to_excel('data.xlsx', index=False)
