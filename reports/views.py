from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ReportForm, CustomUserCreationForm, SearchForm  # Import the SearchForm
from .models import Report, EducationalContent, BlogPost  # Update import to include BlogPost
from django.contrib.auth.models import User
from django.db import models  # Add this import at the top of your file
from .forms import BlogPostForm
from django.contrib import messages
from datetime import datetime
from django.db.models import Count


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
            report.reporter_name = f"{request.user.first_name} {request.user.last_name}"
            report.save()
            return redirect('home')
        else:
            print(form.errors)  # Log form errors for debugging
    else:
        form = ReportForm()
    return render(request, 'reports/submit_report.html', {'form': form})

def report_list(request):
    reports = Report.objects.all()
    return render(request, 'reports/report_list.html', {'reports': reports})

def report_list(request):
    reports = Report.objects.all().order_by('-date_time')  # Order by date_submitted in descending order
    return render(request, 'reports/report_list.html', {'reports': reports})

def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return render(request, 'reports/report_detail.html', {'report': report})

@login_required
def report_edit(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            form.save()
            return redirect('report_detail', pk=report.pk)
        else:
            messages.error(request, "Form is invalid. Please correct the errors below.")
            print("Form errors:", form.errors)  # Log errors for debugging
    else:
        form = ReportForm(instance=report)
    return render(request, 'reports/report_edit.html', {'form': form})

@login_required
def report_delete(request, pk):
    report = get_object_or_404(Report, pk=pk)
    report.delete()
    return redirect('report_list')

def education(request):
    articles = EducationalContent.objects.all().order_by('-date')
    return render(request, 'reports/education.html', {'articles': articles})

def home(request):
    recent_incidents = Report.objects.all().order_by('-date_time')[:6]  # Fetch latest 6 incidents
    recent_blogs = BlogPost.objects.all().order_by('-date')[:6]  # Fetch latest 6 blogs
    current_year = datetime.now().year

    return render(request, 'reports/home.html', {
        'recent_incidents': recent_incidents,
        'recent_blogs': recent_blogs,
        'current_year': current_year,
    })

@login_required
def dashboard(request):
    search_form = SearchForm(request.GET or None)  # Initialize the form with GET data
    search_query = search_form.data.get('search')  # Get the search query from the form

    if search_query:
        recent_reports = Report.objects.filter(location__icontains=search_query).order_by('-date_time')[:5]
    else:
        recent_reports = Report.objects.all().order_by('-date_time')[:6]

    recent_blogs = BlogPost.objects.all().order_by('-date')[:4]  # Change to '-date' instead of '-date_published'

    # Statistics
    total_reports = Report.objects.count()
    resolved_cases = Report.objects.filter(status='resolved').count()  # Adjust based on your status field
    most_affected_areas = Report.objects.values('location').annotate(count=models.Count('id')).order_by('-count')[:3]

    # Most affected regions logic
    most_affected_regions = (
        Report.objects.values('region')
        .annotate(count=Count('id'))
        .order_by('-count')[:5]
    )

    # Debugging output
    print("Most Affected Regions:", most_affected_regions)

    # Find the region with the maximum reports
    top_region = most_affected_regions.first() if most_affected_regions else None

    return render(request, 'reports/dashboard.html', {
        'recent_reports': recent_reports,
        'recent_blogs': recent_blogs,
        'total_reports': total_reports,
        'resolved_cases': resolved_cases,
        'most_affected_areas': most_affected_areas,
        'most_affected_regions': most_affected_regions,  # Include this
        'top_region': top_region,  # Include this if needed
        'search_form': search_form,  # Ensure this line is present
    })


def education(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)  # Create a BlogPost instance but don't save it yet
            blog_post.author = request.user  # Automatically assign the logged-in user as the author
            blog_post.save()  # Now save it to the database
            return redirect('education')  # Assuming 'education' is the name of the URL
    else:
        form = BlogPostForm()

    # Get all blog posts to display
    articles = BlogPost.objects.all().order_by('-date')  # Assuming you want to order by most recent

    return render(request, 'reports/education.html', {'form': form, 'articles': articles})

# Blog list view (for education.html)
def blog_list(request):
    blog_posts = BlogPost.objects.all().order_by('-date')
    return render(request, 'reports/blog_list.html', {'blog_posts': blog_posts})

# Blog detail view (for blog_detail.html)
def blog_detail(request, post_id):
    blog = get_object_or_404(BlogPost, id=post_id)  # Fetch the specific blog post by its ID
    return render(request, 'reports/blog_detail.html', {'blog': blog})

# Edit blog post view (for edit_blog.html)
@login_required
def edit_blog(request, post_id):
    # Get the blog post by ID
    blog_post = get_object_or_404(BlogPost, id=post_id)

    # Check if the current user is the author of the blog post
    if blog_post.author != request.user:
        # Optionally add a message for unauthorized access
        messages.error(request, "You do not have permission to edit this blog post.")
        return redirect('blog_detail', post_id=post_id)  # Redirect to the blog detail page

    if request.method == "POST":
        # Populate the form with POST data for updating
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()  # Save the changes
            messages.success(request, "Blog post updated successfully!")  # Optional success message
            return redirect('blog_detail', post_id=blog_post.id)  # Redirect to the blog detail page
    else:
        # Pre-fill the form with the current blog post data
        form = BlogPostForm(instance=blog_post)

    context = {
        'form': form,
        'blog_post': blog_post
    }
    return render(request, 'reports/edit_blog.html', context)


@login_required
def delete_blog(request, id):
    blog = get_object_or_404(BlogPost, id=id)

    # Ensure that only the author can delete the blog post
    if request.user == blog.author:
        blog.delete()
        messages.success(request, 'Blog post deleted successfully.')
        return redirect('blog_list')  # Redirect to the blog list after deletion
    else:
        messages.error(request, 'You are not authorized to delete this blog post.')
        return redirect('blog_detail', id=blog.id)