class PersonPrinter:

    people = []

    def __init__(self, people):
        self.people = people

   # def run(self):
   #     i = 0
   #     while i < len (self.people):
   #         person = self.people[i]
   #         print (f"{person.get_full_name()} {person.sex}")
   #         i = i + 1

    def run(self):
        for person in self.people:
            print(f"{person.get_full_name()} ({person.sex})")