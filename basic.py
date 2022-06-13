import time
import getpass

from spade import quit_spade

from spade_bdi.bdi import BDIAgent

jid = input("JID> ")
passwd = getpass.getpass()

a = BDIAgent(jid, passwd, "./jason_examples/chap3/domestic-robot/robot.asl")
a.start()

time.sleep(3)


a.stop().result()

quit_spade()