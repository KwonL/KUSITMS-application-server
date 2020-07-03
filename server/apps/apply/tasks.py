from django.core.mail import send_mail
from huey.contrib.djhuey import task
from django.conf import settings


@task()
def send_new_apply_notification(name, university, team):
    send_mail(
        f"새로운 지원자 등록: {team} - {university} - {name}",
        "제곧내",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=["dlrnjsgud322@gmail.com"],
    )
