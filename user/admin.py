from django.contrib import admin
from .models import Closet, Musinsa_Closet

# Register your models here.

# Question모델 관리/ 검색기능
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['closet_title']
    
admin.site.register(Closet, QuestionAdmin)
admin.site.register(Musinsa_Closet, QuestionAdmin)
# admin.site.register(Closet_top, QuestionAdmin)
# admin.site.register(Closet_outer, QuestionAdmin)
# admin.site.register(Closet_pants, QuestionAdmin)
