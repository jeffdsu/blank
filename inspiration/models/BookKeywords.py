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
    def search(cls, book, *search, **kwargs):

        search_build = BookKeywords.objects.filter(book=book, *search)


        if 'style' in kwargs:
            import re
            m = re.search('^top_(\d+)', kwargs['style'])

            if m.group(1) is not None:
                current_search_len = len(search_build)
                top_x = int(m.group(1))

                top_x = current_search_len if top_x > current_search_len else top_x

                search_build = BookKeywords.objects.filter(book=book, *search).order_by('-count')[:top_x]

                print(search_build.query)

                return search_build

        if 'format' in kwargs and kwargs['format'] is dict:

            keyword_map = dict()

            # TODO - help me do this as a one liner
            for keyword in search_build:
                keyword_map[keyword.word] = keyword

            return keyword_map

        return search_build