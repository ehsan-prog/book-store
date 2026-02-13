from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render



from .models import Kteb
from .froms import FormComment

class Home(generic.ListView):
    model = Kteb
    paginate_by = 6
    template_name = "home.html"
    context_object_name = 'kteb'



# class Detail_kteb(generic.DetailView):
#     model = Kteb
#     template_name = "detail_kteb.html"

def detail_kteb(re,pk):
    kteb = get_object_or_404(Kteb,pk=pk)
    nazar = kteb.nazar.all()
    if re.method == "POST":
        formn = FormComment(re.POST)
        if formn.is_valid():
            new = formn.save(commit=False)
            new.book = kteb
            new.user = re.user
            new.save()
            formn = FormComment()
            

    else :
        formn = FormComment()
    xx = {"kteb":kteb,
          "nazar":nazar,
          "form":formn}
    return render(re,"detail_kteb.html",xx)

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