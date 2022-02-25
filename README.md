# OnlinxInstrAdd
Примерный порядок добавления нового инструмента на сервер ONLINX.
Состоит из следующих шагов:
1.Открыть \\onlinx\onlinx_configs

2.В папку  \\onlinx\onlinx_configs\instruments копируем конфигурационный файл формата: 
XXXXXX.cfg, где XXXXXX - код Тикера нового инструмента

3.В папку  \\onlinx\onlinx_configs\sheets  открываем  .cfg файл той торговой площадки куда нужно добавить новый инструмент
(или создать .cfg файл новой  торговой площадки)  и добавляем в него код Тикера нового инструмента.
В этих .cfg файлах также задается параметр временной задержки на данной площадке(если нужно), а также параметр fields - 
набор полей тикеров данной торговой площадки (названии колонок таблиц). Весь перечень всевозможных полей используемых  
инф.системой задается (добавление - копируем и переименовываем)в папке   \\onlinx\onlinx_configs\fields в виде 
соответствующего .cfg файла. 

4.В папке \\onlinx\onlinx_configs\charts  заводятся параметры графика который будет формироваться на сервере.
для чего создается(копируем и переименовываем) .cfg файл следующего формата: YYYYYY.XXXXXX.cfg, 
где YYYYYY - название торговой площадки, XXXXXX - название тикера инструмента.
в .cfg задаются параметры графика формируемого на сервере:
 
fields=Last VDay,R VDay,Bid,Ask              - поля по которым строятся графики
periods=1,5,10,15,30,60,1440,W,M,Y           - периоды свечей графика    
mask=000000.00                               - маска числового значения  
filter=0.01                                  - фильтр
vmask=0000000000                             - маска торгуемого объёма

При задании .cfg файлов графиков(копировании и переименовывании) нужно учитывать особенности торговых площадок и 
брать для копирования файлы той торговой площадки на которую добавляется новый график, а затем уже вносить 
точные коррективы в содержание YYYYY.XXXXXX.cfg файла графика.