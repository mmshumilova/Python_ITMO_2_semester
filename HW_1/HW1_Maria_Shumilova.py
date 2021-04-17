import re

#1 replace all duplicated letters to one
pattern_1 = r'(\w)\1+'
string_1 = 'buzzzzz fuXXxx'

changed_object_1 = re.sub(pattern_1, r'\1', string_1)
print(changed_object_1)

# 2

string_2 = 'Mus musculus Agalma elegans Frillagalma vityazi Cordagalma tottoni'

pattern_2 = r'\b([A-Z])[a-z]*\b'
changed_object_2 = re.sub(pattern_2, r'\1.', string_2)
print(changed_object_2)


# 3
string_3 = 'Mus musculus (Y456) Agalma elegans (AB34) Frillagalma vityazi Cordagalma tottoni'

pattern_3 = r'\b([A-Z])[a-z]*\b'
changed_object_3 = re.sub(pattern_3, r'\1.', string_3)
pattern_4 = r'\('
changed_object_4 = re.sub(pattern_4, r'', changed_object_3)
pattern_5 = r'\)'
changed_object_5 = re.sub(pattern_5, r'', changed_object_4)
pattern_6 = r'\s'
changed_object_6 = re.sub(pattern_6, r'', changed_object_5)
#print(changed_object_3)
#print(changed_object_4)
print(changed_object_5)

#4
#>KAA8770496.1 isocitrate lyase [Escherichia coli] - from NCBI
#active_site = 'K-[KR]-C-G-H-[LMQR]' - from PROSITE

ID_pattern = r'>\w+\d+\.\d*'
active_site_pattern = r'K[KR]CGH[LMQR]'
ID =''
active_site = ''

with open('/home/maria/Documents/Python/02_semester/regular_expressions/hw_1/isocitrate_lyase_e_coli.txt', 'r') as file: #path to protein sequense
    for line in file:
        if '>' in line:
            ID = re.findall(ID_pattern, line) #find our ID and save it

        my_active_site = re.search(active_site_pattern, line) #find our active site
        if my_active_site is None:
            continue
        else:
            active_site = my_active_site # save information about the seq of active site

ID = ''.join(ID) #converting from lst to str
#print(ID)
active_site_seq = active_site.group() #filtering (find seq in our match object)
#print(active_site_seq)
active_site_starts_with = active_site.span() #filtering (find positions in our match object)
active_site_starts_with = active_site_starts_with[0] #we need only the first number
#print(active_site_starts_with)

print(f'Isocitrate lyase {ID} contains its active site {active_site_seq} starting from {active_site_starts_with}th position')



