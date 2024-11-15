from django.views.generic import TemplateView


class InfoView(TemplateView):
    template_name = 'pages/info.html'
