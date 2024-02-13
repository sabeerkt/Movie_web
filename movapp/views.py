from django.shortcuts import redirect, render
from movapp.forms import moviform
from movapp.models import Movie

def index(request):
    movie = Movie.objects.all()
    context = {
        "mov_list": movie
    }
    return render(request, "index.html", context)

def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "det.html", {'movie': movie})

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        des = request.POST.get('description')
        year = request.POST.get('year')
        img = request.FILES['img']
        mov = Movie(name=name, des=des, year=year, img=img)
        mov.save()

    return render(request, "add.html")

def update(request, id):
    movie = Movie.objects.get(id=id)
    form = moviform(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {"form": form, "movie": movie})
def delet(request, id):
    if request.method == 'POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, "delet.html")
    
