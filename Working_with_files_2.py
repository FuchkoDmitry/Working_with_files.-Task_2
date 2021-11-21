import os


def writing_file(path):
    data = {}
    for files in path:
        if files.endswith('.txt'):
            with open(files, encoding='utf-8') as file:
                line = file.read().split('\n')
                data[files] = (len(line), line)
    for number, lines in sorted(data.values()):
        with open('result.txt', 'a', encoding='utf-8') as file:
            file.writelines("%s\n" % line for line in lines)
    return file


writing_file(os.listdir())
