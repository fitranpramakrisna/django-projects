from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from sharing import views
from django.conf.urls.static import static

from django.conf import settings

def index(request):
    return HttpResponse("<h1>Hello World!</h1>")



urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('home/', index)
    path('upload/', views.upload),
    path('<uuid:uid>/', views.download),
    path('', views.index)
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


