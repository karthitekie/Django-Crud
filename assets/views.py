from django.shortcuts import render, redirect, get_object_or_404
from .models import Asset, Maintenance
from datetime import date
from .forms import AssetForm



def asset_list(request):
    try:
        assets = Asset.objects.all()
    except Asset.DoesNotExist:
        assets = []  
    return render(request, 'asset_list.html', {'assets': assets})


def maintenance_history(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    maintenances = Maintenance.objects.filter(asset=asset)
    return render(request, 'maintenance_history.html', {'asset': asset, 'maintenances': maintenances})


def maintenance_due_report(request):
    today = date.today()
    due_assets = Asset.objects.filter(maintenance__due_date__lte=today)
    return render(request, 'maintenance_due_report.html', {'due_assets': due_assets})



def create_asset(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('/assets/')  
    else:
        form = AssetForm()
    
    return render(request, 'create_asset.html', {'form': form})

def category_view(request):
    return render(request, 'category.html')


def sub_category_view(request):
    return render(request, 'sub_category.html')

def department_view(request):
    return render(request, 'department.html')

def location_view(request):
    return render(request, 'location.html')