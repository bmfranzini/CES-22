
def fn_decorate(func):
    def wrapper(*args, **kwargs):
        return "<p>{0}<\p>".format(func(*args, **kwargs))
    return wrapper


@fn_decorate
def restaurant(*args, **kwargs):
    cost = 0
    for arg in args:
        cost += kwargs[arg]
    return "The total order cost is " + str(cost)


print(restaurant("BigMac", "Cheeseburger", "FrenchFries", "Coke", BigMac= 7, Cheeseburger= 1, FrenchFries= 3, Coke= 2, BigTasty= 8, MilkShake= 5))

