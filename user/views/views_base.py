from django.shortcuts import render
from ..models import Closet
from django.contrib.auth.decorators import login_required


# 유저별 옷장 목록
@login_required(login_url='login:login')
def author_closet(request, author_id):
        
    closet_list = Closet.objects.filter(author=author_id).order_by('closet_create_date') # 날짜

    context = {'closet_list': closet_list}    
    return render(request, 'closet_list.html', context)    