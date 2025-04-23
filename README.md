# Django Project with PostgreSQL and Docker

Цей проект налаштовує Django з PostgreSQL базою даних, працюючи через Docker. Це дозволяє вам швидко налаштувати середовище для розробки та тестування.

## Опис

- **Django**: Web framework для Python.
- **PostgreSQL**: Реляційна база даних.
- **Docker**: Для ізольованого середовища.

## Передумови

Щоб працювати з цим проектом, потрібно мати встановлені наступні інструменти:

1. [Docker](https://www.docker.com/get-started)
2. [Docker Compose](https://docs.docker.com/compose/)

## Підготовка до роботи

1. Клонуйте репозиторій:

    ```bash
    git clone <url-репозиторію>
    cd <папка-репозиторію>
    ```

2. Створіть файл `.env` у кореневій директорії проекту, який містить налаштування для бази даних:

    ```env
    SECRET_KEY=django-insecure-)urehbhiasnq2d_aqu6js$5#i%nb9s1v*--gf&*a+i87exvrgk
    DEBUG=True
    DB_NAME=testtask
    DB_USER=postgres
    DB_PASSWORD=sanki1010
    DB_HOST=db
    DB_PORT=5432
    ```

    Замість `DB_HOST=db` переконайтесь, що хост для бази даних встановлено на `db`, оскільки це ім'я контейнера бази даних у Docker Compose.

## Запуск проекту

1. Створіть Docker контейнери та запустіть їх:

    ```bash
    docker-compose up --build
    ```

2. Перевірте, чи працюють контейнери:

    ```bash
    docker-compose ps
    ```

3. Підключіться до контейнера веб-сервісу, щоб запустити міграції та створити суперкористувача:

    ```bash
    docker-compose run web python manage.py migrate
    docker-compose run web python manage.py createsuperuser
    ```

    Дотримуйтесь інструкцій для створення суперкористувача.

4. Тепер, коли все налаштовано, ви можете перейти за адресою `http://localhost:8000` для доступу до проекту.

## Тестування

Для запуску тестів:

1. Переконайтесь, що контейнер бази даних працює:

    ```bash
    docker-compose up -d db
    ```

2. Запустіть тести:

    ```bash
    docker-compose run --rm web pytest
    ```

Цей процес запустить тести у контейнері та виведе результати тестування.

## Проблеми та усунення

- **Connection refused** до бази даних: Переконайтесь, що в `.env` файлі у вас вказано правильне значення для `DB_HOST`, яке повинно бути `db`, а не `localhost`.
- Якщо виникають інші проблеми з підключенням, перевірте логи контейнера PostgreSQL:

    ```bash
    docker logs <container_name>
    ```

## Зупинка та видалення контейнерів

Щоб зупинити всі контейнери та видалити їх:

```bash
docker-compose down -v
