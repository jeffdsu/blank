from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Book(models.Model):
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    pub_date = models.DateField()
    summary = models.TextField()
    cover_url = models.CharField(max_length=255)

    def __str__(self):
        return "%s - %s" % (self.title, str(self.author))
