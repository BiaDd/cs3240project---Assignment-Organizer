from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Assignment

from django.utils import timezone

def index(request):
    return render(request, 'schedule/index.html')

def assignment_form(request):
    return render(request, 'schedule/assignment_form.html')

class AssignmentListView(generic.ListView):
    template_name = 'schedule/assignment_list.html'
    context_object_name = 'assignment_list'

    def get_queryset(self):
        return Assignment.objects.all()

def create_assignment(request):
    if (request.method == 'POST'):
        course = request.POST["course"]
        title = request.POST["title"]
        desc = request.POST["desc"]
        due_date = request.POST["due_date"]
        if (not course or not title or not desc or not due_date):
            return render(request, 'schedule/detail.html', {
                'error_message': "Please fill out the text boxes.",
            })
        Assignment.objects.create(
            course = course,
            title = title,
            description = desc,
            date_created = timezone.now(),
            due_date = due_date
        )
        return HttpResponseRedirect(reverse('schedule:assignment_list'))

def delete_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    assignment.delete()
    return HttpResponseRedirect(reverse('schedule:assignment_list'))

