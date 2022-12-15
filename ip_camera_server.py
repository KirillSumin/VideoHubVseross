from vidgear.gears import CamGear
from vidgear.gears import NetGear
from environs import Env


# все секретные настройки читаются из файла .env, делать по подобию .env_example
env = Env()
env.read_env()

# SOURSE_URL='http://192.168.0.111:4747/video'   # ip камера
SOURSE_URL = 0  # встроенная камера

FRAMES_SKIP = 0

# имя пользователя@ip контейнера, пароль от пользователя (как при подключении по ssh)
options1 = {
    "ssh_tunnel_mode": f"{env('SHH_USER1')}@{env('SHH_IP1')}",  # defaults to port 22
    "ssh_tunnel_pwd": env('SHH_PASSWORD1')
}

options2 = {
    "ssh_tunnel_mode": f"{env('SHH_USER2')}@{env('SHH_IP2')}",  # defaults to port 22
    "ssh_tunnel_pwd": env('SHH_PASSWORD2')
}

options3 = {
    "ssh_tunnel_mode": f"{env('SHH_USER2')}@{env('SHH_IP2')}",  # defaults to port 22
    "ssh_tunnel_pwd": env('SHH_PASSWORD2')
}

stream = CamGear(source=SOURSE_URL).start()

server1 = NetGear(
    address="127.0.0.1",
    port="5454",
    pattern=2,
    logging=True,
    **options1
)

server2 = NetGear(
    address="127.0.0.1",
    port="5455",
    pattern=2,
    logging=True,
    **options2
)

server3 = NetGear(
    address="127.0.0.1",
    port="5456",
    pattern=2,
    logging=True,
    **options3
)

frame_counter = 0
while True:
    try:
        frame = stream.read()

        if frame is None:
            break

        if frame_counter == FRAMES_SKIP:
            frame_counter = 0

            server1.send(frame)
            server2.send(frame)
            server3.send(frame)
        else:
            frame_counter += 1
    except KeyboardInterrupt:
        break

stream.stop()

server1.close()
server2.close()
server3.close()
