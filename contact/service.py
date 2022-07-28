from django.core.mail import mail_admins, send_mail

from contact.forms import ClientForm, ProjectForm


class ContactService:

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
        

        return client, project


    @staticmethod
    def save_project(client_form, project_form):
        client, project = ContactService.save_client_and_project(client_form, project_form)
