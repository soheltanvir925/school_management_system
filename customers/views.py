from django.shortcuts import render, redirect
from customers.models import Client, Domain
from .forms import SchoolRegistrationForm
import datetime

# Create your views here.
def home(request):
    school = Client.objects.exclude(schema_name='public')

    context = {
        "school" : school
    }

    return render(request, 'customers/index.html', context)

def register_school(request):
    if request.method == 'POST':
        form = SchoolRegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['school_name']
            sub = form.cleaned_data['subdomain']
            
            # 1. Create the Tenant
            tenant = Client(
                schema_name=sub.lower().replace('-', '_'), # Ensure schema name is PG friendly
                name=name,
                paid_until=datetime.date.today() + datetime.timedelta(days=30),
                on_trial=True
            )
            tenant.save() # This creates the schema and runs migrations!

            # 2. Create the Domain
            Domain.objects.create(
                domain=f"{sub}.localhost",
                tenant=tenant,
                is_primary=True
            )
            
            return redirect(f"http://{sub}.localhost:8000/admin")
    else:
        form = SchoolRegistrationForm()
    
    return render(request, 'customers/register.html', {'form': form})