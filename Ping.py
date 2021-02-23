import subprocess
import os
a = int(input("The range of addresses you want scanned lower: "))
b = int(input("The range of addresses you want scanned higher: "))
with open(os.devnull, "wb") as limbo:
        for n in range(a, b):
                ip="10.0.0.{0}".format(n)
                result=subprocess.Popen(["ping", "-n", "1", "-w", "1", ip],
        
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print (ip + " Inactive")
                else:
                        print (ip + " Active")
