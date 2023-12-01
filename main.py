import smtplib                                                                                      # this is the library that allows us to send emails
import ssl                                                                                          # this is the library that allows us to use SSL
import os                                                                                           # this is the library that allows us to use environment variables
import mysql.connector                                                                              # this is the library that allows us to connect to the database
from generate import generate_email                                                                 # this is the function that generates the email content
from email.mime.text import MIMEText as email_message                                               # this is the class that allows us to create an email message
from email.mime.multipart import MIMEMultipart as multipart                                         # this is the class that allows us to create an email message
from email.mime.image import MIMEImage as mail_image                                                # this is the class that allows us to attach images to the email
from email.mime.base import MIMEBase as base                                                        # this is the class that allows us to attach files to the email
from email import encoders                                                                          # this is the library that allows us to encode the files
from dotenv import load_dotenv                                                                      # this is the library that allows us to use environment variables

load_dotenv()                                                                                       # this loads the environment variables from the .env file
mail_address = os.getenv("MAIL_ADDRESS")                                                            # this gets the email address from the environment variables
mail_password = os.getenv("MAIL_PASSWORD")                                                          # this gets the email password from the environment variables
db_host = os.getenv("DB_HOST")                                                                      # this gets the database host from the environment variables
db_user = os.getenv("DB_USER")                                                                      # this gets the database user from the environment variables
db_password = os.getenv("DB_PASSWORD")                                                              # this gets the database password from the environment variables
db_name = os.getenv("DB_NAME")                                                                      # this gets the database name from the environment variables

SQL_connection = mysql.connector.connect(                                                           # this is the connection to the database
    host = db_host,                                                                                 # this is the host of the database
    user = db_user,                                                                                 # this is the user of the database
    password = db_password,                                                                         # this is the password of the database
    database = db_name                                                                              # this is the name of the database
)

query = "SELECT email FROM subscribers"                                                             # this is the query that gets the emails from the database
cursor = SQL_connection.cursor()                                                                    # this is the cursor that executes the query
cursor.execute(query)                                                                               # this executes the query
subscriber_emails = [row[0] for row in cursor.fetchall()]                                           # this gets the emails from the query and puts them in a list


subject, html_content, plain_content = generate_email()                                             # this gets the subject, html content and plain content


html = email_message(html_content, "html")
plain = email_message(plain_content, "plain")
email = multipart("alternative")                                                                    # this creates the email message and sets it as multipart
email["Subject"] = subject                                                                          # this sets the subject of the email
email["From"] = mail_address                                                                        # this sets the sender of the email
email.attach(plain)                                                                                 # this sets the plain content of the email
email.attach(html)                                                                                  # this sets the html content of the email

image_existence = os.stat('image_names.txt').st_size != 0                                           # this checks if the image_names.txt file is empty
file_existence = os.stat('file_names.txt').st_size != 0                                             # this checks if the pdf_names.txt file is empty

if image_existence == True:
    with open ("image_names.txt", 'r') as attachements:                                             # this opens the image_names.txt file
        image_names = attachements.read().splitlines()                                              # this reads the image_names.txt file and puts the names in a list
        for image_name in image_names:                                                              # this loops through the image names  
            with open(image_name, 'rb') as f:                                                       # this opens the image
                image_data = f.read()                                                               # this reads the image
        
            image = mail_image(image_data, os.path.basename(image_name))                            # this creates the image object
            image.add_header('Content-Disposition', 'attachment', filename = image_name)            # this sets the image name
            email.attach(image)                                                                     # this attaches the image to the email

if file_existence == True:                                                                          # this checks if the file_names.txt file is empty
    with open ('file_names.txt', 'r') as p:                                                         # this opens the file_names.txt file
        file_names = p.read().splitlines()                                                          # this reads the file_names.txt file and puts the names in a list
        for file_name in file_names:                                                                # this loops through the file names
            with open (file_name, 'rb') as f:                                                       # this opens the file
                pdf = base("application", "ocet-stream")                                            # this creates the file object
                pdf.set_payload(f.read())                                                           # this reads the file
                encoders.encode_base64(pdf)                                                         # this encodes the file
                pdf.add_header('Content-Disposition', 'attachment', filename = file_name)           # this sets the file name
                email.attach(pdf)                                                                   # this attaches the file to the email

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as smtp_server:  # this creates the smtp server
    smtp_server.login(mail_address, mail_password)                                                  # this logs in to the smtp server
    for subscriber_email in subscriber_emails:                                                      # this loops through the subscriber emails
        
        email["To"] = subscriber_email                                                              # this sets the recipient of the email 
        smtp_server.send_message(email)                                                             # this sends the email

cursor.close()                                                                                      # this closes the cursor
SQL_connection.close()                                                                              # this closes the connection to the database