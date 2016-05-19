from rest_framework.response import Response
from inspiration.models import WordToIgnore
import string

class Learning ():

    @classmethod
    def parse_lesson(self, lesson):

        list_of_words_to_ignore = WordToIgnore.objects.all()
        parsed_list = []
        split_list = lesson.split()

        remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
        split_list = [s.translate(remove_punctuation_map) for s in split_list]

        for word in split_list:
            word = word.translate(string.punctuation)

        # This might need a better way later
        dict_of_words_to_ignore = {list_of_words_to_ignore[i]: 1 for i in range(len(list_of_words_to_ignore))}

        # someone tell me if there is a better way to write this
        for word in split_list:
            word_lc = word.lower()
            if word_lc not in dict_of_words_to_ignore:
                parsed_list.append(word_lc)

        return parsed_list


    @classmethod
    def respond_learned(cls, model, insight):

        return Response(status=200, data="[200] %s was {learned} about this %s"%(insight, model))

    @classmethod
    def respond_issues_with_learning(cls):

        return Response(status=400)