from django import forms
from .models import Report
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BlogPost

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



# Define choices for dropdowns and multi-select fields
REGION_CHOICES = [
    ('Greater Accra', 'Greater Accra'), ('Ashanti', 'Ashanti'), ('Eastern', 'Eastern'), 
    ('Western', 'Western'), ('Central', 'Central'), ('Volta', 'Volta'), ('Oti', 'Oti'), 
    ('Northern', 'Northern'), ('Upper East', 'Upper East'), ('Upper West', 'Upper West'),
    ('Bono', 'Bono'), ('Bono East', 'Bono East'), ('Ahafo', 'Ahafo'), ('Western North', 'Western North'),
    ('North East', 'North East'), ('Savannah', 'Savannah')
]

MINING_TYPE_CHOICES = [
    ('Surface mining', 'Surface mining'),
    ('Alluvial mining', 'Alluvial mining'),
    ('Pit mining', 'Pit mining'),
    ('Dredging', 'Dredging')
]

SCALE_CHOICES = [
    ('Small-scale', 'Small-scale'),
    ('Medium-scale', 'Medium-scale'),
    ('Large-scale', 'Large-scale')
]

METHOD_CHOICES = [
    ('Mercury', 'Mercury'),
    ('Cyanide', 'Cyanide'),
    ('Traditional tools', 'Traditional tools')
]

EFFECT_CHOICES = [
    ('Water pollution', 'Water pollution'),
    ('Air pollution', 'Air pollution'),
    ('Land degradation', 'Land degradation')
]

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('resolved', 'Resolved'),
    ('rejected', 'Rejected'),
]

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            'gps_coordinates', 'region', 'town', 'landmarks', 
            'mining_type', 'scale', 'machinery_used', 'mining_method', 
            'environmental_impact', 'photo', 'suspected_individuals', 
            'num_people_involved', 'reporter_name', 'reporter_contact', 
            'additional_comments', 'status'
        ]

        widgets = {
            'gps_coordinates': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter GPS Coordinates'}),
            'region': forms.Select(attrs={'class': 'form-select'}),
            'town': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Town/Community'}),
            'landmarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Nearby Landmarks (optional)', 'rows': 2}),
            'mining_type': forms.Select(attrs={'class': 'form-select'}),
            'scale': forms.Select(attrs={'class': 'form-select'}),
            'machinery_used': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Machinery Used'}),
            'mining_method': forms.Select(attrs={'class': 'form-select'}),
            'environmental_impact': forms.CheckboxSelectMultiple(),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'suspected_individuals': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Suspected Individuals (optional)'}),
            'num_people_involved': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of People Involved'}),
            'reporter_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name (optional)'}),
            'reporter_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Contact Number (optional)'}),
            'additional_comments': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Additional Comments (optional)', 'rows': 3}),
            'status': forms.Select(choices=STATUS_CHOICES, attrs={'class': 'form-select'})
        }

    gps_coordinates = forms.CharField(widget=forms.HiddenInput(), required=False)
    region = forms.ChoiceField(choices=REGION_CHOICES, widget=forms.Select(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded'}))
    town = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded', 'placeholder': 'Town/Community name'}))
    landmarks = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded', 'placeholder': 'Nearby landmarks (optional)'}), required=False)

    mining_type = forms.ChoiceField(choices=MINING_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded'}), required=False)
    scale = forms.ChoiceField(choices=SCALE_CHOICES, widget=forms.Select(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded'}))
    machinery_used = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded', 'placeholder': 'Machinery used (e.g., excavators, dredgers)'}))

    mining_method = forms.ChoiceField(choices=METHOD_CHOICES, widget=forms.Select(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded'}))
    environmental_impact = forms.MultipleChoiceField(choices=EFFECT_CHOICES, widget=forms.CheckboxSelectMultiple())

    photo = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded'}), required=False)
    
    suspected_individuals = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded', 'placeholder': 'Names of suspected individuals or groups (optional)'}), required=False)
    num_people_involved = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded', 'placeholder': 'Number of people involved (optional)'}), required=False)

    reporter_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded', 'placeholder': 'Your name (optional)'}), required=False)
    reporter_contact = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded', 'placeholder': 'Your contact number (optional)'}), required=False)
    additional_comments = forms.CharField(widget=forms.Textarea(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded', 'placeholder': 'Any additional comments (optional)', 'rows': 4}), required=False)
    
    # Add status field with choices
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'w-full py-2 px-3 border border-gray-300 rounded'}))


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'content',
            'images',
            'categories',
            'references',
            'summary',
            'call_to_action',
            'contact_info'
        ]

class SearchForm(forms.Form):
    location = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Search by location'})
    )