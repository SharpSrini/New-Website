from django.urls import path
from localmedia.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'localmedia'

urlpatterns = [
    path('',index,name = 'index'),
    path('signup/',signup,name = 'signup'),
    path('qpost/',PostPost.as_view(),name = 'post'),
    path('detail/<int:pk>/',PostDetail.as_view(), name = 'detail'),
    path('detail/<int:pk>/comment/',add_comment_to_post,name = 'comment'),
    path('logout/',logout_view,name = 'logout'),
    path('detail/<int:pk>/ImagePost', ImagePost.as_view(), name = 'ImagePost'), 
    ]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
