from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from apps.account import views as account_views
from apps.apply import views as apply_views


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", apply_views.TitleView.as_view()),
    # Login
    path("login/", account_views.LoginView.as_view()),
    path("signup/", account_views.SignupView.as_view()),
    path("account/", include("django.contrib.auth.urls")),
    # apply
    path("apply/<int:apply_type>/", apply_views.ApplyView.as_view()),
    # scoring
    path("internal/list/", apply_views.ApplyListView.as_view()),
    path("internal/list/<int:pk>/", apply_views.ApplyDetailView.as_view()),
    path('sentry-debug/', trigger_error),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
