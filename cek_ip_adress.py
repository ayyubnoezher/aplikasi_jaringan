import socket

#input nama hostname
hostname = input('masukan nama website : ')

#get ip address
ip_address = socket.gethostbyhostname(hostname)
 
 #menampilkan domain dan ip-address
 print(f'website : {hostname}')
 print(f'ip-address : {ip_address}')
