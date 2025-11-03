from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from .models import Quote
from .forms import QuoteForm
import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
# Add this with your other imports from django.contrib.auth
from django.contrib.auth import authenticate, logout


def home(request):
    quotes = Quote.objects.all()
    
    # Get the main random quote (same as before)
    if quotes.exists():
        quote = random.choice(quotes) 
    else:
        quote = None
    
    # --- NEW PART ---
    # Get the first 4 distinct genres from the database
    # We use .distinct() to avoid duplicates
    genres = Quote.objects.values_list('genre', flat=True).distinct()[:4]
    
    # Pass BOTH to the template
    context = {
        'quote': quote,
        'genres': genres  # Pass the new list of genres
    }
    return render(request, 'home.html', context)

def all_quotes(request):
    query = request.GET.get('q')
    if query:
      
        quotes = Quote.objects.filter(text__icontains=query) | Quote.objects.filter(author__icontains=query) | Quote.objects.filter(genre__icontains=query)
    else:
      
        quotes = Quote.objects.all()

    paginator = Paginator(quotes, 8)
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number) 

    return render(request, 'all_quotes.html', {'quotes': page_obj, 'query': query})


def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuoteForm()

    return render(request, 'add_quote.html', {'form': form})


@login_required
def like_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    if request.user not in quote.liked_by.all():
        quote.like += 1
        quote.liked_by.add(request.user)
        quote.save()
    return redirect('all_quotes')


def author_quotes(request, author_name):
    quotes = Quote.objects.filter(author=author_name)
    return render(request, 'quotes/author_quotes.html', {'quotes': quotes, 'author': author_name})



def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('email')
        pwd = request.POST.get('pwd')
        
        if fnm and emailid and pwd:
            user = User.objects.create_user(username=fnm, email=emailid, password=pwd)
            user.save()
            return redirect('login')
        else:
            return render(request, 'signup.html')

    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        
        user = authenticate(request, username=fnm, password=pwd)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    return render(request, 'login.html')

# In views.py

# In views.py

def logout_view(request):
    logout(request)
    return redirect('signup') # Change this line