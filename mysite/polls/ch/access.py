import Pyro4

p = Pyro4.Proxy("PYRO:ch.x@localhost:3574")
velo = p.response("i dont feel happy")    
print("response = ", velo)