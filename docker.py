#!/usr/bin/python3
import subprocess
import cgi

print('content-type: text/html')
print()
data = cgi.FieldStorage()
uname = data.getvalue("uname")
pwd  = data.getvalue("pwd")
operation = data.getvalue("operation")
if  uname == "root" and pwd == "prem" and operation == "docker" :
    image = data.getvalue("image")
    name = data.getvalue("name")
    port1 = data.getvalue("port1")
    port2 = data.getvalue("port2")
    localpath =  data.getvalue("localpath")
    dockerpath = data.getvalue("dockerpath")
    name = " --name  {}".format(name)
    if "None" in name :
        name = ""
    port = " -p {}:{}".format(port1,port2)
    if "None" in port :
        port = ""
    volume = " -v {}:{}".format(localpath,dockerpath)
    if "None" in volume :
        volume = ""
    cmd  = "sudo docker container run -dit {1} {2} {3} {0} ".format(image,name,port,volume)
    cmd = cmd.replace('None' , "")
    output = subprocess.getoutput(cmd)
    print(cmd)
    print("<pre>",output,"</pre>")
elif uname == "root" and pwd == "prem" and operation == "status" :
    status = data.getvalue("status")
    if status == "dockerengine":
        output = subprocess.getoutput("sudo systemctl status docker")
    elif status == "container":
        output = subprocess.getoutput("sudo docker ps -a")
    elif status == "runningcontainer":
        output = subprocess.getoutput("sudo docker ps")
    elif status == "images":
        output = subprocess.getoutput("sudo docker images")
    else :
        output = "invalid"
    print("<pre>",output,"</pre>")
elif uname == "root" and pwd == "prem" and operation == "start/stop":
    containername = data.getvalue("containername")
    status = data.getvalue("status")
    if status == "stop":
        output = subprocess.getoutput("sudo docker container stop {}".format(containername))
    elif status == "start":
        output = subprocess.getoutput("sudo docker container start {}".format(containername))
    elif status == "remove":
        output = subprocess.getoutput("sudo docker container rm -f {}".format(containername))
    else:
        output = "Invalid"
    print("<pre>",output,"</pre>")
elif uname == "root" and pwd == "prem" and operation == "cmd" :
    cmd = data.getvalue("cmd")
    cmd = "sudo {}".format(cmd)
    output = subprocess.getoutput(cmd)
    print("<pre>",output,"</pre>")
elif uname == "root" and pwd == "prem" and operation == "containeros":
    name = data.getvalue("osname")
    cmdd = data.getvalue("cmd")
    cmd = "sudo docker container exec {} {}".format(name,cmdd)
    output = subprocess.getoutput(cmd)
    print("<pre> {} </pre>".format(output))
elif uname == "root" and pwd == "prem":

    f = open("/var/www/html/my.html")
    print("succesfully login")
    print(f.read())
    f.close()
else:
    print("<h1>Authentication Error !!!!!</h1>")
