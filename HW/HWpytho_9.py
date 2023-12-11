import re

s = "\tPhone: +7 (948) 106 12 34.\n\
    Phone: +79481061234. \n\
    Phone: +7 948 106 12 34.\n\
    Phone: +7 (948) 106-12-34.\n\
    Phone: +7 (948) 1061234.\n\
    Phone: 8 (948) 106 12 34.\n\
    Phone: 89481061234.\n\
    Phone: 8(948)1061234.\n\
    Phone: +380713061234.\n\
    Phone:+446661061234\n\
    Not a Phone: +4466610612\n\
    Not a Phone: +44-666-106-12-34\n\
    Not a Phone: 4402 6661 0612 3400\n\
    Not a Phone: 666-10-12\n\
    Not a Phone: +44 (6661) 061 234\n\
    Not a Phone: +44 6661 061234\n"

# создает объект регулярного выражения
p = re.compile(r"^\s*Phone:\s*[+\d\s()-]+", re.MULTILINE)
# Проходим по циклу для поиска всех непересекающихся соответствий регулярного выражения в тексте.
for m in re.finditer(p, s):
    print("%s" % (m.group(0)))
