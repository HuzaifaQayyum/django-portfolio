from django.core.mail import mail_admins, send_mail

from contact.forms import ClientForm, ProjectForm


class ContactService:

    @staticmethod
    def send_confirmation_mail_to_client(client):
        send_mail(
            subject="Hey there, We received your proposal.",
            message=f"Dear {client.name}, we appreciate your choice. We will contact you back as soon as possible. Thanks.",
            from_email="squad_alien@official.com",
            recipient_list=[client.email]
        )

    @staticmethod
    def notify_admin(project):
        mail_admins(
            subject=f"{project.client.name} sent you project proposal",
            message=f"""
                Name: {project.client.name}
                Email: {project.client.email}
                Description: { project.description}
                Budget: { project.budget }
            """
        )


    @staticmethod
    def save_client(request):
        client_form = ClientForm(request.POST)

        if client_form.is_valid():
            return client_form.save()

            
    @staticmethod
    def validate_project_and_client(request):
        client_form = ClientForm(request.POST)
        project_form = ProjectForm(request.POST)

        forms_valid = client_form.is_valid() and project_form.is_valid()
        return forms_valid, client_form, project_form

    @staticmethod
    def save_client_and_project(client_form, project_form):
        client = client_form.save()
        project = project_form.save(client=client)

        return client, project


    @staticmethod
    def save_project_and_send_mail(client_form, project_form):
        client, project = ContactService.save_client_and_project(client_form, project_form)
        ContactService.send_confirmation_mail_to_client(client)
        ContactService.notify_admin(project)
