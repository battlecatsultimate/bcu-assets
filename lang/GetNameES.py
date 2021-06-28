import codecs
import os
import unicodedata
import json


def numbers(n):
    if 0 <= n <= 9:
        return "00" + str(n)
    elif 10 <= n <= 99:
        return "0" + str(n)
    elif 100 <= n <= 999:
        return str(n)


def clean(message):
    return "".join(ch for ch in message if unicodedata.category(ch)[0] != "C")


def getfiledirect(name):
    script_dir = os.path.dirname(__file__)
    rel_path = "resLocal_es/"

    return os.path.join(script_dir, rel_path + name)


def getdatafile(name):
    script_dir = os.path.dirname(__file__)
    rel_path = "DataLocal/"

    return os.path.join(script_dir, rel_path + name)


def getcombodata():
    script_dir = os.path.dirname(__file__)
    rel_path = "DataLocal/NyancomboData.csv"

    return os.path.join(script_dir, rel_path)


def getnumber():
    n = 1

    stacker = 0

    while 1:
        try:
            with codecs.open(getfiledirect('Unit_Explanation%s_es.csv' % n), 'r', encoding='utf-8') as f:
                stacker = 0

            n = n + 1
        except:
            stacker = stacker + 1
            n = n + 1

            if stacker == 5:
                return n - 5


print("Initializing Files...\n")

FILES = ["es-UnitExplanation.txt", "es-UnitName.txt", "es-EnemyName.txt", "es-EnemyExplanation.txt",
         "es-CatFruitExplanation.txt", "es-MedalName.txt", "es-MedalExplanation.txt", "es-RewardName.txt", "es-ComboName.txt"]
TYPE = ["Attack Up", "Defense Up"]
TRAIT = ["Red", "Float", "Black", "Metal", "Angel", "Alien", "Zombie"]
GRADE = ["D", "C", "B", "A", "S"]

for n in range(0, len(FILES)):
    with codecs.open(FILES[n], 'w', encoding='utf-8') as f:
        f.write("")

print("Writing Unit Name Files...\n")

for n in range(1, getnumber()):
    try:
        with codecs.open(getfiledirect('Unit_Explanation%s_es.csv' % n), 'r', encoding='utf-8') as f:
            unitex = f.read()

        wait = unitex.split("\n")

        if len(wait) == 1:

            lit = unitex.split("|")

            if lit[0] != "":
                if lit[0].startswith(numbers(n)):
                    with codecs.open('es-UnitName.txt', 'a', encoding='utf-8') as g:
                        g.write("%s\t\t\t\r\n" % numbers(n - 1))
                else:
                    if lit[4] == lit[8]:
                        with codecs.open('es-UnitName.txt', 'a', encoding='utf-8') as g:
                            g.write("%s\t%s\t%s\t\r\n" %
                                    (numbers(n - 1), lit[0].strip(), lit[4].strip()))
                    else:
                        with codecs.open('es-UnitName.txt', 'a', encoding='utf-8') as g:
                            g.write("%s\t%s\t%s\t%s\r\n" %
                                    (numbers(n - 1), lit[0].strip(), lit[4].strip(), lit[8].strip()))
            else:
                with codecs.open('es-UnitName.txt', 'a', encoding='utf-8') as g:
                    g.write("%s\t\t\t\r\n" % numbers(n - 1))

        elif len(wait) >= 3:
            names = []

            for m in range(0, 3):
                lit = wait[m].split("|")

                names.append(lit[0].strip())

            if names[0] != "":
                if names[0].startswith(numbers(n)):
                    with codecs.open('es-UnitName.txt', 'a', encoding='utf-8') as g:
                        g.write("%s\t\t\t\r\n" % numbers(n - 1))
                else:
                    if names[1] == names[2]:
                        with codecs.open('es-UnitName.txt', 'a', encoding='utf-8') as g:
                            g.write("%s\t%s\t%s\t\r\n" % (numbers(n - 1), names[0], names[1]))
                    else:
                        with codecs.open('es-UnitName.txt', 'a', encoding='utf-8') as g:
                            g.write("%s\t%s\t%s\t%s\r\n" %
                                    (numbers(n - 1), names[0], names[1], names[2]))
            else:
                with codecs.open('es-UnitName.txt', 'a', encoding='utf-8') as g:
                    g.write("%s\t\t\t\r\n" % numbers(n - 1))

        else:
            with codecs.open('es-UnitName.txt', 'a', encoding='utf-8') as g:
                g.write("%s\t\t\t\r\n" % numbers(n - 1))
    except:
        print("Unknown Unit number found : %s\n" % n)
        with codecs.open('es-UnitName.txt', 'a', encoding='utf-8') as g:
            g.write("%s\t\t\t\r\n" % numbers(n - 1))

print("Writing Unit Explanation Files...\n")

for n in range(1, getnumber()):
    names = []

    try:
        with codecs.open(getfiledirect('Unit_Explanation%s_es.csv' % n), 'r', encoding='utf-8') as f:
            unitex = f.read()

        wait = unitex.split("\n")

        if len(wait) == 1:

            lit = unitex.split("|")

            if lit[0] != "":
                if lit[1].startswith("仮1") or lit[1].strip() == "":
                    with codecs.open('es-UnitExplanation.txt', 'a', encoding='utf-8') as g:
                        g.write("%s\t\t\t\r\n" % numbers(n - 1))
                else:
                    unitf = lit[1].strip() + "<br>" + lit[2].strip() + "<br>" + lit[3].strip()
                    unitc = lit[5].strip() + "<br>" + lit[6].strip() + "<br>" + lit[7].strip()
                    units = lit[9].strip() + "<br>" + lit[10].strip() + "<br>" + lit[11].strip()

                    if unitc == units:
                        with codecs.open('es-UnitExplanation.txt', 'a', encoding='utf-8') as g:
                            g.write("%s\t%s\t%s\t\r\n" % (numbers(n - 1), unitf, unitc))
                    else:
                        with codecs.open('es-UnitExplanation.txt', 'a', encoding='utf-8') as g:
                            g.write("%s\t%s\t%s\t%s\r\n" % (numbers(n - 1), unitf, unitc, units))
            else:
                with codecs.open('es-UnitExplanation.txt', 'a', encoding='utf-8') as g:
                    g.write("%s\t\t\t\r\n" % numbers(n - 1))

        elif len(wait) >= 3:
            unit = []

            for m in range(0, 3):
                lit = wait[m].split("|")

                if lit[1] != "":
                    if lit[1].startswith("仮1") or lit[1].strip() == "":
                        names.append("")
                    else:
                        names.append(lit[1].strip() + "<br>" + lit[2].strip() + "<br>" + lit[3].strip())

            if len(names) == 0:
                names = [""]

            if names[0] != "":
                if len(names) == 2:
                    with codecs.open('es-UnitExplanation.txt', 'a', encoding='utf-8') as g:
                        g.write("%s\t%s\t%s\t\r\n" % (numbers(n - 1), names[0], names[1]))
                elif len(names) == 3:
                    if names[1] == names[2]:
                        with codecs.open('es-UnitExplanation.txt', 'a', encoding='utf-8') as g:
                            g.write("%s\t%s\t%s\t\r\n" % (numbers(n - 1), names[0], names[1]))
                    else:
                        with codecs.open('es-UnitExplanation.txt', 'a', encoding='utf-8') as g:
                            g.write("%s\t%s\t%s\t%s\r\n" %
                                    (numbers(n - 1), names[0], names[1], names[2]))
                else:
                    print("Wrong Found at : %s" % (n - 1))
                    with codecs.open('es-UnitExplanation.txt', 'a', encoding='utf-8') as g:
                        g.write("%s\t\t\t\r\n" % numbers(n - 1))
            else:
                with codecs.open('es-UnitExplanation.txt', 'a', encoding='utf-8') as g:
                    g.write("%s\t\t\t\r\n" % numbers(n - 1))

        else:
            with codecs.open('es-UnitExplanation.txt', 'a', encoding='utf-8') as g:
                g.write("%s\t\t\t\r\n" % numbers(n - 1))
    except:
        print("Unknown Unit number found : %s\n" % n)
        with codecs.open('es-UnitExplanation.txt', 'a', encoding='utf-8') as g:
            g.write("%s\t\t\t\r\n" % numbers(n - 1))

print("Writing Enemy Name Files...\n")

with codecs.open(getfiledirect('Enemyname.tsv'), 'r', encoding='utf-8') as f:
    enemyex = f.read()

lit = enemyex.split("\n")

for n in range(0, len(lit)):
    wait = lit[n].strip()

    if wait != "" and wait != 'ダミー':
        with codecs.open('es-EnemyName.txt', 'a', encoding='utf-8') as g:
            g.write("%s\t%s\r\n" % (numbers(n), wait))
    else:
        with codecs.open('es-EnemyName.txt', 'a', encoding='utf-8') as g:
            g.write("%s\t\r\n" % (numbers(n)))

print("Writing Enemy Explantion Files...\n")

with codecs.open(getfiledirect('EnemyPictureBook_es.csv'), 'r', encoding='utf-8') as f:
    enemyex = f.read()

lit = enemyex.split("\n")

for n in range(0, len(lit)):
    wait = lit[n].split("|")

    if wait[0] != "" and wait[0] != '【ダミー】' and len(wait) >= 4:
        if wait[1].startswith("仮1"):
            with codecs.open('es-EnemyExplanation.txt', 'a', encoding='utf-8') as g:
                g.write("%s\t\r\n" % (numbers(n)))
            continue

        explanation = wait[1] + "<br>" + wait[2] + "<br>" + wait[3] + "<br>" + wait[4]

        with codecs.open('es-EnemyExplanation.txt', 'a', encoding='utf-8') as g:
            g.write("%s\t%s\r\n" % (numbers(n), explanation))
    else:
        with codecs.open('es-EnemyExplanation.txt', 'a', encoding='utf-8') as g:
            g.write("%s\t\r\n" % (numbers(n)))

print("Writing Cat Fruit Explanation Files...\n")

with codecs.open(getfiledirect('unitevolve_es.csv'), 'r', encoding='utf-8') as f:
    unitcf = f.read()

lit = unitcf.split("\n")

for n in range(0, getnumber() - 1):
    wait = lit[n].split("|")

    desc = numbers(n) + "\t"

    for m in range(0, 3):
        if wait[m] == "＠":
            if m == 2:
                desc = desc + "\n"
            else:
                desc = desc + "<br>"
        else:
            if m == 2:
                desc = desc + wait[m] + "\n"
            else:
                desc = desc + wait[m] + "<br>"
    with codecs.open('es-CatFruitExplanation.txt', 'a', encoding='utf-8') as g:
        g.write(desc)

print("Writing Cat Combo Name Files...\n")

with codecs.open(getfiledirect('Nyancombo_es.csv'), 'r', 'utf-8') as f:
    combo = f.read()

with codecs.open(getcombodata(), 'r', 'utf-8') as f:
    combod = f.read()

lit = combo.split("\n")
litd = combod.split("\n")

for n in range(0, len(lit)):
    names = lit[n].split("|")
    named = litd[n].split(",")

    if int(named[1]) == -1:
        continue

    if len(names) <= 1:
        continue

    if len(litd) <= 5:
        continue

    if names[0] == "":
        continue

    try:
        int(named[0])
    except:
        continue

    with codecs.open('es-ComboName.txt', 'a', 'utf-8') as g:
        g.write(named[0] + "\t" + names[0] + "\n")

print("Writing Medal Name Files...\n")

with codecs.open(getfiledirect('medalname.tsv'), 'r', 'utf-8') as f:
    med = f.read().strip().split("\n")

for n in range(0, len(med)):
    wait = med[n].strip().split("\t")

    if len(wait) < 2:
        continue

    name = wait[0]

    with codecs.open('es-MedalName.txt', 'a', 'utf-8') as g:
        g.write("%s\t%s\n" % (n, name))

print("Writing Medal Explanation Files...\n")

for n in range(0, len(med)):
    wait = med[n].strip().split("\t")

    if len(wait) < 2:
        continue

    desc = wait[1]

    with codecs.open('es-MedalExplanation.txt', 'a', 'utf-8') as g:
        g.write("%s\t%s\n" % (n, desc))

ITEM = ['Speed Up', 'Treasure Radar', 'Rich Cat', 'Cat CPU', 'Cat Jobs',
        'Sniper The Cat', 'XP', 'Silver Ticket', 'Gold Ticket', 'Cat food']
INTEGER = [0, 1, 2, 3, 4, 5, 6, 11, 12, 13]
EXCEPT = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 79, 80, 81, 82, 83, 84, 123]

print("Writing Reward Name Files...")

with codecs.open(getfiledirect('GatyaitemName.csv'), 'r', 'utf-8') as f:
    item = f.read().strip().split("\n")

with codecs.open('es-UnitName.txt', 'r', 'utf-8') as f:
    units = f.read().strip().split("\n")

with codecs.open(getdatafile('drop_chara.csv'), 'r', 'utf-8') as f:
    drops = f.read().strip().split("\n")

with codecs.open(getdatafile('unitbuy.csv'), 'r', 'utf-8') as f:
    forms = f.read().strip().split("\n")

for n in range(0, len(ITEM)):
    with codecs.open('es-RewardName.txt', 'a', 'utf-8') as f:
        f.write("%s\t%s\n" % (INTEGER[n], ITEM[n]))

for n in range(0, len(item)):
    if n in EXCEPT or n < 23:
        continue

    it = clean(item[n]).strip().split("|")[0]

    if it == "":
        continue

    if it == "Lucky Ticket G":
        it = "G Ticket"

    with codecs.open('es-RewardName.txt', 'a', 'utf-8') as f:
        f.write("%s\t%s\n" % (n, it))

for n in range(1, len(drops)):
    wait = clean(drops[n]).strip().split(",")

    if wait[0] == '-1':
        continue

    if len(wait) <= 1:
        continue

    if (int(clean(wait[2])) >= len(units)):
        continue

    sp = units[int(clean(wait[2]))].split("\t")

    if(len(sp) < 2):
        continue

    name = sp[1].strip()

    if name == "":
        continue

    with codecs.open('es-RewardName.txt', 'a', 'utf-8') as f:
        f.write("%s\t%s\n" % (wait[0], name))

for n in range(0, len(forms)):
    wait = clean(forms[n]).strip().split(",")

    if len(wait) < 23:
        continue

    if n >= len(units):
        continue

    unit = units[n].strip().split("\t")

    if len(unit) < 4:
        continue

    name = unit[3].strip()

    if name == "":
        continue

    if int(wait[23]) < 10000:
        continue

    with codecs.open('es-RewardName.txt', 'a', 'utf-8') as f:
        f.write("%s\t%s\n" % (wait[23], name))

with codecs.open(getdatafile("equipmentlist.json"), 'r', 'utf-8') as f:
    equip = json.load(f)

for n in range(0, len(equip["ID"])):
    data = equip["ID"][n]
    g = int(data["gradeID"])
    c = int(data["content"])
    a = int(data["attribute"])

    if c >= len(TYPE):
        print("New type : ", c)
        continue

    if a >= len(TRAIT):
        print("New trait : ", a)
        continue

    if g >= len(GRADE):
        print("New grade : ", g)
        continue

    with codecs.open('es-RewardName.txt', 'a', 'utf-8') as f:
        f.write("%s\t%s %s: %s\n" % (30000 + n, TYPE[c], GRADE[g], TRAIT[a]))
