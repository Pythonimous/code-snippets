import os

names = [tuple(f.split('.')) for f in os.listdir('./') if f[-2:] != 'py']
names = [[int(n[0]), ".".join(n[1:])] for n in names]
names.sort()

dict_by_first_number = {name[0]: [] for name in names}

for name in names:
    dict_by_first_number[name[0]].append(name[1])

old_numbers = list(dict_by_first_number.keys())

to_rename = {}

for i in range(len(old_numbers)):
    to_rename[old_numbers[i]] = i+1

renamed_files = [[to_rename[key], value] for key, value in dict_by_first_number.items()]

new_names = []
for f in renamed_files:
    for i in f[1]:
        new_names.append(f'{f[0]}.{i}')

old_names = [f'{n[0]}.{n[1]}' for n in names]

pairs = list(zip(old_names, new_names))
for pair in pairs:
    os.rename(f'./{pair[0]}', f'./{pair[1]}')
