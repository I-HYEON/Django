from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):  # 목록 페이지
    movies = Movie.objects.all()  # 모든 영화정보 다 가져오기
    context = {'movies':movies}
    return render(request,'movies/index.html',context)

def detail(request,id):  # 상세페이지
    movie = Movie.objects.get(id=id)  # url의 id 값과 일치하는 무비 인스턴스 받아오기
    context = {'movie':movie}  # 콘텍스트에 담아 넘겨주기
    return render(request,'movies/detail.html',context)

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST,request.FILES)  # 요청 내용이 들어간 폼을 형성
        if form.is_valid():  # 폼이 유효하다면
            movie = form.save()  # 생성된 폼을 db에 반영하고, 해당 인스턴스를 movie에 담기
            return redirect('movies:detail',movie.id)  # 인스턴스의 아이디를 넘겨 detail 페이지로 가기
    else:
        form = MovieForm()  # 빈 폼을 형성
    context = {'form':form}
    return render(request,'movies/create.html',context)  # 해당 폼을 렌더링해서 보여주기

def update(request,id):
    movie = Movie.objects.get(id=id)  # id로 인스턴스 가져오기
    if request.method == 'POST':
        form = MovieForm(request.POST,request.FILES,instance=movie)  # 수정된 내용이 담긴 폼으로 instance를 수정
        form.save()  # dp에 반영
        return redirect('movies:detail',movie.id)  # 수정 완료했으면 detail로 가서 수정된 걸 보여주기
    else:
        form = MovieForm(instance=movie)  # 인스턴스가 담긴 폼 형성
    context = {'form':form,'movie':movie}
    return render(request,'movies/update.html',context)  # 해당 폼을 렌더링해서 보여주기

def delete(request,id):  # 상세페이지
    movie = Movie.objects.get(id=id)  # url의 id 값과 일치하는 무비 인스턴스 받아오기
    movie.delete()  # 지우기
    return redirect('movies:index')  # index로 돌아가기