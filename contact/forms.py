from core.forms import BootstrapModelForm
from django import forms
from django.core.mail import mail_admins, send_mail
from django.forms import widgets

from contact.models import Client, Project


class ClientForm(BootstrapModelForm):
    email = forms.EmailField(widget=widgets.EmailInput(attrs={ 'placeholder': 'Your email' }))

    class Meta:
        model = Client
        fields = ['name']
        widgets = {
            'name': widgets.TextInput(attrs={ 'placeholder': 'Your name' })
        }

    def update_client(self, client):
        client_fields_updated = False
        for key, value in self.cleaned_data.items():
                if getattr(client, key) != value:
                    client_fields_updated = True
                    setattr(client, key, value)
        if client_fields_updated:
            client.save()
            
        return client

    def save(self):
        """
            Check if client with same email already exists, if so update the fields if needed and returns the client
            otherwise create a new client
        """
        client = None
        try:
            client = Client.objects.get(email=self.cleaned_data['email'])
            return self.update_client(client)
        except Client.DoesNotExist:
            return Client.objects.create(**self.cleaned_data)


class ProjectForm(BootstrapModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['budget'].empty_label = 'Project Budget'


    class Meta:
        model = Project
        fields = ['budget', 'description']
        widgets = {
            'description': widgets.Textarea(attrs={ 'placeholder': 'Tell us shortly about your project', 'rows': 6 })
        }

    def save(self, client):
        return Project.objects.create(client=client, **self.cleaned_data)
