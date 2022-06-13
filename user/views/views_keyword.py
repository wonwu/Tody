from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Musinsa_Closet, codi
#from recommendation.recommendation import recommendation as recommand
#from recommendation.import_data import Database

#db = Database('db.sqlite3')
#def url_maker(codi_type, codi_id):
#    type_url = {
#    'm01': 'https://store.musinsa.com/app/codimap/views/',
#    'm02': 'https://www.musinsa.com/app/styles/views/'
#    }
#    return type_url[codi_type] + str(codi_id)



@login_required(login_url='login:login')

def keyword_index(request):
    request.post('')
    #recommand()
    return render(request, 'keword.html',)

#
#ata = Musinsa_Closet.objects.first()
#print(data)
