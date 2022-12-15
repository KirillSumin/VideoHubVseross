Для запуска требуется: **>=python3.7, openssh (openssh-server)**

### Запуск основного скрипта:
- Создать виртуальное окружение python (по желанию) \
Установить зависимости:
    ``` bash
    pip install -r requirements.txt
    ```
- По примеру .env_example создать файл .env и вписать туда свои секреты
- Запустить сервер:
    ``` bash
    python3 ip_camera_server.py
    ```
- Запустить клиент:
    ``` bash
    python3 ip_camera_client.py
    ```