# Escalatoria
Этот репозиторий содержит набор упражнений по повышению привилегий в Linux
Репозиторий включает в себя УКАЗАТЬ ФИНАЛЬНОЕ КОЛИЧЕСЧТВО файлов для Docker,
из которых формируются уязвимые образы. Представлены упражнения по повышению привилегий
с использованием следующих техник:

* Повышение привилегий за счет неправильных настроек sudo
* Повышение привилегий за счет неправильно установленных suid для файлов
* Повышение привилегий за счет неправильно установленных capabilities для бинарных файлов
* Повышение привилегий через crontab
* Повышение привилегий через переменные окружения
***
### Получение репозитория
* Скопируйте репозиторий на свою машину командой
* Установите Docker
* Приступайте!
***
### Повышение привилегий за счет неправильных настроек sudo
***
###### 1. ДОСТУПНО ВСЕ!
В этом упражнении мы увидим, как опасна настройка sudo, при которой пользователю разрешено 
выполнение любых команд без пароля
1.  Перейдите в каталог abuse_sudo/nopasswd/ командой `cd abuse_sudo/nopasswd`
2.  Соберите уязвимый образ командой `docker build -t sudo_no_passwd .`
3.  Запустите контейнер из собранного образа и перейдите в его оболочку с помощью команды
    `docker run -it sudo_no_passwd /bin/bash`
4.  Итак, первое, с чего мы начинаем свое повышение привилегий - проверка наличия у текущего пользователя прав sudo. Выполните команду `sudo -l`

![sudo -l result](/pictures/pic1.png)

5.  Мы видим, что для пользователя escalator через sudo доступно выполнение любых команд от имени суперпользователя без ввода пароля, для повышения привилегий достаточно выполнить `sudo su`

![sudo su result](/pictures/pic2.png)

Это был достаточно легкий пример повышения привилегий. Попробуем что-то другое

***
###### 2. Приложения, выполняющиеся через sudo
###### 2.1 Приложения, которые могут осуществлять запись в файл
Теперь мы приступим к техникам повышения привилегий в том случае, когда нам доступно sudo на бинарные файлы, которые могут осуществлять запись в файл. Мы рассмотрим повышение привилегий через sudo на текстовый редактор nano и через sudo на команду mv

1.  Перейдите в каталог abuse_sudo/sudo_on_bin/write_file/abuse_nano
2.  Соберите уязвимый образ `docker build -t abuse_nano .`
3.  Запустите контейнер из собранного образа и перейдите в его оболочку с помощью команды
    `docker run -it abuse_nano /bin/bash`
4.  Выполните sudo -l

![sudo -l result](/pictures/pic3.png)

5.  Мы видим, что мы можем через sudo использовать nano, и редактировать файлы с правами root. 
Для повышения привилегий необходимо отредактировать файл /etc/passwd, создав своего пользователя с правами root. 
Таким образом также осуществляется закрепление в системе
