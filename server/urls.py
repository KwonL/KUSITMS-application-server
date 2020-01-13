from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from apps.account.views import LoginView, SignupView
from apps.apply.views import ApplyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('login/', LoginView.as_view()),
    path('signup/', SignupView.as_view()),
    path('apply/', ApplyView.as_view()),
    path('account/', include('django.contrib.auth.urls')),
]
