
import dmx
import socket


wash = dmx.EuroliteMovingHeadWash(base=1, color=(1, 1, 1), intensity=1)
controller = dmx.DMXController(debug=True, fixtures=[wash])
controller.enabled = True

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 9000))

while True:
    message = server.recv(1000)
    command, argument = message.strip().split(' ', 1)
    if command == 'color':
        rgb = int(argument, 16)
        wash.color = (rgb >> 16) / 255., ((rgb >> 8) & 0xff) / 255., (rgb & 0xff) / 255.
    elif command == 'tilt':
        wash.tilt = int(argument)
    elif command == 'pan':
        wash.pan = int(argument)

