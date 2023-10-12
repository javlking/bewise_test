## Сервис по получению вопрсов для викторины

### Стек технологий:
- python3
- FastApi
- Sqlalchemy
- PostgreSQL
- docker-compose

Для запуска проекта необходимо клонировать репозиторий:
`git clone https://github.com/javlking/bewise_test.git`

Перейти в нужную папку:
`cd bewise_test`

Собрать образ и запустить контейнер docker-compose
`docker-compose up -d --build`

Пример запроса к POST API сервиса можно через swagger для этого нужно после запуска перейти по ссылке [http://0.0.0.0:8000](http://0.0.0.0:8000))
