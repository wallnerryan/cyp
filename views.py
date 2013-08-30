from django.views.generic import TemplateView

#Homepage "landing page"

class LandingPageView(TemplateView):
    template_name = "main/home.html"
