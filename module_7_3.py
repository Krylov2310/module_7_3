print('\033[30m\033[47mДомашнее задание по теме "Оператор "with".\033[0m')
print('\033[30m\033[47mЗадача "Найдёт везде":\033[0m')
print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
thanks = '\033[30m\033[47mБлагодарю за внимание :-)\033[0m'
print()


class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        split = ''
        execute = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(self.file_names, encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                for i in line:
                    if i in execute:
                        line = line.replace(i, ' ')
                split = split + line
            all_words.update({self.file_names: split.split()})
        return all_words

    def find(self, word):
        sort = {}
        set_world = self.get_all_words()[self.file_names]
        for i in range(len(set_world)):
            if word.lower() == set_world[i]:
                sort.update({self.file_names: i+1})
                return sort

    def count(self, word):
        sort = {}
        set_world = self.get_all_words()[self.file_names]
        sort.update({self.file_names: set_world.count(word.lower())})
        return sort


# Пример выполнения программы:
finder2 = WordsFinder('test_file.txt')
print(f'Весь список разделен на слова: {finder2.get_all_words()}')
print(f'Поиск по "TEXT": {finder2.find('TEXT')}')
print(f'Поиск по "teXT": {finder2.count('teXT')}')
print()
print(thanks)
