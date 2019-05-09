# ttBotDemo. Python 2 and 3 compatibility
Демонстрационный бот для ТамТам на основе https://github.com/asvbkr/TamTamBot
***
## Инструкция:
<ol>
<li> Клонировать на один уровень:
<ul>
<li> Репозиторий клиента TamTam Bot API - https://github.com/asvbkr/openapi_client
<li> Репозиторий протобота ТамТам - https://github.com/asvbkr/TamTamBot
<li> Текущий репозиторий - https://github.com/asvbkr/ttBotDemo
</ul>
<li> Создать каталог log на уровне каталогов, клонированных на предыдущем шаге
<li> При отсутствии установить в используемый интерпретатор пакеты: six, certifi, urllib3
<li> Создать файл BotCfg.py в котором добавить константу:<br/>
<CODE>
TOKEN = 'указать токен, полученный от @PrimeBot ТамТам'
</CODE>
<li> Запустить на выполнение файл BotDemo.py
<li> Бот с минимальной функциональностью готов.
</ol>