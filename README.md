Клонировать приложение с помощью команды: git clone https://github.com/teegraph/monitor.git

Перейти в папку с приложением.
Активировать виртуальное окружение для WIN: venv\Scripts\activate
Для запуска миграций и сервера запустить start.bat

для запуска сенсора запустить **python sensor.py**


###### Вариант использования Docker:
Собрать контейнер `docker build -t monitor:1 .`

Запустить `docker-compose up -d`