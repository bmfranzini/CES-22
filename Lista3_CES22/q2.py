
def fn_decorate(func):
    def wrapper(*args, **kwargs):
        return "{0}".format(func(*args, **kwargs))
    return wrapper


class Person(object):
    def __init__(self):
        self.name = "Bruno"
        self.family = "Franzini"

    @fn_decorate
    def get_fullname(self):
        return self.name+" is from "+self.family +"'s family"


me = Person()

print(me.get_fullname())