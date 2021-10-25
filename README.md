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
