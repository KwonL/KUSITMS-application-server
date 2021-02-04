import os
from traceback import print_exc

from django.conf import settings
from django.core.mail import send_mail
from huey.contrib.djhuey import task


@task(retries=2, retry_delay=60)
def send_new_apply_notification(name, university, team, content):
    try:
        send_mail(
            f"새로운 지원자 등록: {team} - {university} - {name}",
            "",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=os.getenv("NOTIFICATION_MAIL_TARGETS").split(","),
            html_message=content,
        )
    except Exception:
        print_exc()
