from django.views import generic
from django.urls import reverse_lazy
from .models import Kteb

class Home(generic.ListView):
    model = Kteb
    paginate_by = 6
    template_name = "home.html"
    context_object_name = 'kteb'

class Detail_kteb(generic.DetailView):
    model = Kteb
    template_name = "detail_kteb.html"

class Add_kteb(generic.CreateView):
    model = Kteb
    template_name = "add_kteb.html"
    fields = ["title","author","touzihat","price","cover"]

class Update_kteb(generic.UpdateView):
    model = Kteb
    template_name = "add_kteb.html"
    fields = ["title","author","touzihat","price","cover"]

class Delete_kteb(generic.DeleteView):
    model = Kteb
    template_name = 'delete_kteb.html'
    success_url = reverse_lazy("home")