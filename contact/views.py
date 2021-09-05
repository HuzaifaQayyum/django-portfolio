from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from contact.forms import *
from contact.service import ContactService


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
        forms_valid, client_form, project_form = ContactService.validate_project_and_client(request)
        if forms_valid:
            ContactService.save_project_and_send_mail(client_form, project_form)
            return HttpResponseRedirect(self.success_url)

        return self.render_to_response(self.get_context_data(client_form=client_form, project_form=project_form))


class ContactSuccessView(generic.TemplateView):
    template_name = 'contact/contact_success.html'
