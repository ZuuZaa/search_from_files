import inquirer

file = "ap_docs2.txt"

def read_file(file):
    with open (file, "r") as file:
        documents = file.read().split("<NEW DOCUMENT>")
        for i, j in enumerate(documents):
            documents[i] = set(j.lower().replace("\n", ' ').replace(".", '').replace(",", '').split(' '))
    return documents

doc = read_file(file)

def search_word(doc, word):
    a = []
    for i, j in enumerate(doc):
        if word.issubset(j):
            a.append(i)
    return a

list_d = []


def read_document(doc, list_d, file,number):
    if number in list_d:
        with open (file, "r") as file:
            documents = file.read().split("<NEW DOCUMENT>")
            print(documents[number])
    else:
        print("Invalid number, please try again:")

while True:
    questions = [
    inquirer.List('choice',
                    message="What would you like to do?",
                    choices=['Search for document', 'Read document', 'Quit'],
            ),
    ]
    answers = inquirer.prompt(questions)
    
    if answers["choice"] == 'Search for document':
        word = set(input("type words to find?    ").split(' '))
        list_d = search_word(doc, word)
        print(list_d)
    elif answers["choice"] == 'Read document':
        number = int(input("Enter number of a file which would you like to read:   "))
        read_document(doc, list_d, file,number)
        print(list_d)
    elif answers["choice"] == 'Quit':
        print("see you:)")
        break




