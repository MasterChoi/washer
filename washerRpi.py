import spidev, time
import threading
import socket
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
spi = spidev.SpiDev()
spi.open(0,0)

gpio.setup(17, gpio.OUT)
gpio.setup(27, gpio.IN)

class Sender(threading.Thread):
	def run(self):
		global data
		data = "3"
		while 1:
			c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			try:
				c_socket.connect(('52.196.153.48', 9999))
			except Exception as e:
				print(e)
			try:
				c_socket.sendall(data.encode('utf-8'))
			except Exception as e:
				print("fail send")
			c_socket.close()
			time.sleep(1)

class SensorRead(threading.Thread):
		def run(self):
			def analog_read(channel):
				r = spi.xfer2([1, (8+channel) << 4, 0])
				adc_out = ((r[1] & 3) << 8) + r[2]
				return adc_out
			
			def wave_read():
				gpio.output(17, False)
				time.sleep(0.5)
				gpio.output(17, True)
				time.sleep(0.00001)
				gpio.output(17, False)

				while gpio.input(27) == 0:
					pulse_start = time.time()
				while gpio.input(27) == 1:
					pulse_end = time.time()
				
				duration = pulse_end - pulse_start
				distance = duration * 17000
				distance = round(distance, 2)
				return(distance)

			while True:
				sound = analog_read(0)
				print(sound)
				wave = wave_read()
				print(wave)

				if wave <= 56 and sound >= 400:
					data = "1"
					print(data)
				elif wave <= 56 and sound < 400:
					data = "2"
					print(data)
				else:
					data = "3"
					print(data)
				time.sleep(0.5)

sensorRead = SensorRead()
sender = Sender()
sensorRead.start()
sender.start()
