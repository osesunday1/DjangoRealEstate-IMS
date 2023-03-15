from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from .filters import *
from django.contrib import messages
from django_pandas.io import read_frame
import plotly 
import plotly.express as px
import json
from django.contrib.auth.decorators import login_required




@login_required()
def delete_agent(request, agent_id):
    agent= Agent.objects.get(pk=agent_id)
    agent.delete()
    return redirect('all-agents')

@login_required()
def delete_property(request, property_id):
    property= Property.objects.get(pk=property_id)
    property.delete()
    return redirect('all-prop')

@login_required()
def delete_client(request, client_id):
    client= Client.objects.get(pk=client_id)
    client.delete()
    return redirect('all-clients')


@login_required()
def update_property(request, property_id):
        property= Property.objects.get(pk=property_id)
        form = PropertyForm(request.POST or None, instance=property)

        if form.is_valid():
            form.save()
            return redirect('all-prop')


        return render(request, 'sow/update_property.html', {
            'property':property,
            'form':form, 
    })

@login_required()
def update_agent(request, agent_id):
        agent= Agent.objects.get(pk=agent_id)
        form = AgentForm(request.POST or None, instance=agent)

        if form.is_valid():
            form.save()
            return redirect('all-agents')


        return render(request, 'sow/update_agent.html', {
            'agent':agent,
            'form':form, 
    })



@login_required()
def update_client(request, client_id):
        client= Client.objects.get(pk=client_id)
        form = ClientForm(request.POST or None,request.FILES or None, instance=client)

        if form.is_valid():
            form.save()
            return redirect('all-clients')


        return render(request, 'sow/update_client.html', {
            'client':client,
            'form':form, 
    })


@login_required()
def add_client(request):
    submitted= False
    if request.method== "POST":
        form= ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_client?submitted=True')
    
    else:    
        form= ClientForm
        if 'submitted' in request.GET:
            submitted= True
            
    return render(request, 'sow/add_client.html', { 'form':form, 'submitted':submitted})

'''
def add_client(request):
    if request.method == "POST":
        updateForm = ClientForm(data=request.POST)
        if updateForm.is_valid():
            new_client = updateForm.save(commit=False)
            new_client.agent_name.number_of_properties_sold = int(updateForm.data['number_of_properties_sold']) + 1
            new_client.save()
            messages.success(request, "Successfully Added Product")
            return redirect(f"/sow_app/")
    else:
        updateForm = ClientForm()

    return render(request, "sow/add_client.html", {'form' : updateForm})
'''




@login_required()
def show_client(request, client_id):
    client= Client.objects.get(pk=client_id)

    return render(request, 'sow/show_client.html', {
      'client':client,  
    })


@login_required()
def all_clients(request):
    client_list= Client.objects.all().order_by('first_name')

    myFilter= ClientFilter(request.GET, queryset=client_list)
    client_list= myFilter.qs

    return render(request, 'sow/all_clients.html', {
      'client_list':client_list, 
      'myFilter':myFilter 
    })


@login_required()
def add_agent(request):
    submitted= False
    if request.method== "POST":
        form= AgentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_agent?submitted=True')
    
    else:    
        form= AgentForm
        if 'submitted' in request.GET:
            submitted= True
            
    return render(request, 'sow/add_agent.html', { 'form':form, 'submitted':submitted})


'''
def add_agent(request):
    if request.method == "POST":
        updateForm = AgentForm(data=request.POST)
        if updateForm.is_valid():
            new_agent = updateForm.save(commit=False)
            new_agent.number_of_properties_sold = new_agent.objects.all().aggregate(Sum('agent_name'))
            new_agent.save()
            messages.success(request, "Successfully Added Product")
            return redirect(f"/sow_app/")
    else:
        updateForm = AgentForm()

    return render(request, "sow/add_agent.html", {'form' : updateForm})
'''




@login_required()
def all_agents(request):
    agent_list= Agent.objects.all()
    return render(request, 'sow/all_agents.html', {
      'agent_list':agent_list  
    })

@login_required()
def add_property(request):
    submitted= False
    if request.method== "POST":
        form= PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_property?submitted=True')
    
    else:    
        form= PropertyForm
        if 'submitted' in request.GET:
            submitted= True
            
    return render(request, 'sow/add_property.html', { 'form':form, 'submitted':submitted})

@login_required()
def all_prop(request):
    property_list= Property.objects.all()
    return render(request, 'sow/all_prop.html', {
      'property_list':property_list  
    })



@login_required()
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B'), day=datetime.now().strftime('%d')):
    name="John"
    month= month.title()
    
    #convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    month_day = day

    #create a calendar
    cal= HTMLCalendar().formatmonth(year, month_number)

    #get current year
    now = datetime.now()
    current_year= now.year

    #GET CURRENT TIME
    current_time= datetime.now().strftime('%H:%M:%S')

    #2nd GET CURRENT TIME
    current_time2 = datetime.now().time()  


    return render(request, 
    'sow/home.html', 
    {
        "name":name,
        "year":year,
        "month":month,
        "month_number": month_number,
        "month_day": month_day,
        "cal":cal,
        "current_year": current_year,
        "current_time": current_time,
        "current_time2":current_time2,

    })

@login_required()
def dashboard(request):
    
    agent= Agent.objects.all()
    client= Client.objects.all()
    property= Property.objects.all()

    df= read_frame(agent)
    df1= read_frame(client)
    df2= read_frame(property)
    


    b1_df= df.groupby (by= "first_name").sum().sort_values(by="number_of_properties_sold")
    b1= px.bar(b1_df,
                                    x = b1_df.index,
                                    y = b1_df.number_of_properties_sold,
                                    title= "Trending Agents"
                                    )
    b1= json.dumps(b1, cls=plotly.utils.PlotlyJSONEncoder)



    p1_df = df2.groupby (by= "building_type").sum().sort_values(by="quantity_sold")
    p1 = px.pie(p1_df,
                                   names= p1_df.index,
                                   values= p1_df.quantity_sold,
                                   title= "Trending Properties"
                                   )
    p1= json.dumps(p1, cls=plotly.utils.PlotlyJSONEncoder)
    
    
    p2_df = df2.groupby (by= "building_type").sum().sort_values(by="quantity_in_stock")
    p2 = px.bar(p2_df,
                                   x= p2_df.index,
                                   y= p2_df.quantity_in_stock,
                                   title= "Properties in Stock"
                                   )
    p2= json.dumps(p2, cls=plotly.utils.PlotlyJSONEncoder)


    c1_df= df1.groupby (by= "first_name").sum().sort_values(by="amount_left")
    c1= px.bar(b1_df,
                                    x = c1_df.index,
                                    y = c1_df.amount_left,
                                    title= "Debts"
                                    )
    c1= json.dumps(c1, cls=plotly.utils.PlotlyJSONEncoder)
    







    context = {
        "b1": b1,
        "p1":p1,
        "c1":c1,
        "p2":p2
    }

    return render (request, "sow/dashboard.html", context= context)

