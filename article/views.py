from django.shortcuts import render, redirect
from .models import Article, Caregory, Profile, Comment, User
from .form import LoginForm, RegistrationForm , SuggestionForm, CommentForm, EditProfileForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.db import IntegrityError
def base_view(request, **kwargs):
    user = request.user
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=user)
        except:
            Profile.objects.create(user=user)
            profile = Profile.objects.get(user=user)
    else:
        profile = []
    categories = Caregory.objects.all()
    context = {
        'categories': categories,
        'profile': profile,
    }
    return context

def index_view(request, **kwargs):


    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    context.update(base_view(request))
    return render(request, 'article/index.html', context)

def category_view(request, pk):
    category = Caregory.objects.get(pk=pk)
    articles = Article.objects.filter(category=category)
    title = category.title
    context = {
        'articles': articles,
        'title': title
    }
    context.update(base_view(request))
    return render(request, 'article/category.html', context)

def article_view(request, pk):
    article = Article.objects.get(pk=pk)
    comments = Comment.objects.filter(article=article)
    article.increase_count()
    article.save()
    context = {
        'article': article,
        'comments': comments
    }
    context.update(base_view(request))
    return render(request, 'article/article.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                messages.success(request, 'Authorization was done successfully !')
                return redirect('index')
            else:
                messages.error(request, 'Incorrect login or password')
                return redirect('index')
        else:
            messages.error(request, 'Incorrect login or password')
            return redirect('index')

def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration was done successfully !')
            return redirect('index')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect('index')


def user_logout(request):
    logout(request)
    messages.warning(request, 'Log out')
    return redirect('index')

def suggestions(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.user = request.user
            suggestion.save()
            messages.success(request, 'Your suggestion was saved successfully!')
            return redirect('index')
        else:
            messages.error(request,'Your suggestion was not saved')

def save_comment(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.profile = request.user.profile
            comment.article = Article.objects.get(pk=pk)
            comment.save()
            messages.success(request, 'Your comment was saved successfully!')
            return redirect('article', pk)
        else:
            return messages.error(request, 'Your comment was not saved')

def profile(request):

    context = base_view(request)
    return render(request, 'article/profile.html', context)



def edit_account(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        try:
            user = request.user
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            messages.success(request, 'Account updated successfully!')
            return redirect('profile')
        except IntegrityError:
            messages.error(request,'User with this username is exist')
            return redirect('profile')

    else:
        messages.error(request,'error')
        return render(request, 'profile.html')



def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data['photo']
            if photo:
                profile = request.user.profile
                profile.photo = photo
                profile.save()
                return render(request, 'article/profile.html', {'profile': profile})
            else:
                messages.error(request, 'Something goes wrong!')
                return render(request, 'profile.html', {'form': form})
    else:
        form = EditProfileForm()
    return render(request, 'profile.html', {'form': form})




def search_view(request):
    categories = Caregory.objects.all()
    query = request.GET.get('query')
    if query:
        articles = Article.objects.filter(title__icontains=query.select)
    else:
        articles = None
    return render(request, 'article/search.html', {'articles': articles, 'categories':categories , 'query': query})