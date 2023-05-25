from django.views.generic import ListView
from .models import BlogModel, PortfolioPostModel
from django.shortcuts import render
from django.core.mail import send_mail
from django.views import View
from .forms import ContactForm


class MainPage(ListView):
    model = BlogModel
    template_name = "themes/theme-particle.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context["portfolio_posts"] = PortfolioPostModel.objects.all()
        context["posts"] = BlogModel.objects.all()
        context["form"] = ContactForm()
        return context

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            # Отправить письмо
            send_mail(subject, message, email, ['aleksandrsd006@gmail.com'])
            return render(request, 'themes/theme-particle.html')
        return render(request, 'themes/theme-particle.html', {'form': form})
