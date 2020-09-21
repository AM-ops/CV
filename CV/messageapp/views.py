from django.views.generic.edit import CreateView
from .models import MessagesModel
from .forms import MessagesForm
from django.urls import reverse, reverse_lazy
class MessageCreate(CreateView):
    template = 'messagesmodel_form.html'
    model = MessagesModel
    fields = ['name','email','message']
    success_url = reverse_lazy("success")
