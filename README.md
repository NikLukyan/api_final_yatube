### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/NikLukyan/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Перейти в папку yatube_api и выполнить миграции:

```
cd yatube_api
```

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```


Когда вы запустите проект, по нижеуказанному адресу будет 
доступна полная документация для API Yatube в формате Redoc: 
```
/redoc/
```

Некоторые примеры запросов к API:

Получить JWT-токен можно после отправки POST-запроса 
на нижеуказанный эндпоинт, передав действующий логин 
и пароль в полях username и password. 

{
"username": "string",
"password": "string"
}:

```
/api/v1/jwt/create/
```

