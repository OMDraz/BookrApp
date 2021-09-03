from django.db import models
from django.contrib import auth

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

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    A model class for every book
    """
    title = models.CharField(max_length=70, help_text="The title of the book.")
    publication_date = models.DateField(verbose_name="Date the book was published")
    isbn = models.CharField(max_length=20, verbose_name="ISBN number of the book.")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through='BookContributor')

    def __str__(self):
        return self.title

class Contributor(models.Model):
    """
    A model class for contributors to a book, e.g author, editors, co-authors, etc.
    """
    first_names = models.CharField(max_length=50, help_text="The contributor's first name / names")
    last_names = models.CharField(max_length=50, help_text="The contributor's last name / names")
    email = models.EmailField(help_text="The Contributor's email address.")

    def initialled_name(self):
        """
        self.first_names = 'Jerome David'
        self.last_names = 'Salinger'
        => 'Salinger, JD'
        """
        initials = ''.join([name[0] for name in self.first_names.split(' ')])
        return "{}, {}".format(self.last_names, initials)

    def __str__(self):
        return self.initialled_name()

class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this contributor had in the book.", choices=ContributionRole.choices, max_length=20)

class Review(models.Model):
    content = models.TextField(help_text="The Review Text.")
    rating = models.IntegerField(help_text="The rating the reviewer has given")
    date_created = models.DateTimeField(auto_now_add=True, help_text="The date and time the review was created")
    date_edited = models.DateTimeField(null=True, help_text="The date and time the review was last edited.")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="The Book that this review is for.")

    def __str__(self):
        return "{} ({} - rating {})".format(self.creator, self.book, self.rating)

