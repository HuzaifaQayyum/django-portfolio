from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from contact.forms import *


class ContactView(generic.TemplateView):
    template_name = 'contact/contact_form.html'
    success_url = reverse_lazy('contact:contact-success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["client_form"] = ClientForm()
        context["project_form"] = ProjectForm()
        context.update(kwargs)
        return context

    def post(self, request):
        client_form = ClientForm(request.POST)
        project_form = ProjectForm(request.POST)

        
        if client_form.is_valid() and project_form.is_valid():
            client = client_form.save()
            project_form.save(client=client)
            return HttpResponseRedirect(self.success_url)

        return self.render_to_response(self.get_context_data(client_form=client_form, project_form=project_form))


class ContactSuccessView(generic.TemplateView):
    template_name = 'contact/contact_success.html'
