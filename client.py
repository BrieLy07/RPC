# rpc_client.py
import Pyro4

# Localizar el nameserver
ns = Pyro4.locateNS()

# Obtener la URI del servicio
uri = ns.lookup("example.hello")

# Conectar al servicio remoto
hello_world = Pyro4.Proxy(uri)

# Llamar al método remoto
name = input("Escribe tu nombre: ")
message = hello_world.say_hello(name)
print(message)
