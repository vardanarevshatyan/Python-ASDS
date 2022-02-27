class SpanishSpeaker:
    @staticmethod
    def order(text) -> str:
        print('Spanish speaker said: ', text)
        return text


class EnglishBarman:
    request_list = {'A cup of coffee, please.': 'Your coffee will be ready in 5 minutes, thank you for the order.',
                    'Do you have sushi?': 'We do not serve sushi.',
                    'Can I speak to your manager?': 'Our manager is out of office right now.'}

    @classmethod
    def get_the_order(cls, text):
        en_text = cls.request_list.get(text, 'Sorry, I did not quite understand.')
        print('Waiter replied: ', en_text)
        return text



class SpanishWaiter(SpanishSpeaker, EnglishBarman):
    @classmethod
    def get_the_order(cls, text):
        en_text = cls.request_list.get(cls.order(text), 'Sorry, I did not quite understand.')
        print('Waiter replied: ', en_text)
        return en_text


if __name__ == '__main__':
    spanish_client = SpanishSpeaker()
    waiter = EnglishBarman()
    spanish_sentence = spanish_client.order('A cup of coffee, please.')
    waiter.get_the_order(spanish_sentence)
