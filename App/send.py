from typing import Optional, Any
from pydantic import BaseModel

from email.mime.multipart import MIMEMultipart, MIMEBase
from email.mime.text import MIMEText

import pybase64

from gmail_api.Google import create_service
from config import settings

# ˋsend email
def send_message(to: str, subject: str, message: str):
    service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    
    emailMsg = message
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = to
    mimeMessage['subject'] = subject
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes().decode('utf-8'))
    
    message = service.users().messages().send(userId="me", body={"raw": raw_string}).execute()
    print(message)
