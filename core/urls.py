
from django.contrib import admin
from django.urls import path
from mainApp.views import  *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('fanlar/', fan_view),

]
