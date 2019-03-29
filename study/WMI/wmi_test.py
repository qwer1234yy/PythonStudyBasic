import unittest, wmi


class MyTestCase(unittest.TestCase):
    def test_basic_connection(self):
        # "Check that a standard connection works"
        result = wmi.WMI()
        print(result)
        self.assertTrue(result)


    def test_simple_moniker(self):
        # "Check that a simple moniker works"
        result = wmi.WMI(moniker="winmgmts:")
        print(result)
        self.assertTrue(wmi.WMI(moniker="winmgmts:"))

    def test_moniker_with_instance(self):
        # "Check that specifying an instance in the moniker works"
        for c0 in wmi.WMI().Win32_ComputerSystem():
            print(c0.Name)
        c1 = wmi.WMI(moniker='winmgmts:Win32_ComputerSystem.Name="%s"' % c0.Name)
        print(c1.UserName)
    def test_Win32_ComputerSystem(self):
        computer = wmi.WMI()
        computer_info = computer.Win32_ComputerSystem()[0]
        os_info = computer.Win32_OperatingSystem()[0]
        proc_info = computer.Win32_Processor()[0]
        gpu_info = computer.Win32_VideoController()[0]

        os_name = os_info.Name.encode('utf-8').split(b'|')[0]
        os_version = ' '.join([os_info.Version, os_info.BuildNumber])
        system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB

        print('OS Name: {0}'.format(os_name))
        print('OS Version: {0}'.format(os_version))
        print('CPU: {0}'.format(proc_info.Name))
        print('RAM: {0} GB'.format(system_ram))
        print('Graphics Card: {0}'.format(gpu_info.Name))
    def test_Win32_Perf_class(self):
        computer = wmi.WMI()
        perfor = computer.Win32_Perf()[0]
        print(perfor.Caption)

    def test_CIM_Memory_class(self):
        computer = wmi.WMI()
        CIM_Memory_ = computer.CIM_Memory()
        print(CIM_Memory_[0])
        print(CIM_Memory_[1])


if __name__ == '__main__':
    unittest.main()
