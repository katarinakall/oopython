"""
Contains all classes for the different types of questions
"""
class Question():
    """
    Question class
    """
    type = "text"

    def __init__(self, answer, text):
        """
        Inits question object
        """
        self._answer = answer
        self._text = text

    @classmethod
    def get_type(cls):
        """
        Returns the type of the question
        """
        return cls.type

    def get_text(self):
        """
        Returns the text
        """
        return self._text

    def check_answer(self, respons):
        """
        Controlls if answer is correct and returns a bool
        """
        respons = respons.lower()
        return self._answer == respons

class RadiobuttonQuestion(Question):
    """
    Radiobutton question class
    """
    type = "radiobutton"

    def __init__(self, answer, text, alternatives):
        """
        Inits radiobutton question object
        """
        super(RadiobuttonQuestion, self).__init__(answer, text)
        self._alternatives = alternatives

    def get_alternatives(self):
        """
        Returns alternatives
        """
        return self._alternatives

class CheckboxQuestion(Question):
    """
    Checkbox question class
    """
    type = "checkbox"

    def __init__(self, answer, text, alternatives):
        """
        Inits checkbox question object
        """
        super(CheckboxQuestion, self).__init__(answer, text)
        self._alternatives = alternatives

    def get_alternatives(self):
        """
        Returns alternatives
        """
        return self._alternatives

    def check_answer(self, respons):
        """
        Controlls if answer is correct and returns a bool
        """
        return respons in self._answer
