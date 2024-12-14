from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from disasters.models import About
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    if request.GET.get('filter'):
       queryset = queryset.filter(category__icontains = request.GET.get('filter'))
    return render(request,'index.html')
def data(request):
    
    return render(request,'data.html')
def login_page(request):
    userid = request.POST.get('userid')
    password = request.POST.get('password')
    if User.objects.filter(username=userid).exists():
        
        return redirect('index/')
    user = authenticate(userid=userid,password=password)
    if user is None:
        messages.error(request,'invalid password')
        return render(request, 'login.html')
    else:
        login(request,user)
        return redirect('/index')

def register(request):
    if request.method == "POST":
        
        
        userid = request.POST.get('userid')
        password = request.POST.get('password')
      
        user = User(userid=userid,password=password)
        user.set_password(password)
        user.save()
        messages.error(request,'username is saved :)')
        return redirect('/register')
    return render(request,'register.html')
    
def services(request):
    return render(request,'services.html')
   # return HttpResponse("this is a about page")
def about(request):
    if request.method == "POST":
        data = request.POST
        disaster_name= request.POST.get('disaster_name')
        date_disaster = request.POST.get('date_disaster')
        dead = request.POST.get('dead')
        injured = request.POST.get('injured')
        heading  = request.POST.get('heading')
        category =request.POST.get('category')
        description = request.POST.get('description')
        about = About(disaster_name=disaster_name,date_disaster=date_disaster,dead=dead,injured=injured,heading=heading,category=category,description=description)
        about.save()
        return redirect('/about')
    queryset = About.objects.all()
    context = {'abouts': queryset}
    return render(request,'about.html',context) 
def delete(request, id):
    queryset = About.objects.get(id = id)
    queryset.delete()
    return redirect('/about')
def services(request, id):
    queryset = get_object_or_404(About,id=id)
    if request.method == "POST":
        data = request.POST
        disaster_name = data.get('disaster_name')
        date_disaster = data.get('date_disaster')
        dead = data.get('dead')
        injured = data.get('injured')
        heading  = data.get('heading')
        category = data.get('category')
        description = data.get('description')
        queryset.disaster_name = disaster_name
        queryset.date_disaster = date_disaster
        queryset.dead = dead
        queryset.injured = injured
        queryset.heading = heading
        queryset.category = category
        queryset.description = description
        queryset.save()
        return redirect('/about')
    context = {'abouts': queryset}
    return render(request,'services.html',context)