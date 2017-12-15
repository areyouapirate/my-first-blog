from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from .models import Post, Inscription, Place
from .forms import PostForm, SignUpForm, InscrForm, PlaceForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token, post_token
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .filters import InscriptionFilter, PlaceFilter
import datetime

"""
POST ENVIRONMENT

"""

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required(login_url='/login/')
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if (form.is_valid() and request.user.is_staff):
            post = form.save(commit=False)
            post.author = request.user
            post.gruppo = request.user.profile.gruppo
            post.published_date = timezone.now()
            post_x = form.cleaned_data.get('x')
            post.save()
            if post.img:
                form.save_img()
            return redirect('post_detail', pk=post.pk)
        elif form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.gruppo = request.user.profile.gruppo
            post.save()
            if post.img:
                form.save_img()
            target = User.objects.filter(profile__gruppo=post.gruppo, is_staff=True)
            if not target:
                target = User.objects.filter(is_staff=True)
            for user in target:
                current_site = get_current_site(request)
                subject = 'Richiesta post'
                if post.img:
                    message = render_to_string('blog/post_request_email.html', {
                        'user': request.user,
                        'domain': current_site.domain,
                        'title': post.title,
                        'text': post.text,
                        'image': post.img.url,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'pid': urlsafe_base64_encode(force_bytes(post.pk)),
                        'token': post_token.make_token(user),
                        })
                else:
                    message = render_to_string('blog/post_request_email.html', {
                        'user': request.user,
                        'domain': current_site.domain,
                        'title': post.title,
                        'text': post.text,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'pid': urlsafe_base64_encode(force_bytes(post.pk)),
                        'token': post_token.make_token(user),
                        })
                user.email_user(subject, message)
                return redirect('post_detail', pk=post.pk)
        
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})




def post_confirm(request, uidb64, pidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        pid = force_text(urlsafe_base64_decode(pidb64))
        user = User.objects.get(pk=uid)
        post=Post.objects.get(pk=pid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and post_token.check_token(user, token):
        post.published_date = timezone.now()
        post.approval = user.username
        post.save()
        return redirect('/')
    else:
        return render(request, 'blog/account_activation_invalid.html')

@login_required(login_url='/login/')
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if (request.method == "POST" and post.gruppo == request.user.profile.gruppo and request.user.is_staff or request.user.is_superuser and request.method == "POST"):
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            if post.img:
                form.save_img()            
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})





"""
LOGIN-SIGNUP ENVIRONMENT

"""



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.gruppo = form.cleaned_data.get('gruppo')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            message = render_to_string('blog/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})
def account_activation_sent(request):
    return render(request, 'blog/account_activation_sent.html')
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.registration_date = timezone.now()
        user.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'blog/account_activation_invalid.html')
def profile_detail(request):
    user = get_object_or_404(User, username=request.user)
    return render(request, 'blog/profile_detail.html', {'user': user})

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'Esiste già un utente con questo username.'
    else:
        data['error_message'] = 'Questo va bene.'
    return JsonResponse(data)
"""
INSCRIPTIONS ENVIRONMENT

"""


@login_required(login_url='/login/')
def inscr_new(request):
    if request.method == "POST":
        form = InscrForm(request.POST)
        if form.is_valid():
            inscr = form.save(commit=False)
            inscr.author = request.user
            inscr.published_date = datetime.datetime.now()
            inscr.save()
            return redirect('inscr_detail', pk=inscr.pk)
    else:
        form = InscrForm()
    return render(request, 'blog/inscr_edit.html', {'form': form})
def inscr_detail(request, pk):
    inscr = get_object_or_404(Inscription, pk=pk)
    if (request.user.is_staff and request.user.profile.gruppo == inscr.first_choice or inscr.author == request.user or request.user.is_staff):
        return render(request, 'blog/inscr_detail.html', {'inscr': inscr})
    else:
        return redirect('/')
def inscr_list(request):
    if request.user.is_superuser:
        inscr_origin3 = Inscription.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        inscr_filter3 = InscriptionFilter(request.GET, queryset=inscr_origin3)
        return render(request, 'blog/inscr_list.html', {'filter3': inscr_filter3})
    elif request.user.is_staff:
        inscr_origin1 = Inscription.objects.filter(published_date__lte=timezone.now(), first_choice=request.user.profile.gruppo).order_by('published_date')
        inscr_filter1 = InscriptionFilter(request.GET, queryset=inscr_origin1)
        inscr_origin2 = Inscription.objects.filter(published_date__lte=timezone.now(), second_choice=request.user.profile.gruppo).order_by('published_date')
        inscr_filter2 = InscriptionFilter(request.GET, queryset=inscr_origin2)
        inscr_origin0 = Inscription.objects.filter(published_date__lte=timezone.now(), author=request.user).order_by('published_date')
        inscr_filter0 = InscriptionFilter(request.GET, queryset=inscr_origin0)
        return render(request, 'blog/inscr_list.html', {'filter0': inscr_filter0, 'filter1': inscr_filter1, 'filter2': inscr_filter2})
    else:
        inscr_origin0 = Inscription.objects.filter(published_date__lte=timezone.now(), author=request.user).order_by('published_date')
        inscr_filter0 = InscriptionFilter(request.GET, queryset=inscr_origin0)
        return render(request, 'blog/inscr_list.html', {'filter0': inscr_filter0})


"""
PLACES ENVIRONMENT

"""

@login_required(login_url='/login/')
def place_new(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.author = request.user
            place.published_date = datetime.datetime.now()
            place.save()
            return redirect('place_detail', pk=place.pk)
    else:
        form = PlaceForm()
    return render(request, 'blog/place_edit.html', {'form': form})

def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return render(request, 'blog/place_detail.html', {'place': place})

def place_list(request):
    place_origin0 = Place.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    place_filter0 = PlaceFilter(request.GET, queryset=place_origin0)
    return render(request, 'blog/place_list.html', {'filter0': place_filter0})