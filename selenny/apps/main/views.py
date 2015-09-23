from django.views.generic import TemplateView


class HowToView(TemplateView):
    template_name = 'main/howto.html'


class SelennyView(TemplateView):
    template_name = 'main/selenny.html'

    def get_context_data(self, **kwargs):
        context = super(SelennyView, self).get_context_data(**kwargs)

        start = int(self.kwargs['start'])
        number = int(self.kwargs['number'])

        context['range'] = range(start, start+number)
        return context
