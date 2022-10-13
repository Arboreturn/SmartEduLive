from django.shortcuts import render
from django.views.generic.list import ListView
from teachers.models import Teacher
from django.views.generic.detail import DetailView
from courses.models import Course
# Create your views here.

class TeacherListView(ListView):
    model = Teacher
    template_name = "teachers.html"
    context_object_name = 'teachers'
    # paginate_by = 2 bu da sayflama daha best pratice ama şuanlık kullanmayacağız
    #queryset = Teacher.objects.all()[:1] sayfada kaç tane öğretmen gösterileceği
    
    # def get_queryset(self):
    #     return Teacher.objects.all()[:2] # kaç tane öğretmen var aynı mantık ama fonksiyon tabanlı


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = "teacher.html"
    context_object_name = 'teacher'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available=True, teacher =self.kwargs["pk"]) #hocaların sayfasındaki filtreleme kısmı
        return context
    