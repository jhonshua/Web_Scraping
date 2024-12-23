from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from schemas.user.user_schemas import EmailSchema,  New_userSchema
from templates.email_templates.new_account import template_new_account
from templates.email_templates.rest_password import template_reset
from dotenv import load_dotenv
import os

load_dotenv()

# Cargar variables de entorno
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
EMAILS_FROM_EMAIL = os.getenv('EMAILS_FROM_EMAIL')
SMTP_PORT = os.getenv('SMTP_PORT')
SMTPL_HOST = os.getenv('SMTPL_HOST')
MAIL_USER_STARTTLS = os.getenv('MAIL_USER_STARTTLS')
USE_CREDENTIAL = os.getenv('USE_CREDENTIALS')
SMTP_SSL_TLS = os.getenv('SMTP_SSL_TLS')

# Configuración del servidor SMTP
conf = ConnectionConfig(
    MAIL_USERNAME=SMTP_USER,
    MAIL_PASSWORD=SMTP_PASSWORD,
    MAIL_FROM=EMAILS_FROM_EMAIL,
    MAIL_PORT=SMTP_PORT,
    MAIL_SERVER=SMTPL_HOST,
    USE_CREDENTIALS=MAIL_USER_STARTTLS,
    MAIL_STARTTLS=USE_CREDENTIAL,
    MAIL_SSL_TLS=SMTP_SSL_TLS,
)

async def send_email(data: New_userSchema):
    
    try:
        if data.template == "new_user":
            html = template_new_account (data.email, data.password, data.name)
        else:
          
           html = template_reset (data.password, data.name)
        message = MessageSchema(
            subject="Fastapi-Mail module",
            recipients=[data.email],
            body=html,
            subtype=MessageType.html,
        )

        fm = FastMail(conf)
        await fm.send_message(message)
        return "Email sent successfully"

    except Exception as e:
        # Manejar errores de forma informativa
        print(f"Error sending email: {str(e)}")
        return "Error sending email. Please try again later."

