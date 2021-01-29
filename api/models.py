from django.db import models

# Helper functions
def project_cover(instance, filename):
    return "Project_{0}/cover_{1}".format(instance.id, filename)


def project_image(instance, filename):
    return "Project_{0}/image_{1}".format(instance.project.id, filename)


def client_logo(instance, filename):
    return "ClientLogos/{0}".format(filename)


def license_images(instance, filename):
    return "Licences/{0}".format(filename)


# Create your models here.
class Project(models.Model):
    title = models.CharField(
        "Title",
        help_text="Title of the project",
        max_length=64,
        null=False,
        blank=False,
    )
    cover_image = models.ImageField(
        "Cover Image",
        upload_to=project_cover,
        blank=False,
        null=False,
        help_text="Project cover image",
    )
    short_description = models.CharField(
        "Short Description",
        help_text="Example: Renovations and upgrades",
        max_length=32,
        blank=True,
        null=False,
        default="",
    )
    description = models.TextField(
        "Project Description",
        help_text="Overview of the project, written in markdown",
        blank=False,
        null=False,
    )
    details = models.TextField(
        "Project Details",
        help_text="Details about the project, including specifics",
        null=False,
        blank=False,
    )

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="images",
    )
    text = models.CharField(
        "Project Image Text",
        help_text="A title for the image",
        default="Project Image",
        max_length=32,
    )
    image = models.ImageField("Project Image", upload_to=project_image)


class Client(models.Model):
    client_image = models.ImageField("Client Logo", upload_to=client_logo)
    company = models.CharField(
        "Company Name",
        max_length=64,
        null=False,
        blank=False,
        default="",
        help_text="Name of company",
    )

    def __str__(self) -> str:
        return str(self.company)

    def __repr__(self) -> str:
        return self.company


class License(models.Model):
    license_image = models.ImageField("License Photo", upload_to=license_images)
    name = models.CharField(
        "License Title",
        max_length=64,
        null=False,
        blank=False,
        default="Solutions License",
        help_text="Title of license to be displayed",
    )

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class Message(models.Model):
    first_name = models.CharField("First Name", null=False, blank=False, max_length=32)
    last_name = models.CharField("Last Name", null=False, blank=False, max_length=32)
    company = models.CharField("Company", null=False, blank=False, max_length=32)
    email = models.EmailField("Email", blank=False, null=False)
    message = models.TextField("Message", max_length=200)

    def __str__(self) -> str:
        return "Message from{0} {1}".format(self.last_name, self.first_name)

    def __repr__(self) -> str:
        return "Message from{0} {1}".format(self.last_name, self.first_name)