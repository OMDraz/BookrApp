from django.db import models

class Publisher(models.Model):
    """
    This is a model class governs and defines what we call a publisher - a company that releases books
    Helpful tips:
    help_text = Add descriptive text for a field to be auto-included in forms
    max_length = Defines max length of a field in terms of no. of characters
    """
    name = models.CharField(max_length=50, help_text='The name of the publisher')
    website = models.URLField(help_text='The publisher\'s website')
    email = models.EmailField(help_text="The publisher's email address.")

class Book(models.Model):
    """
    A model class for every book
    """
    title = models.CharField(max_length=70, help_text="The title of the book.")
    publication_date = models.DateField(verbose_name="Date the book was published")
    isbn = models.CharField(max_length=20, verbose_name="ISBN number of the book.")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through='BookContributor')
class Contributor(models.Model):
    """
    A model class for contributors to a book, e.g author, editors, co-authors, etc.
    """
    first_names = models.CharField(max_length=50, help_text="The contributor's first name / names")
    last_names = models.CharField(max_length=50, help_text="The contributor's last name / names")
    email = models.EmailField(help_text="The Contributor's email address.")

class BookContributor(models.Model):

    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this contributor had in the book.", choices=ContributionRole.choices, max_length=20)