import unittest, wmi, re, string, os
from subprocess import Popen, PIPE
import subprocess


class MyTestCase(unittest.TestCase):
    def test_Handling_Services(self):
        ip = '172.24.58.80'
        username = 'MSO\yang.yang'
        password = 'pwcmsoYY123'
        conn = wmi.WMI(ip, user=username, password=password)
        for s in conn.Win32_Service(StartMode="Auto", State="Running"):
            # filter service names
            print(s.Name)
            if 'MSSQLSERVER' == s.Name:
                # result, = s.StartService()
                # print(result)
                print(s.State, s.StartMode, s.Name, s.DisplayName)

    def test_basics(self):
        conn = wmi.WMI()
        print(conn.Win32_Process.properties.keys())
        # for class_name in conn.classes:
        #     print(class_name)
        #     # if 'Process' in class_name:
        #     #     print(class_name)

    def test_subprocess(self):
        # print(subprocess.call(['ipconfig']))
        print(subprocess.call(["dir"], shell=True))

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
    def test_Win32_PerfFormattedData_class(self):
        computer = wmi.WMI()
        perfor = computer.Win32_PerfFormattedData()[0]
        print(perfor)


    def test_CIM_Memory_class(self):
        computer = wmi.WMI()
        CIM_Memory_ = computer.CIM_Memory()
        print(CIM_Memory_[0])
        print(CIM_Memory_[1])

    def test_GetServiceStatus(self, caption):
        self.caption = caption
        c = wmi.WMI()
        for svc in self.server.Win32_Service(Caption=self.caption):
            state = svc.State
        print(str(state))

    def test_GetCpuList(self):
        c = wmi.WMI()
        cpulist = []
        cpudict = {}
        for cpu in c.Win32_Processor():
            name = str(cpu.Name).strip()
        deviceid = str(cpu.DeviceID)
        cpudict = {deviceid: name}
        cpulist.append(cpudict)
        print(cpulist)
    def test_GetLocalDrives(self):
        #get size of disk
        ip = '172.24.58.80'
        username = 'MSO\yang.yang'
        password = 'pwcmsoYY123'
        c = wmi.WMI(ip, user=username, password=password)

        driveList = []
        for disk in c.Win32_LogicalDisk():
            if disk.DriveType == 3:
                driveList.append(str(disk.Name))
                print(float(disk.Size) /1073741824.0)
                print(float(disk.FreeSpace) / 1073741824.0)
        print(driveList)

    def test_get_uptime(self):
        ip = '172.24.58.80'
        username = 'MSO\yang.yang'
        password = 'pwcmsoYY123'
        c = wmi.WMI(ip, user=username, password=password)
        # secs_up = int([uptime.SystemUpTime for uptime in c.Win32_PerfFormattedData_PerfOS_System()][0])
        # hours_up = secs_up / 3600
        # print(hours_up)

        # for cpu in c.Win32_Processor():
        #     print(cpu)
        # utilizations = [cpu.LoadPercentage for cpu in c.Win32_Processor()]
        # print(utilizations)
        # utilization = int(sum(utilizations) / len(utilizations))  # avg all cores/processors
        # print(len(utilizations))
        # print(sum(utilizations))
        # print(utilization)
        # Available Memory
        # available_mbytes = int([mem.AvailableMBytes for mem in c.Win32_PerfFormattedData_PerfOS_Memory()][0])
        # print(available_mbytes)
        # Available Memory
        # available_mbytes = int([mem.AvailableMBytes for mem in c.Win32_PerfFormattedData_PerfOS_Memory()][0])
        # print(available_mbytes)

        # Memory Used
        for mem in c.Win32_PerfFormattedData_PerfOS_Memory():
            print(mem)

        pct_in_use = int([mem.PercentCommittedBytesInUse for mem in c.Win32_PerfFormattedData_PerfOS_Memory()][0])
        print(pct_in_use)

        # test ping
        # host_name = '172.24.58.80'
        # p = Popen('ping -n 1 ' + host_name, stdout=PIPE)
        # m = re.search('Average = (.*)ms', p.stdout.read())
        # print(p)
        # print(m)

if __name__ == '__main__':
    unittest.main()
