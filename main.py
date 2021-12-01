import os
import shutil
#Создаём каталоги под файлы, перед этим удаляем существующие
shutil.rmtree("instruments")
shutil.rmtree("sheets")
shutil.rmtree("charts")
os.mkdir("instruments")
os.mkdir("sheets")
os.mkdir("charts")
instruments = []

#Создаем массив с кодами инструмента
with open("/Users/admin/Onlinx/file.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)

#Создаем конфиги инструментов
os.chdir("instruments")
for i in range(len(array)):
    x = str(array[i])
    f = open(x[:-1] + ".cfg", "w", encoding='utf-8')
    f.write("description=")
    f.close()
#Создаем строку для добавления в файл площадки
instr = str(array)
instr = instr.replace("'","").replace("[","").replace(r"\n","").replace("]","").replace(" ","")
os.chdir("..")
os.chdir("sheets")
s = open("instruments.txt", "w", encoding='utf-8')
s.write(instr)
s.close()

#Создаем конфиги с параметрами для графика
os.chdir("..")
os.chdir("charts")
for i in range(len(array)):
    x = str(array[i])
    d = open("MMVB." + x[:-1] + ".cfg", "w", encoding='utf-8')
    d.write("fields=Last VDay,R VDay,Bid,Ask\n")
    d.write("periods=1,5,10,15,30,60,1440,W,M,Y\n")
    d.write("mask=0000.00\n")
    d.write("filter=0.01\n")
    d.write("vmask=0000000000")
    d.close()


