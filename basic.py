import time
import getpass

from spade import quit_spade

from spade_bdi.bdi import BDIAgent

jid = "agente1@localhost"
passwd = "12345"

a = BDIAgent(jid, passwd, "condicional.asl")
a.start()

# Es para que se ejecute el fichero ASL, aumentar si el tiempo no es suficiente
time.sleep(3)


a.stop().result()

quit_spade()