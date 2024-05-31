from django.http import HttpResponse
from .models import item
from django.template import loader
from django.shortcuts import render , redirect
from .forms import itemform
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse, reverse_lazy




# def index(request):
#     item_list = item.objects.all()
#     context={ 'item_list':item_list,
 
       
#     }
#     return render(request,"food/index.html",context)

class IndexClassView(ListView):
    model=item
    template_name='food/index.html'
    context_object_name='item_list'

def it(request):
    return HttpResponse("<h1>This is an item view<h1>")

# def detail(request,item_id):
#     shi=item.objects.get(pk=item_id)
#     context={'shi':shi,
             
#     }
#     return render(request,"food/detail.html",context)

class FoodDetail(DetailView):
    model=item
    template_name='food/detail.html'
   

# def create_form(request):
#     qwer=itemform(request.POST or None)
#     if qwer.is_valid():
#         qwer.save()
#         return redirect('food:index')
    
#     return render(request,'food/item-form.html',{'qwer':qwer,})
class createitem(CreateView):
    model=item
    form_class=itemform
    context_object_name='form'
    

    template_name='food/item-form.html'
    # success_url= reverse_lazy('food:index')
    
    
    def form_valid(self,form):
        form.instance.user_name=self.request.user
        
        return super().form_valid(form)

# def update_item(request,id):
#     pq=item.objects.get(id=id)
#     qwer=itemform(request.POST or None, instance=pq)
#     if qwer.is_valid():
#         qwer.save()
#         return redirect('food:index')
#     return render(request,'food/item-form.html',{'pq':pq,'qwer':qwer})

class updateitem(UpdateView):
    model=item
    form_class=itemform
    template_name='food/item-form.html'

    def form_valid(self,form):
        return super().form_valid(form)

def delete_item(request,id):
    pq=item.objects.get(pk=id)
    if request.method=="POST":
        pq.delete()
        return redirect('food:index')
    return render(request,'food/delete-item.html',{'pq':pq})
    


        