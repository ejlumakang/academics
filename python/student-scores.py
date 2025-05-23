def average(name, Math, Science, English):
    x = (Math + Science + English) / 3
    print("{}'s grade (Math = {}, Science = {}, English = {}) and the average is {:.2f}.".format(name, Math, Science, English, x))


average("John", 95, 90, 80)
average("Ana", 70, 80, 90)
average("Frank", 78, 99, 100)