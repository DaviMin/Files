

file = open("first_file.txt", "w")
#to w je zpusob zapisu/cteni - pokud neexistuje, tak ho vytvori
# pokud existuje, tak to tam prepise
# textovy soboru nepotrebuje nutne koncovku .txt

file.write("Test Text")
file.close()
# kdyz kdykoliv otevrim sobour, zapisu/nactu a hlavne pak zavru, at nezabira pamet

file = open("first_file.txt", "r")
# ted tim r ho jen ctu
data = file.read()
file.close()
print(data)
# jak to dostat do souboru a jak ze souboru

file = open("first_file.txt", "a")
file.writelines("\ndruhy radek")
# \n tak se to znaci enter - ted se muzu podivat do first_file.txt, jak je to tam psane

