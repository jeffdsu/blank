from .Learning import Learning
from inspiration.models import Book
from inspiration.models import BookKeywords
import ast



class BookLearning(Learning):

    @classmethod
    def learn (cls, book, insight, **kwargs):

        try:
            # TODO - if debug mode:
            import inspect
            function = inspect.stack()[0][3]

            list_of_found_words = cls.parse_lesson(insight.lesson)
            kwargs['format'] = dict
            book_known_keywords = BookKeywords().search(book, **kwargs)

            #  TODO - make this print out only in debug mode later
            print(list_of_found_words)
            print(book_known_keywords)

            new_book_keywords = []
            known_book_keywords = []

            # TODO - probably move this to something else later
            for found_word in list_of_found_words:
                if found_word not in book_known_keywords:

                    #TODO - make this a debug statement:
                    print("{%s} new word! %s"%(function, found_word))

                    new_book_keywords.append(cls.gen_keyword(found_word, book, insight))

                else:
                    known_keyword = book_known_keywords[found_word]

                    known_book_keywords.append(cls.analyze_known_key_word(known_keyword, insight))
                    print("{%s} known word! %s" % (function, found_word))


            cls.save_new(new_book_keywords)
            cls.analyze(known_book_keywords)

            return cls.respond_learned(book, insight)
        except:
            return cls.respond_issues_with_learning()

    @classmethod
    def analyze(cls, known_book_keywords):
        try:
            for book_keyword in known_book_keywords:
                print("here!")
                book_keyword.save()
        except:
            return cls.respond_issues_with_learning()

    @classmethod
    def analyze_known_key_word(cls, known_keyword, insight):

        known_keyword.count += 1
        list_of_insights = ast.literal_eval(known_keyword.list_of_insights)
        list_of_insights.append(insight.id)

        known_keyword.list_of_insights = str(list_of_insights)

        return known_keyword

    @classmethod
    def gen_keyword(cls, found_word, book, insight):

        try:
            book_keyword_dict = dict()
            book_keyword_dict['word'] = found_word
            book_keyword_dict['book'] = book

            temp_insight_list = []
            temp_insight_list.append(insight.id)
            book_keyword_dict['list_of_insights'] = str(temp_insight_list)
        except:
            # should return response
            return

    @classmethod
    def save_new(cls, new_book_keywords):
        try:
            for book_keyword in new_book_keywords:
                book_keyword.save()
        except:
            return cls.respond_issues_with_learning()
