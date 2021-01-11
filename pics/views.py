from django.shortcuts import render
from django.http  import HttpResponse,HttpResponseRedirect,Http404
from .models import Pic
# Create your views here.
# function to display the home page

def home(request):
    home = Pic.objects.all()
    return render(request,'displays/allpics.html',{'home':home})

# function to display the location page
def location(request,location):
    pics = Pic.filter_by_location()
    return render(request,'displays/location.html',{"pics":pics})

# function to display a selected pic
# def pic(request,id):
    
#     pics = Pic.objects.get(id=id)
#     # try:
#     #     pics = Pic.objects.get(id=id)
#     # except DoesNotExist:
#     #     raise Http404()
    
#     return render(request,'displays/enlarged_display.html',{"pics":pics})

def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        searched_categories = Pic.search_by_category(search_term)
        message = f"{search_term}"
        
        return render(request,'displays/search.html',{"message":message,"home":searched_categories})
    else:
        message = "You haven't searched for any term"
        return render(request,'displays/search.html',{"message":message})
    
