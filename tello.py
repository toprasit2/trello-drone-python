import socket
import threading
import time

# IP and port of Tello
tello_address = ('192.168.10.1', 8889)

# IP and port of local computer
local_address = ('', 9000)

# Create a UDP connection that we'll send the command to
tello1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Linux config
# tello1.setsockopt(socket.SOL_SOCKET, 25, 'wlp3s0'.encode())

# Bind to the local address and port
tello1.bind(local_address)

# Send the message to Tello and allow for a delay in seconds
def send(message, delay):
  # Try to send the message otherwise print the exception
  try:
    tello1.sendto(message.encode(), tello_address)  
    print("Tello1 send: " + message)
  except Exception as e:
    print("Error sending: " + str(e))

  # Delay for a user-defined period of time
  time.sleep(delay)

# Receive the message from Tello
def receive():
  # Continuously loop and listen for incoming messages
  while True:
    # Try to receive the message otherwise print the exception
    try:
      response, ip_address = tello1.recvfrom(128)
      print("Tello1 message: " + response.decode(encoding='utf-8'))

    except Exception as e:
      # If there's an error close the socket and break out of the loop
      tello1.close()
      print("Error receiving: " + str(e))
      break

# Create and start a listening thread that runs in the background
# This utilizes our receive functions and will continuously monitor for incoming messages
receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()   


# Cammand
def command():
  send("command", 5)

# Takeoff
def takeoff():
  send("takeoff", 10)

# Land
def land():
  send("land", 5)

# Up 20-500 cm
def up(x):
  send("up "+x, 5)

# Down 20-500 cm
def down(x):
  send("down "+x, 5)

# Left 20-500 cm
def left(x):
  send("left "+x, 5)

# Right 20-500 cm
def right(x):
  send("right "+x, 5)
  
# Forword 20-500 cm
def forward(x):
  send("forward "+x, 5)

# Back 20-500 cm
def back(x):
  send("back "+x, 6)

# Rotate clockwise  1-3600 
def cw(x):
  send("cw "+x, 6)

# Rotate counter clockwise  1-3600 
def ccw(x):
  send("ccw "+x, 6)

# Flip 
# l left
# r right 
# f forward
# b back
# bl back/left
# rb right/back
# fl front/left
# fr front/right
def flip(x):
  send("flip "+x, 6)

# set Speed 1-100cm/s
def speed(x):
  send("speed "+x, 5)

# Check Battery
def battery():
  send("battery?", 5)

# Check Time
def time():
  send("time?", 5)

# Check Speed
def speed():
  send("speed?", 5)

def main():
    pass

if __name__ == '__main__':
    command()
    takeoff()
    battery()
    land()
    tello1.close()