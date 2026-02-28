class Robot:
    
    # constructor
    def __init__(self, baterie, delka_rukou):
        self.bat = baterie
        self.del_ruk = delka_rukou
        self.ukony_do_kontroli = 1000

    def krok_vpred(self):
        print("Robot udělal krok vpřed")
        self.ukony_do_kontroli -= 1
        print(f"Úkony do kontroly {self.ukony_do_kontroli}")
    
    def krok_dozadu(self):
        print("Robot udělal krok zpět.")
        self.ukony_do_kontroli -= 1
        print(f"Úkony do kontroly: {self.ukony_do_kontroli}")

        


robot_1 = Robot(24, 0.6)
robot_2 = Robot(10, 0.3)
robot_3 = Robot(50, 1.3)
robot_4 = Robot(38, 0.4)


robot_1.krok_vpred()
robot_1.krok_dozadu()
robot_1.krok_vpred()
robot_1.krok_dozadu()




































# print(robot_1.bat)
# print(robot_1.del_ruk)
# print(robot_1.ukony_do_kontroli)
# robot_1.krok_vpred()
# robot_1.krok_vpred()
# robot_1.krok_vpred()
# robot_1.krok_vpred()
# robot_1.krok_dozadu()
# robot_1.krok_dozadu()
# robot_1.krok_dozadu()
# robot_1.krok_dozadu()
# robot_1.krok_dozadu()
# print(robot_1.ukony_do_kontroli)


# print(robot_2.bat)
# print(robot_2.del_ruk)

# print(robot_3.bat)
# print(robot_3.del_ruk)

# print(robot_4.bat)
# print(robot_4.del_ruk)