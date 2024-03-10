import os

def text(sector):
    file_main = os.main_dir(sector)
    text_list = []

    for file in file_main:
        with open(sector + "/" + file) as file_1:
            text_list.append([file, 0, []])
            for line in file_1:
                text_list[-1][2].append(line.strip())
                text_list[-1][1] += 1
    return sorted(text_list, key=lambda x: x[1])


def text_sector(sector, name):
    with open(name + '.txt', 'w+', encoding = 'utf-8') as file_2:
        for file in text(sector):
            file_2.write(f'File name: {file[0]}\n')
            file_2.write(f'Length: {file[1]} string(s)\n')
            for string in file[2]:
                file_2.write(string + '\n')
            file_2.write('-\n')

text_sector('text', 'mytext')
