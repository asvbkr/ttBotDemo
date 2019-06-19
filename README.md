# ttBotDemo. Python 2 and 3 compatibility
Демонстрационный бот для ТамТам на основе https://github.com/asvbkr/TamTamBot
Рабочий инстанс - https://tt.me/asvbkrTestBot1 (@asvbkrTestBot1)
***
## Инструкция:
<ol>
<li> Клонировать текущий репозиторий - https://github.com/asvbkr/ttBotDemo
<li> При отсутствии установить в используемый интерпретатор пакеты: six, certifi, urllib3
<li> Установить переменную среды TT_BOT_DEMO_API_TOKEN - указать токен, полученный от @PrimeBot
<li> При необходимости:
<ul>
<li> Установить переменную среды TRACE_REQUESTS - вывод информации о всех запросах. Возможные значения - True или False
<li> Установить переменную среды LOGGING_LEVEL - уровень логирования. Возможные значения - текстовые названия уровней из пакета logging. Например, DEBUG или WARNING
</ul>
<li> Запустить на выполнение python manage.py runserver 0.0.0.0:5000. Для работы в режиме webhooks всё готово
<li> Для работы в режиме longpolls:
<ul>
<li> Под Django:
<ul>
<li> Старт - в браузере открыть адрес запущенного приложения с окончанием /start_polling
<li> Стоп - в браузере открыть адрес запущенного приложения с окончанием /stop_polling
</ul>
<li> Без Django: запустить на выполнение - python BotDemo.py. Остановка - Ctrl-Break
</ul>
<li> Бот с минимальной функциональностью готов.
</ol>
