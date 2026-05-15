from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # تطبيقاتك
   # path('books/', include("apps.bookmodule.urls")),
    path('users/', include("apps.usermodule.urls")),
    path('bookmodule/', include("apps.bookmodule.urls")),

]

# ⭐ مهم جداً لعرض الصور (LAB 11 Task 3)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
