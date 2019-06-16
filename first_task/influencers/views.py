
from django.http import HttpResponse
from django.template import loader
from .models import Data
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

def get_data(request):
    with open ('/home/himanshu/Desktop/Database/data.json', 'r') as f:
        a = json.load(f)
    for data in a:
        x = data['data']['allInfluencers']

        for i in x:
            try:
                username = i['username']
                fcount = i['stats']['followerCount']
                avgLike = i['stats']['engagement']['avgLikesRatio']
                avgComment = i['stats']['engagement']['avgCommentsRatio']
                picture = i['picture']
                d = Data(username=username, followerCount=fcount, avgLikesRatio=avgLike, avgCommentsRatio=avgComment,
                         picture=picture)
                d.save()

            except:
                pass



def index(request):
    #if Data.objects.all().count()<298:
     #   with open('/home/himanshu/Desktop/Database/data.json', 'r') as f:
      #      a = json.load(f)
       # for data in a:
       #     x = data['data']['allInfluencers']

        #    for i in x:
         #       try:
          #          username = i['username']
           #         fcount = i['stats']['followerCount']
            #        avgLike = i['stats']['engagement']['avgLikesRatio']
             #       avgComment = i['stats']['engagement']['avgCommentsRatio']
              #      picture = i['picture']

               #     d = Data(username=username, followerCount=fcount, avgLikesRatio=avgLike, avgCommentsRatio=avgComment,
                #         picture=picture)
                 #   d.save()

    #            except:
     #               pass

    all_data = Data.objects.all()
    template = loader.get_template('influencers/index.html')
    page = request.GET.get('page')

    paginator = Paginator(all_data, 20)
    try:
       users = paginator.get_page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
        'all_data': users,
    }
    return HttpResponse(template.render(context, request))



# Create your views here.