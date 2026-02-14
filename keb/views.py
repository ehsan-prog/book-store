from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required


from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from .models import Kteb
from .froms import FormComment,FormKteb
class Home(generic.ListView):
    model = Kteb
    paginate_by = 6
    template_name = "home.html"
    context_object_name = 'kteb'



# class Detail_kteb(generic.DetailView):
#     model = Kteb
#     template_name = "detail_kteb.html"

@login_required
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

# class Add_kteb(LoginRequiredMixin,generic.CreateView):
#     model = Kteb
#     template_name = "add_kteb.html"
#     fields = ["title","author","touzihat","price","cover"]
@login_required
def add_kteb(re):
    if re.method == 'POST':
        form = FormKteb(re.POST)
        if form.is_valid():
            form_user = form.save(commit=False)
            form_user.user = re.user
            form_user.save()
           
            return redirect(f"/{form_user.id}/")
            
    else:
        form = FormKteb()
    return render(re,"add_kteb.html",{'form':form})

class Update_kteb(LoginRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    model = Kteb
    template_name = "add_kteb.html"
    fields = ["title","author","touzihat","price","cover"]
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

class Delete_kteb(LoginRequiredMixin,UserPassesTestMixin,generic.DeleteView):
    model = Kteb
    template_name = 'delete_kteb.html'
    success_url = reverse_lazy("home")
    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user