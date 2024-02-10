# Маланка Илья 
## Тестовое задание

##
##

## Суть задания:
Создание набора для пользователя

## Требования
1.      Вывод постранично записей из справочника на экран
2.      Добавление новой записи в справочник
3.      Возможность редактирования записей в справочнике
4.      Поиск записей по одной или нескольким характеристикам

## Особенности: 
1.      Реализация интерфейса через консоль (без веб- или графического интерфейса)
2.      Хранение данных должно быть организовано в виде текстового файла, формат которого придумывает сам программист
3.      В справочнике хранится следующая информация: фамилия, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый)

## Функционал
При запуске программы в окне консоли можно выбрать следующие пункты:

1 Display contacts (введя цифру 1) :
-будет забрана информация из файла contacts.json и выведена на экран.
Работа происходит через функцию display_contacts()

2 Add contact (введя цифру 2) :
Пользователю будет необходимо ввести следующие данные:
- Last Name:
- First Name:
- Middle Name: 
- Organization: 
- Work Phone:
- Personal Phone: 

Работа происходит через функцию add_contact()

3	Edit contact (введя цифру 3):
Пользователю будет необходимо ввести следующие обновленные данные:
- Last Name:
- First Name:
- Middle Name: 
- Organization: 
- Work Phone:
- Personal Phone: 

Работа происходит через функцию edit_contact()

4	Search contact:
Работа происходит через функцию search_contacts()

5	Exit:
Происходит выход из программы и сохранение всех актуальных данных
Работа происходит через функцию save_contacts()
