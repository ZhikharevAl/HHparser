# **Парсинг вакансий на HeadHunter.**

## Данный проект демонстрирует возможность получения и сохранения вакансий по определенному запросу (например, "QA") с сайта HeadHunter.

### Используемые библиотеки:
- [pandas](https://pandas.pydata.org/)
- [requests](https://pypi.org/project/requests/)

### Получение и сохранение данных.

Для получения данных используется класс **DataParser**, который принимает на вход название вакансии и количество страниц. Для каждой страницы запрашиваются данные с помощью библиотеки **requests**, данные записываются в список и возвращаются методом **get_data**.

Далее данные сохраняются в формате **.csv** с помощью метода **save_to_csv**. Название файла формируется на основе названия вакансии.

### Обработка данных.

Для обработки данных использовались возможности библиотеки **pandas**.

Для чтения данных из файла используется метод **read_csv**. Далее производится удаление столбца с индексом 0, переименование столбца и задание этого столбца как индекса датафрейма.

Затем для подсчета средней зарплаты выбираются только те строки, в которых указана зарплата **(df.salary.dropna()**). В каждой такой строке значение поля **salary** является строкой, содержащей словарь. Для того чтобы получить значение поля currency, необходимо эту строку преобразовать в словарь. Это делается с помощью функции **ast.literal_eval**. Далее создаются три списка: **rur, eur и usd**, содержащие словари с зарплатами в разных валютах.

Значения зарплат хранятся в словарях в виде интервала (от и до). Для подсчета средней зарплаты необходимо привести значения к числовому виду. Для этого производится следующая последовательность действий:

Из каждой строки извлекается значение поля from (нижняя граница) и удаляются все значения **NaN**.
Из каждой строки извлекается значение поля to (верхняя граница) и удаляются все значения **NaN**.
Значения **from и to** объединяются в пары, каждая пара представляет интервал зарплаты.
Из каждой пары извлекается среднее значение, и полученные значения средних значений затем усредняются для получения средней зарплаты.
Результат выводится на экран.