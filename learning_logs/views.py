from django.shortcuts import render

from .models import Topic
from .forms import TopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    """Página principal"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Mostrar todos os temas"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request,topic_id):
    """Mostrar um único tema e todas as suas entradas"""
    topic = Topic.objects.get(id= topic_id)
    entrys = topic.entry_set.order_by('-date_added') # Ordenando as entradas do mais antigo para o mais recente
    context = {'topic': topic, 'entrys': entrys}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Adicionar novo topico"""
    if request.method != 'POST':
        form = TopicForm() #Cria um formulário vazio
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics')) # Redireciona para a página de tópicos
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)