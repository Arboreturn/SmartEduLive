from django.urls import path
from . import views
from pages.views import AboutView,İndexView,ContactView
urlpatterns = [
    path('', İndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),
     path('contact/', ContactView.as_view(), name="contact"),
    #path(route, view, opt(kısayol ismi))
]
