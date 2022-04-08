import abc


class University(object):
    _metaclass_ = abc.ABCMeta

    @abc.abstractmethod
    def get_localization(self):
        """Returns the city of the university"""

    @staticmethod
    def get_computer_engineering():     # both universities has this course
        return "ITA and IME has the computer engineering course"

    @classmethod
    def military_institute(cls):
        return "ITA and IME are military institutes"


class ITA(University):
    def get_localization(self):
        return "São José dos Campos"

    def get_aeronautics_engineering(self):    # instance method
        return "Only ITA has aeronautic engineering course"


class IME(University):
    def get_localization(self):
        return "Rio de Janeiro"



ita = ITA()
ime = IME()

print(ita.get_localization())
print(ime.get_localization())

print(ita.get_computer_engineering())
print(ime.get_computer_engineering())

print(ita.get_aeronautics_engineering())
