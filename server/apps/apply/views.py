from django.conf import settings
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, FormView, ListView

from .forms import ApplicationForm
from .models import ApplyForm, SNSImage
from .tasks import send_new_apply_notification


class ApplyView(LoginRequiredMixin, FormView):
    login_url = "/login/"
    form_class = ApplicationForm
    success_url = "/"

    def get_form(self):
        try:
            apply = ApplyForm.objects.get(user=self.request.user)
            return self.form_class(instance=apply, **self.get_form_kwargs())
        except ApplyForm.DoesNotExist:
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
            send_new_apply_notification(
                apply.name, apply.university, apply.apply_type
            )

        messages.success(self.request, "지원이 접수되었습니다!")
        return redirect("/")

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, "오류 발생. 오류가 지속되면 학회장에게 문의하세요.")
        return redirect("/")

    def get_context_data(self, **kwargs):
        res = {"form": ApplicationForm()}
        apply = ApplyForm.objects.filter(user=self.request.user).first()
        res = {"object": apply} if apply else {}

        if self.request.GET.get("application_type"):
            res.update(
                {
                    "application_type": getattr(
                        ApplyForm,
                        self.request.GET.get("application_type").upper(),
                    )
                }
            )
        return res

    def get_template_names(self):
        app_type = self.request.GET.get("application_type")

        if app_type:
            return f"apply/{app_type}.html"
        return "apply/member.html"


@method_decorator(
    name="get", decorator=staff_member_required(login_url="/login/")
)
class ApplyListView(ListView):
    model = ApplyForm
    ordering = ["name"]
    template_name = "apply/list.html"


@method_decorator(
    name="get", decorator=staff_member_required(login_url="/login/")
)
class ApplyDetailView(DetailView):
    model = ApplyForm

    def get_template_names(self):
        obj = self.object
        return "apply/{}".format(
            {
                ApplyForm.MANAGEMENT: "management.html",
                ApplyForm.EDUCATION_PLANNING: "education_planning.html",
                ApplyForm.PUBLIC_RELATION: "public_relation.html",
                ApplyForm.MEMBER: "member.html",
            }.get(obj.apply_type)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"application_type": "채점지", "scoring": True})
        return context
