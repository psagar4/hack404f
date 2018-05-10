
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^auth/$',  views.login_form, name='login_form'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)