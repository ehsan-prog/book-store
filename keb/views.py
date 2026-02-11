from django.views import generic

from .models import Kteb

class Home(generic.ListView):
    model = Kteb
    template_name = "home.html"
    context_object_name = 'kteb'
