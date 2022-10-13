from zoneinfo import available_timezones
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView # template view genelde static sayflarda gösterirlir
from django.views.generic.edit import FormView #
from courses.models import Course
from .forms import ContactForm
from django.contrib.messages.views import SuccessMessageMixin # mixin parametresi ile contact view e gider
from django.contrib.auth.models import User
from teachers.models import Teacher

class İndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available=True).order_by("-date")[:2]
        context['total_course'] = Course.objects.filter(available=True).count()
        context['total_students'] = User.objects.count()
        context['total_teachers'] = Teacher.objects.count()
        return context



# def index(request):
#     return render(request,"index.html")
 
 
class AboutView(TemplateView):
    template_name = "about.html"



class ContactView(SuccessMessageMixin,FormView):
    template_name ="contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('contact') # mesajı alınca nereye gitsin
    success_message = "we receiver you request" # formu gönderdikten sonra teşekkür mesajı
    
    # formu gönderikten sonra
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)