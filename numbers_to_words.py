s1 = ["ნული","ერთი","ორი","სამი","ოთხი","ხუთი","ექვსი","შვიდი","რვა","ცხრა","ათი"]
s2 = ["თერთმეტი","თორმეტი","ცამეტი","თოთხმეტი","თხუთმეტი","თექვსმეტი","ჩვიდმეტი","თვრამეტი","ცხრამეტი"]
s3 = ["ორ","სამ","ოთხ","ხუთ","ექვს","შვიდ","რვა","ცხრა"]
s4 = ["ათი","ოცი","ოცდაათი","ორმოცი","ორმოცდაათი","სამოცი","სამოცდაათი","ოთხმოცი","ოთხმოცდაათი"]
s5 = ["ოცდა","ოცდა","ორმოცდა","ორმოცდა","სამოცდა","სამოცდა","ოთხმოცდა","ოთხმოცდა"]
s6 = ["ას","ორას","სამას","ოთხას","ხუთას","ექვსას","შვიდას","რვაას","ცხრაას"]
s7 = ["ათას","მილიონ","მილიარდ","ტრილიონ"]
s8 = ["ი"]

word = ""

def get_symbols(number, pos):
    ln = len(str(number))
    ss = str(number)
    return int(ss[(ln-pos):ln])

def ornishna(number):
    erteuli = int(str(number)[1])
    ateuli = int(str(number)[0])
    if(number in (11,12,13,14,15,16,17,18,19)):
        return s2[int((number % 10)-1)]
    if(erteuli == 0):
        return s4[ateuli-1]
    if(ateuli % 2 == 0):
        ateuli = s5[ateuli-2]
        erteuli = s1[erteuli]
        return ateuli + "" + erteuli
    else:
        ateuli = s5[ateuli-2]
        erteuli = s2[erteuli-1]
        return ateuli + "" + erteuli

def samnishna(number):
    erteuli = int(str(number)[2])
    ateuli = int(str(number)[1])
    aseuli = int(str(number)[0])
    if(erteuli == 0 and ateuli == 0):
        return s6[aseuli-1] + s8[0]
    if(erteuli == 0 and ateuli > 0):
        return s6[aseuli-1] + "" + s4[ateuli-1]
    if(erteuli > 0 and ateuli == 0):
        return s6[aseuli-1] + "" + s1[erteuli]
    else:
        return s6[aseuli-1] + "" + ornishna(ateuli * 10 + erteuli)

def n_1_999_to_word(number):
    if(number == 0):
        return ""
    if(number <= 10 and number > 0):
        return s1[number]
    if(number in (11,12,13,14,15,16,17,18,19)):
        return s2[int((number % 10)-1)]
    if(number < 100 and number > 19):
        return ornishna(number)
    if(number < 1000 and number > 99):
        return samnishna(number)

def number_to_word(number,word):
    if(number < 1000):
        if(number == 0):
            word += s8[0]
        else:
            word += " " + n_1_999_to_word(number)
        return word
    if(number > 999 and number < 1000000):
        word += " " + n_1_999_to_word(int(number / 1000)) +""+ s7[0]
        number = get_symbols(number,3)
        return number_to_word(number, word)
    if(number > 999999 and number < 1000000000):
        word += " " + n_1_999_to_word(int(number / 1000000)) +""+ s7[1]
        number = get_symbols(number,6)
        return number_to_word(number, word)
    if(number > 999999999 and number < 1000000000000):
        word += " " + n_1_999_to_word(int(number / 1000000000)) +""+ s7[2]
        number = get_symbols(number,9)
        return number_to_word(number, word)
    if(number > 999999999999 and number < 1000000000000000):
        word += " " + n_1_999_to_word(int(number / 1000000000000)) +""+ s7[3]
        number = get_symbols(number,12)
        return number_to_word(number, word)

def get_result(my_number):
    if(my_number < 1 or my_number > 999999999999999):
        return "გთხოვთ მიუთითოთ მთელი დადებითი რიცხვი, 1-დან 999999999999999-ს ჩათვლით"
    else:
        return number_to_word(my_number,"")

my_number = 123456789012345
print(get_result(my_number))
