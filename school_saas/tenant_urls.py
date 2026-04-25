from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
    path('', include('school.urls')),
    path('', include('home_auth.urls')),
    #path('finance/', include('finance.urls')),
    #path('exam/', include('exams.urls')),
   

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
