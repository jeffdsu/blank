from .Learning import Learning
from inspiration.models import Medium
from inspiration.models import Keyword
import ast



class MediumLearning(Learning):

    @classmethod
    def learn (cls, medium, insight, words_to_ignore_dict, **kwargs):

        try:
            # TODO - if debug mode:
            import inspect
            function = inspect.stack()[0][3]

            list_of_found_words = cls.parse_lesson(insight.lesson)
            kwargs['format'] = dict
            medium_known_keywords = Keyword().search(medium, **kwargs)

            #  TODO - make this print out only in debug mode later
            print(list_of_found_words)
            print(medium_known_keywords)

            new_medium_keywords = []
            known_medium_keywords = []

            # TODO - probably move this to something else later
            for found_word in list_of_found_words:
                if found_word not in medium_known_keywords:

                    if found_word not in words_to_ignore_dict:
                        #TODO - make this a debug statement:
                        print("{%s} new word! %s"%(function, found_word))

                        new_medium_keywords.append(cls.gen_keyword(found_word, medium, insight))
                    else:
                        print("{%s} new word but ignored! %s" % (function, found_word))

                else:
                    known_keyword = medium_known_keywords[found_word]
                    print(known_keyword)
                    known_medium_keywords.append(cls.analyze_known_key_word(known_keyword, insight))
                    print("{%s} known word! %s" % (function, found_word))

            cls.save_new(new_medium_keywords)
            cls.analyze(known_medium_keywords)

            return cls.respond_learned(medium, insight)
        except Exception as e :
            print(e)
            return cls.respond_issues_with_learning()

    @classmethod
    def analyze(cls, known_medium_keywords):
        try:
            for medium_keyword in known_medium_keywords:
                print("here!")
                medium_keyword.save()
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
    def gen_keyword(cls, found_word, medium, insight):

        try:
            medium_keyword_dict = dict()
            medium_keyword_dict['word'] = found_word
            medium_keyword_dict['medium'] = medium

            temp_insight_list = []
            temp_insight_list.append(insight.id)
            medium_keyword_dict['list_of_insights'] = str(temp_insight_list)
            return Keyword(**medium_keyword_dict)

        except Exception as e:
            print(e)
            return

    @classmethod
    def save_new(cls, new_medium_keywords):
        try:
            for medium_keyword in new_medium_keywords:
                medium_keyword.save()
        except:
            return cls.respond_issues_with_learning()
