from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from .views import IndexView, RegisterView, FindReferenceView, ReferenceListView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^reference/$', FindReferenceView.as_view(), name='reference'),
    url(r'^view/$', ReferenceListView.as_view(), name='view_reference'),
    url(r'^subjects/$', views.LoadSubjects, name='ajax_load_subjects'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)