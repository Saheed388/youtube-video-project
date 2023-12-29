Creating a virtual machine 

1. Create VM machine

After creating it install the following to get your mage running
2. Update the package list:

sudo apt-get update
sudo apt-get install update 

3. 
install python
sudo apt-get install python3-apt
4. 
install wget
sudo apt-get install wget
wget https://bootstrap.pypa.io/get-pip.py 

5. 
install
sudo apt-get install python3-pip
goto
mage.ai
https://github.com/mage-ai/mage-ai/blob/master/README.md

6. 
install mage
sudo pip3 install mage-ai

7. 
After the installation navigate to the vm instance you created 
go to networl
copy the external address
-- eg http://34.140.168.22:6789

try start the mage 
mage start kafka_projec

When not being able to connect after the first connecttion
pip install --upgrade pyarrow


8. 
CREATE PERMISION VIA FIREWALL

Search fire wall
--vpc network
--create fire wall rules


Targets

--All instances in the network

Source IPV Range
0.0.0.0/0

Select TCP