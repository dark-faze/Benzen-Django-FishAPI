from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.getData),
    path('addRecord/', views.postData),
    path('getAllRecords/', views.getDataSeq),
    path('getRecord/', views.getReq)

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#addRecord is for adding a fish record
