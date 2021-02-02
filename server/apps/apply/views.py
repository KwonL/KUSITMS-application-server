import locale
from datetime import timedelta, datetime

from django.conf import settings
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, FormView, ListView, TemplateView

from .forms import ApplicationForm
from .models import ApplyForm, SNSImage, SiteConfig, ApplyConfig
from .tasks import send_new_apply_notification


class TitleView(TemplateView):
    template_name = "index.html"
    config = SiteConfig.objects.last()

    def get_generation_str(self):
        generation = str(self.config.generation)
        if generation[-1] == "1":
            return generation + "st"
        elif generation[-1] == "2":
            return generation + "nd"
        elif generation[-1] == "3":
            return generation + "rd"
        else:
            return generation + "th"

    def get_context_data(self, **kwargs):
        if self.config is None:
            return dict()
        apply_configs = list(
            ApplyConfig.objects.filter(is_active=True).values_list("id", "name")
        )
        return {
            "generation_str": self.get_generation_str(),
            "president": self.config.president,
            "vice_president": self.config.vice_president,
            "apply_types": apply_configs,
        }


def get_interview_date_list(apply_config):
    interview_date_list = list()
    day_list = list()
    locale.setlocale(locale.LC_ALL, "ko_KR.UTF-8")
    start_time = apply_config.interview_start + timedelta(hours=9)
    end_time = apply_config.interview_end + timedelta(hours=9)
    start_hour = start_time.hour
    day_delta = timedelta(days=1)
    hour_delta = timedelta(hours=1)

    while start_time <= end_time:
        day_list.append(
            start_time.strftime("%m/%d(%a) %H%p~")
            + (start_time + hour_delta).strftime("%H%p")
        )
        start_time += hour_delta
        if start_time.hour == end_time.hour:
            start_time += day_delta
            start_time = start_time.replace(hour=start_hour)
            interview_date_list.append(day_list)
            day_list = list()
    return interview_date_list


class ApplyView(LoginRequiredMixin, FormView):
    login_url = "/login/"
    form_class = ApplicationForm
    success_url = "/"
    template_name = "apply/application.html"

    def get_form(self, **kwargs):
        apply = ApplyForm.objects.filter(
            user=self.request.user,
            apply_type_id=self.request.resolver_match.kwargs.get("apply_type"),
        ).first()
        if apply:
            return self.form_class(instance=apply, **self.get_form_kwargs())
        else:
            return self.form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        apply = form.save(commit=False)
        is_new = False if apply.id else True

        if not apply.image:
            messages.error(self.request, "이미지를 업로드하세요")
            return redirect("/")
        apply.user = self.request.user
        apply.save()

        # SNS 인증
        if "sns_image" in self.request.FILES:
            for sns in self.request.FILES.getlist("sns_image"):
                image = SNSImage.objects.create(application=apply)
                image.image.save(sns.name, sns)

        if is_new and not settings.DEBUG:
            send_new_apply_notification(apply.name, apply.university, apply.apply_type)

        messages.success(self.request, "지원이 접수되었습니다!")
        return redirect("/")

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, "오류 발생. 오류가 지속되면 학회장에게 문의하세요.")
        return redirect("/")

    def get_context_data(self, **kwargs):
        apply = ApplyForm.objects.filter(
            user=self.request.user,
            apply_type_id=self.request.resolver_match.kwargs.get("apply_type"),
        ).first()
        apply_config = ApplyConfig.objects.get(
            id=self.request.resolver_match.kwargs.get("apply_type")
        )
        interview_date_list = get_interview_date_list(apply_config)

        return {
            "object": apply,
            "apply_config": apply_config,
            "interview_date_list": interview_date_list,
            "interview_list_len_1": len(interview_date_list),
            "interview_list_len_2": len(interview_date_list[0]),
        }


@method_decorator(name="get", decorator=staff_member_required(login_url="/login/"))
class ApplyListView(ListView):
    queryset = ApplyForm.objects.all()
    ordering = ["name"]
    template_name = "apply/list.html"


@method_decorator(name="get", decorator=staff_member_required(login_url="/login/"))
class ApplyDetailView(DetailView):
    model = ApplyForm

    def get_template_names(self):
        return "apply/application.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        interview_date_list = get_interview_date_list(self.object.apply_type)
        context.update(
            {
                "scoring": True,
                "apply_config": self.object.apply_type,
                "interview_date_list": interview_date_list,
                "interview_list_len_1": len(interview_date_list),
                "interview_list_len_2": len(interview_date_list[0]),
            }
        )
        return context
