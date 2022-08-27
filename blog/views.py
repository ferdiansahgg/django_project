from django.shortcuts import render
# Create your views here.

post = [
    {
        'author':'Ferdiansah',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '26 Agustus 2022',
    },
    {
        'author':'Ahmad Arfan Mashuda',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '27 Agustus 2022',
    }
]

def home(request):
    context ={
        'posts': post
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})