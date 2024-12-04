# rpc_server.py
import Pyro4

# Definir la clase del servicio RPC
@Pyro4.expose
class HelloWorld(object):
    def say_hello(self, name):
        return f"Hello, {name}!"

# Iniciar el servidor Pyro4
def start_server():
    daemon = Pyro4.Daemon()  # Crear el daemon RPC
    ns = Pyro4.locateNS()  # Localizar el nameserver
    uri = daemon.register(HelloWorld)  # Registrar el servicio
    ns.register("example.hello", uri)  # Registrar el nombre del servicio
    print("Server is running...")
    daemon.requestLoop()  # Mantener el servidor corriendo

if __name__ == "__main__":
    start_server()
