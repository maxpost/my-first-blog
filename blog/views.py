from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
#Hinzugefügt wegen Chart.js
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def home(request):
    return render(request, 'blog/home.html', {})

def resume(request):
    return render(request, 'blog/resume.html', {})

def apps(request):
    return render(request, 'blog/apps.html', {})

#Hinzugefügt wegen Chart.js
class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]


line_chart = TemplateView.as_view(template_name='/templates/blog/resume.html')
line_chart_json = LineChartJSONView.as_view()
