from django.db import models
from .InspirationBaseModelMixin import InspirationBaseModelMixIn

class BookKeywords(models.Model, InspirationBaseModelMixIn):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    word = models.CharField(max_length=50)
    count = models.IntegerField(default=0)
    list_of_insights = models.TextField()

    def __str__(self):
        return "<BookKeywords - %s - %d>" % (self.word, self.count)

    @classmethod
    def search(cls, book, **kwargs):

        book_keyword = BookKeywords.objects.filter(book=book)

        keyword_map = dict()

        # TODO - help me do this as a one liner
        for keyword in book_keyword:
            keyword_map[keyword.word] = keyword

        return keyword_map