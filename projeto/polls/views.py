from django.views.generic import TemplateView

class PollsView(TemplateView):
    template_name = 'polls.html'