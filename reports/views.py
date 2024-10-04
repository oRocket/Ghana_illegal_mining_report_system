from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ReportForm, CustomUserCreationForm, SearchForm  # Import the SearchForm
from .models import Report, EducationalContent, BlogPost  # Update import to include BlogPost
from django.contrib.auth.models import User
from django.db import models  # Add this import at the top of your file

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in
            return redirect('dashboard')  # Redirect to dashboard after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'reports/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST['username_or_email']
        password = request.POST['password']
        
        # Check if the input is an email or username
        if '@' in username_or_email:
            try:
                user = User.objects.get(email=username_or_email)
                username = user.username  # Get the username from the user object
            except User.DoesNotExist:
                user = None
        else:
            username = username_or_email
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after successful login
        else:
            return render(request, 'reports/login.html', {'error': 'Invalid credentials'})  # Updated path
    
    return render(request, 'reports/login.html')  # Updated path


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def submit_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect('home')
    else:
        form = ReportForm()
    return render(request, 'submit_report.html', {'form': form})

def report_list(request):
    reports = Report.objects.all()
    return render(request, 'report_list.html', {'reports': reports})

def education(request):
    articles = EducationalContent.objects.all().order_by('-date_published')
    return render(request, 'education.html', {'articles': articles})

def home(request):
    recent_incidents = Report.objects.all().order_by('-date_time')[:5]  # Fetch latest 5 incidents
    recent_blogs = BlogPost.objects.all().order_by('-date_published')[:5]  # Fetch latest 5 blogs
    return render(request, 'reports/home.html', {
        'recent_incidents': recent_incidents,
        'recent_blogs': recent_blogs,
    })

@login_required
def dashboard(request):
    search_form = SearchForm(request.GET or None)  # Initialize the form with GET data
    search_query = search_form.data.get('search')  # Get the search query from the form

    if search_query:
        recent_reports = Report.objects.filter(location__icontains=search_query).order_by('-date_time')[:5]
    else:
        recent_reports = Report.objects.all().order_by('-date_time')[:5]

    recent_blogs = BlogPost.objects.all().order_by('-date_published')[:5]

    # Statistics
    total_reports = Report.objects.count()
    resolved_cases = Report.objects.filter(status='resolved').count()  # Adjust based on your status field
    most_affected_areas = Report.objects.values('location').annotate(count=models.Count('id')).order_by('-count')[:3]

    return render(request, 'reports/dashboard.html', {
        'recent_reports': recent_reports,
        'recent_blogs': recent_blogs,
        'total_reports': total_reports,
        'resolved_cases': resolved_cases,
        'most_affected_areas': most_affected_areas,
        'search_form': search_form,  # Ensure this line is present
    })

