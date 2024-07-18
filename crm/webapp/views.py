from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required  
from .models import Record, Categorie
from django.db.models import Q
from django.contrib import messages
import logging


# - Home

def home(request):
    return render(request, 'webapp/index.html')




# - Register

def register(request):
    
    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST) 

        if form.is_valid():

            form.save()

            # messages.success(request, 'Account created successfull!')

            return redirect('login')
            
    else:

        form = CreateUserForm()        

    context = {'form':form,}  
    
    return render(request, 'webapp/register.html', context)     




# - Login a user

def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username= request.POST.get('username')
            password= request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:login(request, user) 

            # messages.success(request, 'You have logged.')
         
            return redirect('dashboard')
    else:
        form = LoginForm()

    context = {'form':form,}   

    return render(request, 'webapp/login.html', context=context)          




# - Dashboard 

@login_required(login_url='login') 
def dashboard(request):

    my_records = Record.objects.all()

    context = {'records':my_records,}

    return render(request, 'webapp/dashboard.html', context=context)




# - Create a new record

@login_required(login_url='login')
def create_record(request):

    form = CreateRecordForm()

    if request.method == 'POST':

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()
            
            messages.success(request, 'Your record was created.')

            return redirect('dashboard')
        # messages.success(request, 'Added Your Record.')    


    context = {
        'form':form
    }    

    return render(request, 'webapp/create-record.html', context=context)





# - Update a record

@login_required(login_url='login')
def update_record(request, record_id):

    record = get_object_or_404(Record, id=record_id)

    form = UpdateRecordForm(instance=record ) # instance means select the record to get from URL

    if request.method == 'POST':
        
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            
            form.save()

            # messages.success(request, 'Your record was updated.')
            
            return redirect('dashboard')
        

    context = {
        'form':form
    }
    
    return render(request, 'webapp/update-record.html', context=context)





# - Read / View a singular record

@login_required(login_url='login')
def view_record(request, record_id):

    all_records = get_object_or_404(Record, id=record_id)
    
    context = {'record':all_records}
    
    return render(request, 'webapp/view-record.html', context=context) 





# - Delete a record

@login_required(login_url='login')
def delete_record(request, record_id):

    record = get_object_or_404(Record, id=record_id)

    record.delete()
    # messages.success(request, 'Your record was deleted.')

    return redirect('dashboard')




# - Search about a record
logger = logging.getLogger(__name__)

@login_required(login_url='login')
def search(request):
    query = request.GET.get('query')
    results = []
    try:
        if query:
            results = Record.objects.filter(Q(first_name__icontains=query) | Q(id__icontains=query))
    except Exception as e:
        logger.error("Error during search: %s", e)
    return render(request, 'webapp/search.html', context={'results': results, 'query': query})



# User Logout

def user_logout(request):
    logout(request)
    
    # messages.success(request, 'Logout success!')

    return redirect('login')




def custom_page_not_found_view(request, exception):
    return render(request, 'webapp/404.html', status=404)