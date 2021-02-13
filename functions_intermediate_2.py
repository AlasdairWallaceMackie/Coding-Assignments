x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print (x)

students[0]["last_name"] = "Bryant"
print (students)

sports_directory['soccer'][0] = "Andres"
print(sports_directory)

z[0]['y'] = 30
print(z)

nightwish = [
    {'first_name': "Tuomas", 'last_name': "Holopainen", 'instrument': "Keyboards"},
    {'first_name': "Emppu", 'last_name': "Vuorinen", 'instrument': "Guitar"},
    {'first_name': "Floor", 'last_name': "Jansen", 'instrument': "Vocals"},
    {'first_name': "Kai", 'last_name': "Hahto", 'instrument': "Drums"},
    {'first_name': "Marko", 'last_name': "Hietala", 'instrument': "Bass"},
    {'first_name': "Troy", 'last_name': "Donockley", 'instrument': ['uilleann pipes', 'tin whistle', 'bouzouki', 'bodhrán']}
]

def iterate_dictionary(some_list):
    for i in range(len(some_list)):
        output_line = ""
        for item in some_list[i]:
            output_line += (f"{item}: {some_list[i].get(item)}, ")
        output_line = output_line[:-2] #Remove final comma
        print(output_line)
iterate_dictionary(nightwish)

def iterate_dictionary_2(key_name, some_list):
    for i in range( len(some_list) ):
        print( some_list[i].get(key_name) )

iterate_dictionary_2('last_name', nightwish)
iterate_dictionary_2('first_name', nightwish)
iterate_dictionary_2('instrument', nightwish)

nightwish_dict = {
    'members': ['Tuomas', 'Floor', 'Emppu', 'Marko', 'Troy', 'Kai'],
    'albums': ['Angels Fall First', 'Oceanborn', 'Wishmaster', 'Century Child', 'Once', 'Dark Passion Play', 'Imaginaerum', 'Endless Forms Most Beautiful', 'Human. :||: Nature.']
}

def print_info(dict_of_lists):
    for item in dict_of_lists:
        output_string = ""
        print( str(len(dict_of_lists[item])) + " " + item.upper() )
        for i in range( len(dict_of_lists[item]) ):
            print( dict_of_lists.get(item)[i] )
        print(" ") #New Line

print_info(nightwish_dict)