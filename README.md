# Python-task2

How to setup this ?
# Step1
Install httpd and Docker in RedHat or Centos<br />
<b>dnf install httpd -y <br />
dnf install docker-ce -y<br /></b><br />
Start services<br />
<b>systemctl start httpd <br />
systemctl start docker<br />
systemctl enable httpd<br />
systemctl enable docker<br /></b>

# Step2
Download github repo <br />
<b>git clone https://github.com/Premchandg278/python-task2.git</b><br /><br />
Now copy index.html file to <b>/var/www/html/</b> directory<br />
<b>cp python-task2/index.html  /var/www/html/ <br /> <br /></b>
Copy docker.py file to <b>/var/www/cgi-bin/</b> directory<br />
<b>cp python-task2/docker.py  /var/www/cgi-bin/<br /><br /></b>
Copy page.html file to <b>/var/www/</b> directory<br /> 
<b>cp python-task2/page.html  /var/www/<br /><br /></b>

# Step3 
Check your Linux system ip address<br />
<b>ifconfig<br /></b>
Now you need to change http://192.168.43.168 to your linux system ip address in index.html and page.html webpages
