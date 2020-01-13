import os
from datetime import datetime

from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string


def get_image_name(instance, filename):
    _, extension = os.path.splitext(filename)
    date = datetime.strftime(timezone.now(), '%Y%m%d')
    random = "{}{}".format(
        date,
        get_random_string(
            length=6,
            allowed_chars=str(
                'abcdefghijklmnopqrstuvwxyz'
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            )
        )
    )
    new_filename = '{random}{extension}'.format(
        random=random,
        extension=extension
    )

    return 'profile/{}'.format(
        new_filename
    )


class ApplyForm(models.Model):
    image = models.ImageField(
        upload_to=get_image_name, null=False, blank=False,
        default=''
    )
    user = models.ForeignKey(
        'account.User', on_delete=models.SET_NULL, related_name='applications',
        null=True, blank=False
    )
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    birth = models.DateField()
    phone = models.CharField(max_length=30)
    gender = models.CharField(max_length=2)
    insta = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    answer_1 = models.TextField()
    answer_2 = models.TextField()
    answer_3 = models.TextField()
    answer_4 = models.TextField()
    answer_5 = models.TextField()
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
