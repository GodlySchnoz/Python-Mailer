def generate_email():                               # DO NOT under any circumstances change the name of this function, it's used in main.py
    subject = "Add email subject here"              # this is the subject of the email, modify it as needed    
    html_content = f"""
        <html>
        <head></head>
        <body>
            <p>html content here</b></p>
        </body>
        </html>
    """                                             # can be modified as needed, to include images, files etc, must be added in the attachments via main.py

    plain_content = "Add email content here"        # this is the plain text version of the email, it's the same as the html content but without the html tags,
    
    return subject, html_content, plain_content     # this function returns the subject, html content and plain content of the email, DO NOT CHANGE THE RETURN STATEMENT