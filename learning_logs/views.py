from django.shortcuts import render
from .models import Topic

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