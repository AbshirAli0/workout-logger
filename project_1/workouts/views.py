from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Workout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy


# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form":form})

@login_required
def home(request):
    return render(request, "home.html")

class WorkoutListView(LoginRequiredMixin, ListView):
    model = Workout
    template_name = "workouts/workout_list.html"
    context_object_name = "workouts"

    def get_queryset(self):
        return Workout.objects.filter(user= self.request.user)

class WorkoutCreateView(LoginRequiredMixin,CreateView):
    model = Workout
    fields = ["exercise", "weight", "sets", "reps"]
    template_name = "workouts/workout_forms.html"
    success_url = reverse_lazy('workout-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class WorkoutUpdateView(LoginRequiredMixin,UpdateView):
    model = Workout
    fields = ["exercise","weight","sets","reps"]
    template_name = "workouts/workout_form.html"
    success_url = reverse_lazy("workout-list")

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)


class WorkoutDetailedView(LoginRequiredMixin,DetailView):
    model = Workout
    template_name = "workouts/details.html"
    context_object_name = "workout"

    def get_queryset(self):
        return Workout.objects.filter(user= self.request.user)
    