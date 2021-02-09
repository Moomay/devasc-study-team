from Router import *
import unittest

class TestRouter(unittest.TestCase):
    def test_OneInf(self):
        r1 = Router('Cisco', 'IOSv', 'R1')
        r1.add_inf('Gigabit 0/1')
        self.assertEqual(r1.show_infs(), 'Show interfaces of R1\n'+
                                         'R1 has 1 interfaces\n'+
                                         'Gigabit 0/1\n'
        )
    def test_noInterface(self):
        r2 = Router('Mikrotik', 'RB450', 'R2')
        self.assertEqual(r2.show_infs(), 'Show interfaces of R2\n'+
                                         'R2 has 0 interfaces\n')
    def test_moreInterface(self):
        r3 = Router('TotoLink', 'A3002RU', 'R3')
        interfacesList = ['Fast 0/0', 'Fast 0/1', 'Fast 1/0', 'Fast 1/1']
        for interface in interfacesList:
            r3.add_inf(interface)
        self.assertEqual(r3.show_infs(), 'Show interfaces of R3\n'+
                                         'R3 has 4 interfaces\n'+
                                         'Fast 0/0\n'+
                                         'Fast 0/1\n'+
                                         'Fast 1/0\n'+
                                         'Fast 1/1\n'
        )
    def test_sameInterface(self):
        r4 = Router('Tplink', 'MR-6400', 'R4')
        r4.add_inf("Fast 0/0")
        r4.add_inf("Fast 0/0")
        r4.add_inf("Fast 0/1")
        r4.add_inf("Fast 0/1")
        self.assertEqual(r4.show_infs(), 'Show interfaces of R4\n'+
                                         'R4 has 2 interfaces\n'+
                                         'Fast 0/0\n'+
                                         'Fast 0/1\n'
        )
    def test_connect(self):
        r1 = Router('Cisco', 'IOSv', 'R1')
        r2 = Router('Mikrotik', 'RB450', 'R2')
        interfacesList = ['Gigabit 0/0', 'Gigabit 0/1', 'Gigabit 1/0', 'Gigabit 1/1']
        for interface in interfacesList:
            r1.add_inf(interface)
            r2.add_inf(interface)
        r1.connect('Gigabit 0/1', r2, 'Gigabit 1/0')
        r2.connect('Gigabit 1/1', r1, 'Gigabit 0/0')
        self.assertEqual(r1.show_cdp(), 'R1 interface Gigabit 0/0 connect to R2 on interface Gigabit 1/1\n'+
                                        'R1 interface Gigabit 0/1 connect to R2 on interface Gigabit 1/0\n'
                                        
        )
        self.assertEqual(r2.show_cdp(), 'R2 interface Gigabit 1/0 connect to R1 on interface Gigabit 0/1\n'+
                                        'R2 interface Gigabit 1/1 connect to R1 on interface Gigabit 0/0\n'
        )

if __name__ == '__main__':
    unittest.main()