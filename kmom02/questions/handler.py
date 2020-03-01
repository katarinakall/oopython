#!/usr/bin/env python3
"""
Contains the handler/manager class for the questions.
"""
from questions import Question
from questions import CheckboxQuestion
from questions import RadiobuttonQuestion

class QuestionManager():
    """
    Manages all questions
    """
    max_score = 15

    def __init__(self):
        self._questions = questions
        self._points = 0
        self._quest_count = 0


    def get_score(self):
        """
        Returns the palyers score
        """
        return self._points

    def get_max_score(self):
        """
        Returns the maximum score
        """
        return self.max_score

    def has_next(self):
        """
        Controlls if question list has more questions returns a bool
        """
        return len(self._questions) > self._quest_count

    def get_next(self):
        """
        Returns next question from question list
        """
        question = self._questions[self._quest_count]
        return question

    def get_quest_count(self):
        """
        Returns the number of answerd questions
        """
        return self._quest_count

    def read_session(self, session):
        """
        Read current score and current quest number from session
        """
        self._points = session.get("points", 0)
        self._quest_count = session.get("quest_count", 0)

    def write_session(self, session):
        """
        Write current score and quest number to session
        """
        session["points"] = self._points
        session["quest_count"] = self._quest_count

    def reset(self):
        """
        Reset score and quest number to 0
        """
        self._quest_count = 0
        self._points = 0

    def correct_answer(self, form):
        """
        Checks if guessed answer is the correct answer
        """
        question = self._questions[self._quest_count]
        if question.get_type() == "checkbox":
            response = form.getlist("answer")
            for resp in response:
                if question.check_answer(resp):
                    self._points += 1
        else:
            response = form["answer"]
            if question.check_answer(response):
                self._points += 1

        self._quest_count += 1

q1 = Question("djungelboken",\
 "Vad heter den animerade filmen från 1967 som handlar om Mowgli?")
q2 = Question("merkurius", "Vilken planet ligger närmast solen?")
q3 = Question("vänster", \
"Springer älgen, på Vägverkets varningsskylt för älg, åt vänster eller höger?")
q4 = CheckboxQuestion(["K2", "Mount Everest", "Kanchenjunga"], \
"Vilka av följande berg är världens 3 högsta?", \
["K2", "Lhotse", "Mount Everest", "Makalu", "Kanchenjunga", "Cho Oyu"])
q5 = CheckboxQuestion(["Kanel", "Ingefära", "Nejlika"], \
"Vilka kryddor använder man när man bakar pepparkakor?", \
["Peppar", "Kardemumma", "Kanel", "Ingefära", "Nejlika", "Vanilj"])
q6 = CheckboxQuestion(["Maja", "Alice", "Julia"], \
"Vilka var de tre mest populära flicknamnen under 2010?", \
["Julia", "Maja", "Lisa", "Johanna", "Alicia", "Alice"])
q7 = RadiobuttonQuestion("narkos", \
 "2019 godkändes ett nytt antidepressivt läkemedel. Vad har det använts vid \
 tidigare?", ["Narkos", "Kejsarsnitt", "Benbrott"])
q8 = RadiobuttonQuestion("alexander flemming", \
 "Vad heter bakteriologen från Skottland som upptäckte penicillinet?", \
 ["Allan Flemming", "Alexander Flemming", "Anders Flemming"])
q9 = RadiobuttonQuestion("gorillan", \
"Vilken är den största av människoaporna?", \
["Schimpansen", "Orangutangen", "Gorillan"])
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9]
