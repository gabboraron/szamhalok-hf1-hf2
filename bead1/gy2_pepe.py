from subprocess import PIPE, Popen
p1 = Popen(["dmesg"], stdout=PIPE)
p2 = Popen(["grep", "hda"], stdin=p1.stdout, stdout=PIPE)
p1.stdout.close()  # Allow p2 to receivea SIGPIPE ifp1 exits.
p2.wait()
output = p2.communicate()[0]
print(output)