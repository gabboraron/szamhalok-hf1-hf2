import subprocess
#import time
#subprocess.call(['df', '-h']) 

p = subprocess.Popen(["ping","-c",  "5", "google.com"], stdout= subprocess.PIPE)
print(p.communicate())
