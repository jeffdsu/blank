from django.db import models
from django.contrib.auth.models import User


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

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return "%s - %s" % (str(self.book), str(self.user))

class Insight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.TextField()
    checkout = models.ForeignKey(Checkout, null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    valid = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % (str(self.lesson_learned))

class InsightKeywords(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    word = models.CharField(max_length=50)
    count = models.IntegerField(default=0)

    def __str__(self):
        return "%s - %d" % (self.word, self.count)

class WordsToIgnore(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return "%s" % (self.word)
