class Pdf:
    def open(self):
        print("open the pdf")
class Word:
    def open(self):
        print("open the word file")
def open1(obj):
    obj.open()
p=Pdf()
w=Word()
open1(p)
open1(w)