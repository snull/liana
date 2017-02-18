from django.shortcuts import render, get_object_or_404
from .models import Post
from datetime import datetime
from json import JSONEncoder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import Http404
from django.contrib.auth.models import User
from django.core import serializers
from mySources import get_token
from django.views.decorators.http import require_POST
from .forms import PostForm

# Create your views here.
def list(request):
    posts = Post.objects.all().order_by('-date') # get posts from Post class
    context = {
        'posts': posts,
    } # set a dictionory for posts
    return render(request, "list.html", context) # return (request, template, context)

@csrf_exempt
@require_POST
def list_json(request):
    num = request.POST.get('num', 100)
    posts = Post.objects.all().order_by('-date')[:num]
    posts_serializered = serializers.serialize('json', posts)
    return JsonResponse(posts_serializered, encoder=JSONEncoder, safe=False)

@csrf_exempt
def new_post(request):
    try:
        this_token = request.POST['token']
        this_user = get_object_or_404(User, token__token=this_token)
        now = datetime.now()
        post_text = request.POST['text']
        new_post = Post(text=post_text, user=this_user, date=now)
        new_post.save()
        status = 'OK'
    except:
        status = 'ERROR'
    context = {}
    context['status'] = status
    return JsonResponse(context, encoder=JSONEncoder)

def register(request):
    return render(request, 'register.html', {})

def create_post(request):
    now = datetime.now()
    print "------------------"
    print request.user.is_staff
    print "------------------"
    if not request.user.is_staff:
        raise Http404
    form = PostForm(request.POST or None, request.FILES,)
    message = {}
    if form.is_valid():
        try:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.date = now
            instance.save()
            message['status'] = 'created successfully! <a href="/posts/list/">See the item</a>'
            message['tags'] = 'alert alert-success safe'
        except:
            message['status'] = 'created failed! try again...'
            message['tags'] = 'alert alert-danger safe'
    context = {
        'form': form,
        'message': message,
    }
    return render(request, 'create.html', context)

def edit_post(request, id=None):
    if not request.user.is_staff:
        raise Http404
    instance = get_object_or_404(Post, id=id)

    if not(instance.user == request.user):
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    message
    if form.is_valid():
        try:
            now = datetime.now()
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.date = now
            form.save()
            message['status'] = 'edit successfully! <a href="/posts/list/">See the item</a>'
            message['tags'] = 'alert alert-success safe'
        except:
            message['status'] = 'edit failed! try again...'
            message['tags'] = 'alert alert-danger safe'

    context = {
        'form': form,
    }
    return render(request, 'edit.html', context)
