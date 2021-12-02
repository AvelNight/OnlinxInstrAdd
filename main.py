import datetime
import os
import shutil
import zipfile

os.chdir(os.getcwd())
# Создаём каталоги под файлы, перед этим удаляем существующие
if os.path.exists("instruments"):
    shutil.rmtree("instruments")
if os.path.exists("sheets"):
    shutil.rmtree("sheets")
if os.path.exists("charts"):
    shutil.rmtree("charts")
os.mkdir("instruments")
# os.chmod("instruments", 777)
os.mkdir("sheets")
# os.chmod("sheets", 777)
os.mkdir("charts")
# os.chmod("charts", 777)
instruments = []
# Указываем фанансовую площадку
platform = str(input())

# Создаем массив с кодами инструмента
with open("/Users/admin/Onlinx/file.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)
# array = ['XAG/USD_gr', 'XAU/USD_gr', 'XPD/USD_gr', 'XPT/USD_gr']
print("Массив создан")
# Создаем конфиги инструментов
os.chdir(os.getcwd())
os.chdir("instruments")
for i in range(len(array)):
    x = str(array[i])
    with open(x[:-1] + ".cfg", "a+", encoding='utf-8') as f:
        f.write("description=")
        f.close()
print("Инструменты созданы")

# Создаем строку для добавления в файл площадки
instr = str(array)
instr = instr.replace("'", "").replace("[", "").replace(r"\n", "").replace("]", "").replace(" ", "")
os.chdir("..")
os.chdir("sheets")
s = open("instruments.txt", "w+", encoding='utf-8')
s.write(instr)
s.close()
print("Строка создана")
# Создаем конфиги с параметрами для графика
os.chdir("..")
os.chdir("charts")
for i in range(len(array)):
    x = str(array[i])
    d = open(platform + "." + x[:-1] + ".cfg", "w+", encoding='utf-8')
    # Ниже прописываем маску для графиков
    d.write("fields=Last VDay,R VDay,Bid,Ask\n")
    d.write("periods=1,15,30,60,W,M,Y\n")
    d.write("mask=0000.00\n")
    d.write("filter=0.01\n")
    d.write("vmask=0000000000")
    d.close()
print("Параменты графика созданы")
# Архивируем все каталоги
dt = datetime.datetime.now()
now_date = dt.date().strftime("%Y-%m-%d")  # Текущая дата
now_time = dt.time().strftime("%H-%M-%S")  # Текущее время
os.chdir("..")
backup_folders = ["charts", "instruments", "sheets"]  # Список папок для архивации
arch_name = "arch_" + str(now_date) + ".zip"  # имя архива!
ignore_file = ["123.txt"]  # если надо исключить файлы


def mybackup(arch, folder_list, mode):
    # Счетчики
    num = 0
    num_ignore = 0
    # Создание нового архива
    z = zipfile.ZipFile(arch, mode, zipfile.ZIP_DEFLATED, True)
    # Получаем папки из списка папок.
    for add_folder in folder_list:
        # Список всех файлов и папок в директории add_folder
        for root, dirs, files in os.walk(add_folder):
            for file in files:
                if file in ignore_file:  # Исключаем лишние файлы
                    print("Исключен! ", str(file))
                    num_ignore += 1
                    continue
                # Создание относительных путей и запись файлов в архив
                path = os.path.join(root, file)
                z.write(path)
                print(num, path)
                num += 1
    z.close()
    print("------------------------------")
    print("Добавлено: ", num)
    print("Проигнорировано: ", num_ignore)


print(now_time, now_date)
# создаст архив при наличии перезапишет существующий
mybackup(arch_name, backup_folders, "w")
