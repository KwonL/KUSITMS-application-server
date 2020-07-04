import os
import uuid

from django.db import models


def get_image_name(instance, filename):
    _, extension = os.path.splitext(filename)
    return f"profile/{uuid.uuid4()}{extension}"


def get_sns_image_name(instance, filename):
    _, extension = os.path.splitext(filename)
    return f"sns/{uuid.uuid4()}{extension}"


class ApplyForm(models.Model):
    MANAGEMENT, PUBLIC_RELATION, EDUCATION_PLANNING, MEMBER = (
        "경영총괄팀",
        "대외홍보팀",
        "교육기획팀",
        "학회원",
    )
    APPLY_TYPE_CHOICES = [
        (MANAGEMENT, "management"),
        (PUBLIC_RELATION, "public relation"),
        (EDUCATION_PLANNING, "education planning"),
        (MEMBER, "member"),
    ]

    apply_type = models.CharField(
        max_length=255, choices=APPLY_TYPE_CHOICES, default=MEMBER, blank=True
    )
    image = models.ImageField(upload_to=get_image_name)
    user = models.ForeignKey(
        "account.User",
        on_delete=models.SET_NULL,
        related_name="applications",
        null=True,
        blank=False,
    )
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=20)
    birth = models.DateField()
    phone = models.CharField(max_length=30)
    gender = models.CharField(max_length=2)
    insta = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    answer_1 = models.TextField(default="")
    answer_2 = models.TextField(default="")
    answer_3 = models.TextField(default="")
    answer_4 = models.TextField(default="")
    answer_5 = models.TextField(default="")
    answer_6 = models.TextField(default="")
    activity_1 = models.CharField(max_length=255, blank=True)
    activity_2 = models.CharField(max_length=255, blank=True)
    activity_3 = models.CharField(max_length=255, blank=True)
    activity_4 = models.CharField(max_length=255, blank=True)
    activity_5 = models.CharField(max_length=255, blank=True)
    date_1_1 = models.BooleanField(default=False)
    date_1_2 = models.BooleanField(default=False)
    date_1_3 = models.BooleanField(default=False)
    date_1_4 = models.BooleanField(default=False)
    date_1_5 = models.BooleanField(default=False)
    date_1_6 = models.BooleanField(default=False)
    date_1_7 = models.BooleanField(default=False)
    date_2_1 = models.BooleanField(default=False)
    date_2_2 = models.BooleanField(default=False)
    date_2_3 = models.BooleanField(default=False)
    date_2_4 = models.BooleanField(default=False)
    date_2_5 = models.BooleanField(default=False)
    date_2_6 = models.BooleanField(default=False)
    date_2_7 = models.BooleanField(default=False)
    date_3_1 = models.BooleanField(default=False)
    date_3_2 = models.BooleanField(default=False)
    date_3_3 = models.BooleanField(default=False)
    date_3_4 = models.BooleanField(default=False)
    date_3_5 = models.BooleanField(default=False)
    date_3_6 = models.BooleanField(default=False)
    date_3_7 = models.BooleanField(default=False)
    date_4_1 = models.BooleanField(default=False)
    date_4_2 = models.BooleanField(default=False)
    date_4_3 = models.BooleanField(default=False)
    date_4_4 = models.BooleanField(default=False)
    date_4_5 = models.BooleanField(default=False)
    date_4_6 = models.BooleanField(default=False)
    date_4_7 = models.BooleanField(default=False)
    mt_avail = models.CharField(max_length=10)
    ot_avail = models.CharField(max_length=10)


class SNSImage(models.Model):
    application = models.ForeignKey(
        ApplyForm,
        on_delete=models.CASCADE,
        related_name="sns_images",
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to=get_sns_image_name, null=False, blank=False, default=""
    )
