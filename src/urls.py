
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from django.conf import settings 
from django.conf.urls.static import static
from dashboard import views

admin.site.site_header  =  "Seeable Tarlac Admin"  
admin.site.site_title  =  "Seeable Tarlac"
admin.site.index_title  =  "Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('sign-up/', views.CreateAuthor.as_view(), name='create_user'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', include("django.contrib.auth.urls")), # <-- added
    # app url configs
    path('',include('blog.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
