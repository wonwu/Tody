from django.urls import path
from .views import views_outer, views_pants, views_top, views_onepiece, views_base, views_keyword, views_skirt
from django.conf.urls.static import static
from django.conf import settings

app_name = 'closet'

urlpatterns = [    
    
    # 유저 옷장 보여주기
    path('<int:author_id>/', 
    views_base.author_closet, name='author_closet'),    

    path('<int:author_user>/<int:closet_id>/', 
    views_top.detail, name ='detail'),

    path('<int:author_user>/<int:closet_id>/', 
    views_pants.detail, name ='detail'),

    path('<int:author_user>/<int:closet_id>/', 
    views_outer.detail, name ='detail'),

    path('<int:author_user>/<int:closet_id>/', 
    views_onepiece.detail, name ='detail'),

    
    # 상의 등록
    path('closet/top_create/<int:author_user>/', 
    views_top.closet_create, name='top_create'),    

    # 하의 등록
    path('closet/pants_create/<int:author_user>/', 
    views_pants.closet_create, name='pants_create'),

    # 아우터 등록
    path('closet/outer_create/<int:author_user>/', 
    views_outer.closet_create, name='outer_create'),
    
    # 원피스 등록
    path('closet/onepiece_create/<int:author_user>/', 
    views_onepiece.closet_create, name='onepiece_create'),

    # 스커트 등록
    path('closet/skirt_create/<int:author_user>/', 
    views_skirt.closet_create, name='skirt_create'),

    path('keyword/keyword', views_keyword.keyword_index, name="keyword")

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)