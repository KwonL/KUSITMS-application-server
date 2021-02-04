import os
import uuid

from django.db import models

from utils.const import NOTICE_DEFAULT_STRING, QUESTION_5_DEFAULT, QUESTION_6_DEFAULT


def get_image_name(instance, filename):
    _, extension = os.path.splitext(filename)
    return f"profile/{uuid.uuid4()}{extension}"


def get_sns_image_name(instance, filename):
    _, extension = os.path.splitext(filename)
    return f"sns/{uuid.uuid4()}{extension}"


def get_main_image_name(instance, filename):
    _, extension = os.path.splitext(filename)
    return f"title/{uuid.uuid4()}{extension}"


def get_main_slide_name(instance, filename):
    _, extension = os.path.splitext(filename)
    return f"main-slide/{uuid.uuid4()}{extension}"


class SiteConfig(models.Model):
    generation = models.IntegerField("기수", default=0)
    main_image = models.ImageField(
        upload_to=get_main_image_name, null=False, blank=False, default=""
    )
    president = models.CharField("학회장 이름 (전화번호)", max_length=100, default="")
    vice_president = models.CharField("부학회장 이름 (전화번호)", max_length=100, default="")
    start = models.DateTimeField("지원 시작일")
    end = models.DateTimeField("지원 종료일")
    ot_date = models.DateField("OT 날짜")
    mt_date = models.DateField("MT 날짜")
    is_active = models.BooleanField("활성화 여부", default=True)
    recruitment_summary = models.URLField("모집 요강 URL", default="", blank=True)

    class Meta:
        db_table = "site_config"
        verbose_name = "사이트 설정(기수, 지원일 등)"
        verbose_name_plural = "사이트 설정(기수, 지원일 등)"


class MainSlideImage(models.Model):
    site_config = models.ForeignKey(
        SiteConfig,
        on_delete=models.SET_NULL,
        related_name="main_slides",
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to=get_main_slide_name, null=False, blank=False, default=""
    )


class ApplyConfig(models.Model):
    name = models.CharField("지원서 타입(학회원, 경총, 대홍..)", max_length=255, default="21기 학회원")
    is_active = models.BooleanField("활성화 여부", default=True)
    notice = models.TextField("유의사항", default=NOTICE_DEFAULT_STRING, blank=True)
    question_1 = models.TextField("질문 1", default="1번 질문")
    question_2 = models.TextField("질문 2", default="2번 질문")
    question_3 = models.TextField("질문 3", default="3번 질문")
    question_4 = models.TextField("질문 4", default="4번 질문")
    question_5 = models.TextField("질문 5(활동 내역)", default=QUESTION_5_DEFAULT)
    question_6 = models.TextField("질문 6(자유롭게 하고싶은 말)", default=QUESTION_6_DEFAULT)
    interview_start = models.DateTimeField("면접 시작일과 시간(한시간 단위로 설정됨)")
    interview_end = models.DateTimeField("면접 종료일과 시간(한시간 단위로 설정됨)")

    class Meta:
        db_table = "apply_config"
        verbose_name = "지원서 개별 설정"
        verbose_name_plural = "지원서 개별 설정"


class ApplyForm(models.Model):
    apply_type = models.ForeignKey(
        ApplyConfig, on_delete=models.SET_NULL, related_name="applications", null=True
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
    interview_date = models.TextField(default="", blank=True)

    class Meta:
        verbose_name = "지원서"
        verbose_name_plural = "지원서"


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


class MailList(models.Model):
    name = models.CharField("이름", max_length=255, blank=True, default="")
    email = models.EmailField("이메일")

    class Meta:
        verbose_name = "이메일 리스트"
        verbose_name_plural = "이메일 리스트"
