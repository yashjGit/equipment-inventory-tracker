from django.shortcuts import render, redirect , get_object_or_404
from .models import Equipment
from .forms import EquipmentForm

def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'tracker/equipment_list.html', {'equipments': equipments})

def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    
    return render(request, 'tracker/add_equipment.html', {'form': form})

def edit_equipment(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm(instance=equipment)
    
    return render(request, 'tracker/edit_equipment.html', {'form': form, 'equipment': equipment})

def delete_equipment(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        equipment.delete()
        return redirect('equipment_list')
    
    return render(request, 'tracker/delete_equipment.html', {'equipment': equipment})