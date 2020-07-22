import csv

def ImportCSV(csvPath):
    inList = []
    with open(csvPath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row["farming_practicesList"])
            inList.append(row['farming_practicesList'])
    
    parsedList = Parse(inList)
    for item in parsedList:
        print(item)


def Parse(input):
    if input == [""]:
        return [ParseResult("", 0)]

    prertn = {}
    items = [""]

    for item in input:

        if ";" in item:
            items = item.split("; ")
            for phrase in items:
                prertn = PhraseAddOrInit(prertn, phrase)
        else:
            prertn = PhraseAddOrInit(prertn, item)

    rtn = []

    for key in prertn:
        rtn.append(ParseResult(key, prertn[key]))

    return rtn


def PhraseAddOrInit(prertn, phrase):
    if phrase in prertn:
        prertn[phrase] += 1
    else:
        prertn[phrase] = 1
    return prertn


class ParseResult():
    def __init__(self, phrase, count):
        self.Phrase = phrase
        self.Count = count

    def __str__(self):
        return self.Phrase + ": " + str(self.Count)
