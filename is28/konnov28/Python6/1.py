import pickle

def create_file(file_name, content):
    file = open(file_name, 'wb')
    pickle.dump(content, file)
    file.close()

def read_file(file_name):
    file = open(file_name, 'rb')
    content = pickle.load(file)
    file.close()
    return content

def print_dictionaries(array_of_dicts, string):
    if string == '':
        print(array_of_dicts)
        return
    for d in array_of_dicts:
        if string in d:
            print(d)

content = [{"математика" : 1,
            "история" : 2,
            "информатика" : 3,
            },
           {"математика" : 1,
            "география" : 2,
            "информатика" : 3,
            },
           {"математика" : 1,
            "география" : 2,
            "история" : 3,
            },
           ]

file_name = "test.pkl"

#create_file(file_name, content)
cont = read_file(file_name)
print_dictionaries(cont, "история")


