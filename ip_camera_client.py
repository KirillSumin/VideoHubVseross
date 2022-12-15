from vidgear.gears import NetGear
import cv2

client = NetGear(
    address="127.0.0.1",  # вставить своё значение
    port="5454",  # вставить своё значение
    pattern=2,
    receive_mode=True,
    logging=True,
)

while True:
    frame = client.recv()

    if frame is None:
        break

    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()

client.close()
