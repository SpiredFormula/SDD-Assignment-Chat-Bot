from Avatar import Avatar
import json


class Menu:


    def __init__(self):
        
        self.loadMenu()
        self.waiter = Avatar()

    def loadMenu(self):
        try:
            with open("Menu.json") as m:
                data = m.read()
                self.menu = json.loads(data)
                
        except:
            self.menu = {"snack": {"popcorn": 5.00}}
            print(self.menu)



    def showCourse(self, course):
        print(f"Course: {course.title()} test")
        self.waiter.say(f"The dishes for the {course} course are.")


    def showDishes(self, course):

        dishes = self.menu[course]

        for dish in dishes:
            price = dishes[dish]

            desc = f"{dish.title():10s} ${price:3.2f}"
            print(desc)
            self.waiter.say(desc)


    def showMenu(self, menuCourse=None):
        print("---- Menu ----")
        self.waiter.say("The following is the Menu")


        if menuCourse:
            self.showCourse(menuCourse)
            self.showDishes(menuCourse)
        else:
            for course in self.menu:
                self.showCourse(course)
                self.showDishes(course)


def main():
    m = Menu()
    m.showMenu()
    m.showMenu("starter")


if __name__ == "__main__":
    main()
