from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy


from project.forms import TopicForm, FoodForm
from project.models import Topic, Food
from django.http import HttpResponse, HttpResponseRedirect



class Home(generic.CreateView):
    def get(self, request):
        return render(request, 'home.html')

class TopicListView(generic.ListView):
    """ Renders a list of all projects. """
    model = Topic

    def get(self, request):
        """ GET a list of projects. """
        topics = self.get_queryset().all()
        return render(request, 'list.html', {
          'topics': topics
        })


class TopicDetailView(generic.DetailView):
    """ Renders a specific project based on it's slug."""
    model = Topic

    def get(self, request, slug):
        """ Returns a specific projects project by slug. """
        topic = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'topic.html', {
          'topic': topic
        })
class TopicCreateView(generic.CreateView):
    form_class = TopicForm
    template_name = "new_topic.html"

    def post(self, request, *args, **kwargs):
        form = TopicForm(request.POST)
        if form.is_valid():
            project = form.save()
            project.save()
            return HttpResponseRedirect(reverse_lazy("topic-details-project", args=[project.slug]))

class TopicUpdateView(generic.UpdateView):
    model = Topic
    fields = ['title','content']
    template_name = 'new_topic.html'

class TopicDeleteView(generic.DeleteView):
    model = Topic
    success_url = reverse_lazy('topic-list-project')
    template_name = 'confirm_delete.html'


def food_image_view(request):

    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('foods')


    else:
        form = FoodForm()
    return render(request, 'new_food.html', {'form' : form})



def display_food_images(request):

    if request.method == 'GET':

        # getting all the objects of hotel.
        Foods = Food.objects.all()
        return render(request, 'food_recipes.html',
                     {'foods' : Foods})

class FoodDetailView(generic.DetailView):
    """ Renders a specific project based on it's slug."""
    model = Food

    def get(self, request, pk):
        """ Returns a specific projects project by slug. """
        food = Food.objects.get(pk=pk)
        return render(request, 'food_detail.html', {
          'food': food
        })

class FoodUpdateView(generic.UpdateView):
    model = Food
    fields = ['title', 'image', "ingredients"]
    template_name = 'new_food.html'

class FoodDeleteView(generic.DeleteView):
    model = Food
    success_url = reverse_lazy('foods')
    template_name = 'food_confirm_delete.html'
