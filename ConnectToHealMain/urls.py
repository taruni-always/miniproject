from django.urls import path
from . import views
from django.views.i18n import JavaScriptCatalog
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('jsi18n',JavaScriptCatalog.as_view(),name="js-catalog"),
    path('', views.home,name = "ConnectToHeal-home"),
    path('home/', views.home,name = "ConnectToHeal-home"),
    path('contact/', views.contact,name = "ConnectToHeal-contact"),
    path('viewBlogs/', views.viewBlogs,name = "ConnectToHeal-viewBlogs"),
    path('ventingSpace/', views.ventingSpace,name = "ConnectToHeal-ventingSpace"),
    path('viewTherapists/', views.viewTherapists,name = "ConnectToHeal-viewTherapists"),
    path('detailAppointment/',views.detailAppointment,name = "ConnectToHeal-detailAppointment"),
    path('myAppointments/', views.myAppointments,name = "ConnectToHeal-myAppointments"),
    path('approveSessions/', views.approveSessions,name = "ConnectToHeal-approveSessions"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
