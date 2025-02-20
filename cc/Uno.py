from pwn import *

host = '2048.challs.olicyber.it'
port = '10007'

connection = remote(host, port)

connection.connect()

