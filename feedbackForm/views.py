from django.shortcuts import render
from django.views.generic.edit import FormView
from feedbackForm.forms import FeedbackForm

# Create your views here.
class FeedbackView(FormView):
    template_name = 'feedback/contact.html'

    form_class = FeedbackForm
    success_url = '/'