"""Задание 2 : пользовательские заметки
Цель - разработка минимального консольного интерфейса
Знакомство с паттернами State\Strategy """

class Menu:
    "Набор пользовательских команд, привязанный к модели"
    def __init__(self, model, items):
        self.model = model
        self.items = items
                                
    def show(self):
        "Вывести позиции в пронумерованном виде"
        for index,item in enumerate(self.items , 1):
            print( "[{index}]: {itemtext}".format(
                   index = index,
                   itemtext = item.text ) )
    def ask(self):
        """ Запросить номер выбранной команды у пользователя
            и вернуть выбраную команду"""
        index = -1  # задание 0
        while index >(len(self.items) - 1) or index < 0:
            index = int(input("Введите команду: ")) - 1
        return self.items[index]
    
    def run(self):
        "Показать меню, и выполнить выбранную пользователем команду"
        self.show()
        self.ask().execute()


class MenuItem:
    "Строчка меню"
    def __init__(self, text, command):
        self.text = text
        self.execute = command

class User:
    "Данные пользователя"
    def __init__(self,name):
        self.name = name
        self.notes = []
                        
class Model:
    "Общая модель приложения"

    users = {}  # задание 3 

    def menuName(model):
        if model.currentMenu == model.userMenu:
            print ("Список комманд пользователя %s" \
                   % (model.currentUser.name))
            
    def __init__(model):
        model.currentMenu = model.logInScreen
        model.currentUser = None
        
    def run(model):
        while model.currentMenu is not None:
            print ("Menu")
            model.currentMenu.run()

    noteSep = "-" * 20

    "Список команд"
    def logIn(model):
        userName = input("Введите имя пользователя: ")
        model.currentUser = User( name = userName )
        model.currentMenu = model.userMenu
        
        for key in model.users :    # задание 3
            if key == userName :
                model.currentUser.notes = model.users[key]                
        
        
    def addNote(model):
        print("Введите заметку: ", end=" ")
        model.currentUser.notes.append( list( model.readMultiLineNote() ))
                        
    def delNote(model):     # задание 1
        i = int(input("Введите заметку на удаление: ")) - 1
        del model.currentUser.notes[i]

    def readMultiLineNote(model):
        while True:
            nextLine = input()
            if nextLine: yield nextLine
            else: return 
        
    def listNotes(model):
        print(model.noteSep)
        for note in model.currentUser.notes :   # задание 2
            l = len(note)
            s = 15  # длина строки
            if l > s :
                for i in range (int(l/s) + 1):
                    print(note[i * s : (i + 1) * s])
                print("")    # "\n" добавляет 2 строки вместо одной
            else:
                print(note)
            print(model.noteSep)

    def logOut(model):
        model.currentMenu = model.logInScreen
        model.users[model.currentUser.name] = model.currentUser.notes
        model.currentUser = None
                
    def exit(model):
        print("До свидания!")
        model.currentMenu = None
        
    "Список меню"
    @property
    def logInScreen(model) :
        return Menu(model, [
            MenuItem(
                text = "Войти в систему",
                command = model.logIn),
            MenuItem(
                text = "Выйти из программы",
                command = model.exit )
            ])
    
    @property
    def userMenu(model):
        return Menu(model, [
            MenuItem(   # задание 1
                text = "Добавить заметку",
                command = model.addNote),
            MenuItem(
                text = "Удалить заметку",
                command = model.delNote),
            MenuItem(
                text = "Показать заметки",
                command = model.listNotes),
            MenuItem(
                text = "Выйти на стартовый экран",
                command = model.logOut)
            ])   
"""Задания:
0. При выборе команды реализовать проверку, что выбранное число является
    и лежит разрешимом интервале ( 1 - Max номер )

1. В меню пользователя добавить и реализовать команду "Удалить заметку"

2. Реализовать ввод многострочных заметок ( заканчивать ввод пустой строкой )

3. Реализовать хранение списка пользователей в модели так,
     чтобы входящий снова под своими именем пользователь имел доступ
     к уже введённым заметкам.
     
4. Добавить в классе Menu возможность определять заголовок Меню ( строчка,
     выводящаяся перед другими командами ).

5. Добавить в классах Menu и MenuItem возможность определять текст команды
     и заголовок меню как шаблон, зависящий от набора свойств Model.
     Сделать так, чтобы заголовом меню пользователя
     было "Команды пользователя {Имя текущего пользователя}"
"""

if __name__ == '__main__':
    Model().run()
