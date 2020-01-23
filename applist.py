import wmi
from tabulate import tabulate
def list():
    w=wmi.WMI()
    prod=[]
    for p in w.Win32_Product():
       prod.append([p.Caption,p.Vendor,p.Version])
    print(tabulate(prod,headers=['Program name','Publisher','Version'],tablefmt="psql"))

