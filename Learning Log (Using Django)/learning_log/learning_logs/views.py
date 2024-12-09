from django.shortcuts import render

from .models import Topic

# Create your views here.

# view for the home page
def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')

# View for the Topics page
def topics(request):
    """Show the list of topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context)

# View for the individual topic page
def topic(request, topic_id):
    """Show the list of entries for each topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}

    return render(request, 'learning_logs/topic.html', context)



