import threading
import socket, time
class Receiver(threading.Thread):
	def run(self):
		global data
		while 1:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			s.bind(('172.31.22.9', 9999))
			s.listen(1)
			conn, addr = s.accept()
			data = conn.recv(1024)
			print ("Received data : "+data.decode('utf-8'))
			conn.close()
			s.close()

class Con(threading.Thread):
	def run(self):
		while 1:
			while 1:
				print("an sock")
				serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
				print("created an sock")
				serverSocket.bind(('172.31.22.9',5555))
				print("binded")
				serverSocket.listen(1)
				print('waitting conn')
				conn, addr = serverSocket.accept()
				print('new conn')
				try:
					if data == b'1':
						print("Send data : "+data)
						conn.sendall("A\n")
					elif data == b'2':
						print("Send data : "+data)
						conn.sendall("B\n")
					elif data == b'3':
						print("Send data :"+data)
						conn.sendall("C\n")
					else:
						print("Recive error")
					time.sleep(1)
				except StandardError:
					print("Error")
					break
				conn.close()
				serverSocket.close()

rev = Receiver()
rev.start()
con = Con()
con.start()
