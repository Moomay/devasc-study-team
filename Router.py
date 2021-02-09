class Router:
    def __init__(self, brand, model, hostname):
        self.brand = str(brand)
        self.model = str(model)
        self.hostname = str(hostname)
        self.interfaceSet = set()
        self.linkConnect = [] #[LocalInterface, router, ConnectInterface]
    def add_inf(self, interface):
        self.interfaceSet.add(interface)
    def show_infs(self):
        num_interface = len(self.interfaceSet)
        show_inf_l0 = 'Show interfaces of ' + self.hostname
        show_inf_l1 = self.hostname + ' has ' + str(num_interface) + ' interfaces'
        if (num_interface > 0):
            show_inf_ln = ''
            listInterface = list(self.interfaceSet)
            listInterface.sort()
            for interface in listInterface:
                show_inf_ln += interface+'\n'
            return show_inf_l0+'\n'+show_inf_l1+'\n'+show_inf_ln
        return show_inf_l0+'\n'+show_inf_l1+'\n'
    def connect(self, inf0, rc, infc):
        if (isinstance(rc, Router)):
            if (self.isInterfaceAdd(inf0) and rc.isInterfaceAdd(infc)):
                if (self.isConnect(inf0)):
                    self.disconnect(inf0)
                if (rc.isConnect(infc)):
                    rc.disconnect(infc)
                self.linkConnect.append([inf0, rc, infc])
                rc.linkConnect.append([infc, self, inf0])
    def isConnect(self, inf0):
        for link in self.linkConnect:
            if (link[0] == inf0):
                return True
        return False
    def disconnect(self, inf0):
        count = 0
        while (count < len(self.linkConnect)):
            if (inf0 == self.linkConnect[count][0]):
                break
            count += 1

        #link = self.linkConnect[count][::]
        self.linkConnect.pop(count)
    def isInterfaceAdd(self, inf):
        return inf in self.interfaceSet
    def show_cdp(self):
        txt = ''
        linkConnect = sorted(self.linkConnect ,key=lambda link: link[0])
        for link in linkConnect:
            txt += self.hostname + ' interface ' + link[0] + ' connect to ' + link[1].hostname + ' on interface ' + link[2] + '\n'
        return txt
if __name__ == '__main__':
    r1 = Router('Cisco', 'IOSv', 'R1')
    r2 = Router('Cisco', '3745', 'R2')
    r3 = Router('Juniper', 'MX5', 'R3')

    r1.add_inf('Gigabit 0/1')
    r1.add_inf('Gigabit 0/2')
    r2.add_inf('Gigabit 0/1')
    r2.add_inf('Gigabit 0/2')
    r2.add_inf('Gigabit 0/3')
    r3.add_inf('Gigabit 0/1')

    r1.connect('Gigabit 0/1', r2, 'Gigabit 0/3')
    print(r1.show_cdp())
    print(r1.show_infs())
    print(r2.show_infs())
    print(r3.show_infs())
