from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from apps.account.views import LoginView, SignupView
from apps.apply.views import ApplyView, ApplyListView, ApplyDetailView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('login/', LoginView.as_view()),
    path('signup/', SignupView.as_view()),
    # path('apply/', ApplyView.as_view()),
    path('account/', include('django.contrib.auth.urls')),
    path('list/', ApplyListView.as_view()),
    path('list/<int:pk>/', ApplyDetailView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
