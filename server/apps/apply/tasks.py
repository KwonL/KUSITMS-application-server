from traceback import print_exc

from django.conf import settings
from django.core.mail import send_mail
from huey.contrib.djhuey import task

from apps.apply.models import MailList


@task(retries=2, retry_delay=60)
def send_new_apply_notification(name, university, team, content):
    mail_list = list(MailList.objects.all().values_list("email", flat=True))
    try:
        send_mail(
            f"새로운 지원자 등록: {team} - {university} - {name}",
            "",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=mail_list,
            html_message=content,
        )
    except Exception:
        print_exc()
