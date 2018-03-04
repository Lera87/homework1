name="Mark"
surname="Zuckerberg"
print("{} {}".format(name, surname))
#меняем местами имя и фамилию
print("{} {}".format(surname, name))

person_name = "Mark Zuckerberg"
name, surname = person_name.split(" ")
new_person_name = "{} {}".format(surname, name)
print(person_name)
print(new_person_name)
