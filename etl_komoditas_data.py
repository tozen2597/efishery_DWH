# import modules
import operator
import json
import re

# specify json path
read_file = 'soal-2.json'

# read json using json.load()
with open(read_file) as file:
    data = json.load(file)

# get each fish and weights
ikan = []
# list exclusion of komoditas
exclude = [
    '',
    'dan',
    'kepala',
    'sea',
    'food',
    'ikan',
    'soto',
    'ayam',
    'babat',
    'kikil'
]
# mapping typo fish name
mapping = {
    'lelw': 'lele',
    'gurami': 'gurame',
    'mujaer': 'mujair',
    'parin': 'patin'
}

# dictionary for final result
soal_2 = {}
for val in data:
    for key, value in val.items():
        if key == 'komoditas':
            kom_split = value.replace(',',';').replace('.', ';').replace(' ',';')
            kom_split = re.split(';', kom_split)
            kom_split = [i for i in kom_split if i not in exclude]
            for i, kom in enumerate(kom_split):
                if kom in mapping.keys():
                    kom = mapping[kom]
                    kom_split[i] = kom
                if kom not in soal_2:
                    soal_2[kom] = 0
        else:
            ber_split = value.replace(' kg', 'kg').replace(',',';').replace('.', ';').replace(' ',';')
            ber_split = [x for x in re.split(';', ber_split) if x != '']
            bool_ind = [True for x in list(soal_2.keys()) if x in ber_split]
            bool_ind = True if True in bool_ind else False
            try:
                if bool_ind:
                    for i, ber in enumerate(ber_split):
                        if ber in soal_2.keys():
                            soal_2[ber] += int(ber_split[i+1].replace('kg', ''))
                elif 'setengah' in ber_split:
                    for kom in kom_split:
                        soal_2[kom] += 0.5
                elif '1/2' in ber_split:
                    for kom in kom_split:
                        soal_2[kom] += 0.5
                else:
                    # for i, ber in enumerate(ber_split):
                    #     print(ber)
                    #     print(re.findall(r'[0-9]-[0-9]', ber))
                    for kom in kom_split:
                        soal_2[kom] += int([x for x in ber_split if 'kg' in x][0].replace('kg', ''))
            except:
                continue

i = 1
for komoditas, berat in sorted(soal_2.items(), key=operator.itemgetter(1), reverse=True):
    print(f'{i}. {komoditas}: {berat}kg')
    i += 1