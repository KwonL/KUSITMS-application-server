from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from apps.account import views as account_views
from apps.apply import views as apply_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="index.html")),
    # Login
    path("login/", account_views.LoginView.as_view()),
    path("signup/", account_views.SignupView.as_view()),
    path("account/", include("django.contrib.auth.urls")),
    # apply
    path("apply/", apply_views.ApplyView.as_view()),
    # scoring
    path("list/", apply_views.ApplyListView.as_view()),
    path("staff_list/", apply_views.StaffApplyListView.as_view()),
    path("list/<int:pk>/", apply_views.ApplyDetailView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
