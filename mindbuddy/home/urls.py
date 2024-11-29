from django.contrib import admin
from django.urls import include ,path
from home  import views

urlpatterns = [
    #path('admin /', admin.site.urls),
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("login",views.login,name='login'),
    path("form",views.form,name='Questioner'),
]


