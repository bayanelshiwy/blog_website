from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin



from blog.models import Blog



@method_decorator(login_required, name='dispatch')
class BlogList(LoginRequiredMixin, ListView):
    model = Blog



class BlogView(DetailView):
    model = Blog

class BlogCreate(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'body', 'picture']
    success_url = reverse_lazy('blog_list')

class BlogUpdate(UpdateView):
    model = Blog
    fields = ['title', 'body', 'picture']
    success_url = reverse_lazy('blog_list')

class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_list')

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'blog/blog_form.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'blog/blog_list.html.html')



