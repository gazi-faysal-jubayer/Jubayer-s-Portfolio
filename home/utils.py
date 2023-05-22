from django.core.mail  import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail  import send_mail


def sendMessage(name,email,subject,message):
    try:
        template = render_to_string('selection_mail.html', {'name':name,
                                                            'email': email,
                                                            'message': message,
                                                            })
        mail = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['gazi.faysal.jubayer@gmail.com','halimahalima4628@gmail.com'],
        )
        mail.fail_silently=False
        mail.send()
    except Exception as e:
        return False
    return True
