# Django + Stripe API бэкенд

Запуск приложения
------
```
git clone https://github.com/Jusseta/test_task.git
Установить виртуальное окружение
Создать и заполнить файл '.env' по примеру из '.env.sample'.
Собрать и запустить контейнер 'docker-compose up --build'.
```

Сервис
------
* `http://127.0.0.1:8000/admin/` - Админка
* `http://127.0.0.1:8000/buy/<item_id>` - Покупка товара
* `http://127.0.0.1:8000/item/<item_id>` - Страница товара
