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

#задание7
american_date = "05.17.2016"
month = int(american_date[:2])
day = int(american_date[3:5])
year = int(american_date[6:])
european_date = "{}.{}.{}".format(day, month, year)
print(american_date)
print(european_date)

#задание9
snake_case = "employee_first_name"
new = snake_case.split("_")
camelcase = new[0].capitalize()+new[1].capitalize()+new[2].capitalize()
print(snake_case)
print(camelcase)

#задание10
writer = "Leo Tolstoy*1828-08-28*1910-11-20"
#writer = "Marcus Aurelius*121-04-26*180-03-17"
name, DOB, DOD = writer.split("*")
DOB1 = DOB.split("-")
DOD1 = DOD.split("-")
age = int(DOD1[0])-int(DOB1[0])
print(name,",", age)








