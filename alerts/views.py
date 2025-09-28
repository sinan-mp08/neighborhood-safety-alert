# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Alert, Report

# -------------------------------
# Custom Login View
# -------------------------------
class CustomLoginView(LoginView):
    template_name = 'alerts/login.html'
    success_url = reverse_lazy('dashboard')  # default redirect

    def get_success_url(self):
        # Redirect to 'next' if present, otherwise use success_url
        return self.get_redirect_url() or self.success_url

# -------------------------------
# Dashboard view (requires login)
# Shows official alerts and approved reports
@login_required(login_url='login')
def dashboard_view(request):
    # Official alerts only
    official_alerts = Alert.objects.filter(is_official=True).order_by('-date_created')
    
    # User reports only (all reports)
    user_reports = Report.objects.all().order_by('-date_reported')
    
    return render(request, 'alerts/dashboard.html', {
        'official_alerts': official_alerts,
        'user_reports': user_reports
    })

    

# -------------------------------
# Home page view (simple landing page)
# -------------------------------
def home(request):
    return render(request, 'alerts/home.html')

# -------------------------------
# Register view
# -------------------------------
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in immediately
            messages.success(request, 'Account created successfully! Welcome!')
            return redirect('dashboard')  # make sure this matches your urls.py
    else:
        form = UserCreationForm()
    return render(request, 'alerts/register.html', {'form': form})


from .models import Alert

# List of all alerts page
@login_required(login_url='login')
def alerts_list_view(request):
    alerts = Alert.objects.all().order_by('-date_created')
    return render(request, 'alerts/alerts_list.html', {'alerts': alerts})



from django.contrib import messages
@login_required(login_url='login')
def report_incident_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        if not all([title, description, latitude, longitude]):
            messages.error(request, "Please fill all fields and select a location on the map.")
            return redirect('report_incident')

        location_str = f"{latitude}, {longitude}"

        Report.objects.create(
            reporter=request.user,
            title=title,
            description=description,
            latitude=latitude,
            longitude=longitude,
            location=location_str,
            status='Pending'
        )
        messages.success(request, "Report submitted successfully!")
        return redirect('dashboard')

    return render(request, 'alerts/report_incident.html')



from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    """
    Logs out the user and redirects to login page.
    """
    next_page = 'login'  # redirect after logout



 