from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Ev
from .forms import ChargingForm
# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def all_evs(request):
    evs = Ev.objects.all()
    context = {'evs': evs}
    return render(request, 'evs/index.html', context)


def evs_detail(request, ev_id):
  ev = Ev.objects.get(id=ev_id)
  # instantiate charging form to be rendered in html
  charging_form = ChargingForm()
  return render(request, 'evs/detail.html', { 'ev': ev, 'charging_form': charging_form})

class EvCreate(CreateView):
  model = Ev
  fields = '__all__'

class EvUpdate(UpdateView):
  model = Ev
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['model', 'body_type', 'battery_mileage']

class EvDelete(DeleteView):
  model = Ev
  template_name = 'main_app/ev_confirmation.html'
  success_url = '/evs'

def add_charging(request, ev_id):
  form = ChargingForm(request.POST)
  if form.is_valid():
    new_charging = form.save(commit=False)
    new_charging.ev_id = ev_id
    new_charging.save()
  return redirect('detail', ev_id=ev_id)