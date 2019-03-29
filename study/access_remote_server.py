import unittest, winrm, win32api, win32net, wmi
from socket import *


class MyTestCase(unittest.TestCase):
    def test_access_server_by_winrm(self):
        username = 'mso\yang.yang'
        password = 'pwcmsoYY123'
        sess = winrm.Session('https://172.24.58.80', auth=(username, password), transport='kerberos')
        print(sess)
        result = sess.run_cmd('ipconfig', ['/all'])
        print(result)

    def test_access_server_by_win32(self):
        ip = '192.168.1.18'
        username = 'MSO\yang.yang'
        password = 'pwcmsoYY123'

        use_dict = {}
        use_dict['remote'] = r'\\\\172.24.58.80\\'
        use_dict['password'] = password
        use_dict['username'] = username
        result = win32net.NetUseAdd(None, 2, use_dict)
        win32net.NetUseAdd()
        print(result)

    def test_access_server_by_WMI(self):
        ip = '172.24.58.80'
        username = 'MSO\yang.yang'
        password = 'pwcmsoYY123'

        try:
            print("Establishing connection to %s" % ip)
            # connection = wmi.WMI(ip, user=username, password=password)
            connection = wmi.WMI()

            # ipconfig_result = connection.Win32_Process.Create(CommandLine="cmd.exe /c ipconfig")
            # print(ipconfig_result)

            # cmd_help = connection.Win32_Process.Create(CommandLine="cmd.exe /?")
            # print(cmd_help)
            # 'taskkill /F /PID pid_number'
            # notebook 15584 excel 13896
            kill_process = connection.Win32_Process.Create(CommandLine="cmd.exe /c taskkill /F /PID 15584")
            print(kill_process)
            # cmd:
            # shutdown /r --to Restart your windows PC; "shutdown /s" to Shutdown your computer;
            # shutdown /l" to Log off your computer
            # net start mssqlserver - Start default instance of SQL Server
            # net stop mssqlserver - Stop default instance of SQL Server
            # wmic logicaldisk get size,freespace,caption  --Hard disk information from command prompt
            # Querying
            # for os in connection.Win32_OperatingSystem():
            #     print(os.Caption)

            # Monitoring
            # pass one of “creation”, “deletion”, “modification” or “operation” to the.watch_for method
            # process_watcher = connection.Win32_Process.watch_for("creation")
            # while True:
            #     new_process = process_watcher()
            #     print(new_process.Caption)

            # 'Filtering the returned list'
            # this can get free size of disc
            # for disk in connection.Win32_LogicalDisk(DriveType=3):
            #     print(disk)

        except wmi.x_wmi:
            print("Your Username and Password of " + getfqdn(ip) + " are wrong.")


if __name__ == '__main__':
    unittest.main()
