# api
1. `GET = http://127.0.0.1:8000/api/csv/`
#### Описание
##### Ответ:
```json
{"response": [
      {
        "username": "username1",
        "spent_money": 123,
        "gems": ["rubin", "akat", "zakat"]
      },
      { 
        "username": "username2",
        "spent_money": 124,
        "gems": ["rubin", "akat", "zakat"]
      }
]}
```
+ 
` со списком из 5 клиентов, потративших наибольшую сумму за весь период.
Каждый клиент описывается следующими полями:

2. `POST = http://127.0.0.1:8000/api/csv/`
#### Описание
##### Аргументы:
+ `deals` - файл, содержащий историю сделок. `deals.csv` - находится в папке проекта.
##### Ответ:
+ `Status: OK` - файл был обработан без ошибок
+ `Status: Error, Desc: <Описание ошибки>` - в процессе обработки файла произошла ошибка.


# Доступы
Админка: 
1. login - `admin`
2. password - `admin`

# Как запустить проект
Нужно иметь Docker

1. `git clone https://github.com/egolodnikov/cd_drf.git`
2. `cd cd_drf/`
3. `docker-compose up`
