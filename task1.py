class Task1():
    """Цель - запросить с консоли у пользователя его имя, количество слагаемых
     все слагаемые одно за другим и написать их сумму, обратившись
     к пользователю по имени.
     
     *знания*
     общая структура языка
        http://docs.python.org/3.3/reference/simple_stmts.html
        http://docs.python.org/3.3/tutorial/controlflow.html#for-statements
        
     ввод\вывод с консоли
        http://docs.python.org/3.3/library/functions.html#print
        http://docs.python.org/3.3/library/functions.html#input
     обработка списков list
        http://docs.python.org/3.3/library/stdtypes.html#list

      подсказка - чтобы форматировать строку можно пользоваться оператором % 
        пример:
           "Этот %s день" % "Дерьмовый"
           "В нём %i %s часов" %(24,"унылых")
        http://docs.python.org/3.3/library/stdtypes.html#printf-style-string-formatting
     """

    def askName(self) :
        "метод должен запрашивать имя текущего пользователя"
        self.askName = input ("Введите ваше имя : ")
        return self.askName
        
    def askTermCount(self):
        "метод должен запрашивать количество слагаемых"
        self.askTermCount = input ("Введите количество слогаемых : ")
        return self.askTermCount
             
        
    def askTerm(self, i: "Номер очередного слагаемого" ):
        "метод должен запрашивать очередной параметр "
        self.askTerm = input ("Введите следующее целое слогаемое")
        return self.askTerm
            
        
    def main(self):
        name = self.askName()
        count = self.askTermCount()
        terms = [] #инициализируем список слагаемых
        for i in range (1, int(count)) :
            terms.append( askTerm ( i ) )
            
        Print ("Имя пользователя :"), name #здесь выводим для пользователя сумму слагаемых
        Print ("Сумма слогаемых :"), sum(terms) #можно воспользоваться встроенной функцией sum()

if __name__ == '__main__':
    Task1().main()
