class EnglishSpeaker:
    """Something in English. This is the target class."""
    @staticmethod
    def order(text) -> str:
        print('English speaker said: ', text)
        return text


class SpanishSpeaker:
    """Something in Spanish. This is the Adaptee."""
    @staticmethod
    def spanish_order(text) -> str:
        print('Spanish speaker said: ', text)
        return text


class EnglishBarman:
    """This is the client class working with the target. """
    request_list = {'A cup of coffee, please.': 'Your coffee will be ready in 5 minutes, thank you for the order.',
                    'Do you have sushi?': 'We do not serve sushi.',
                    'Can I speak to your manager?': 'Our manager is out of office right now.'}

    @classmethod
    def get_the_order(cls, text):
        en_text = cls.request_list.get(text, 'Sorry, I did not quite understand.')
        print('Barman replied: ', en_text)
        return text


class TranslatorFriend(SpanishSpeaker, EnglishSpeaker):
    translations = {'Una taza de café por favor.': 'A cup of coffee, please.',
                    '¿Tienes sushi?': 'Do you have sushi?',
                    '¿Puedo hablar con su gerente?': 'Can I speak to your manager?'}

    """Translator speaks Spanish and acts as the Adapter."""
    @classmethod
    def order(cls, text):
        en_text = cls.translations.get(text, 'I cannot translate that.')
        print('Translator translated to barman: ', en_text)
        return en_text


if __name__ == '__main__':
    english_client = EnglishSpeaker()
    spanish_client = SpanishSpeaker()
    barman = EnglishBarman()
    translator = TranslatorFriend()
    print(10*'*', 'Client communicates with the target.', 10*'*')
    english_order = english_client.order('A cup of coffee, please.')
    barman.get_the_order(english_order)
    print(50*'*', '\n')
    print(10*'*', 'Client and Adaptee cannot communicate.', 10*'*')
    sp_order = spanish_client.spanish_order('¿Tienes sushi?')
    barman.get_the_order(sp_order)
    print(50 * '*', '\n')
    print(10*'*', 'Adapter saves the situation.', 10*'*')
    translated_order = translator.order(sp_order)
    barman.get_the_order(translated_order)
    print(50 * '*', '\n')