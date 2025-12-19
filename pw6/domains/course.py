class Course:
    def __init__(self, cid="", name="", credit=1):
        self.__id = cid
        self.__name = name
        self.__credit = credit

    def input(self):
        self.__id = input("Course ID: ")
        self.__name = input("Course name: ")
        self.__credit = int(input("Credit: "))

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credit(self):
        return self.__credit

    def show(self):
        print(
            f"ID: {self.__id}, "
            f"Name: {self.__name}, "
            f"Credit: {self.__credit}"
        )
