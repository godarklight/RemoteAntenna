

This is will take some modifying but it's a bare minimum that I knocked up in 15 minutes  
  
You will need to install gpiod and find the gpiochip and line you wish to use  
I'm using a banana Pi M5 so it's almost certainly wrong for your setup.
Change the chip and line in driver/app.py - you can find out with the gpioinfo 0 or gpioinfo 1 command.  

Setup:
```bash
apt install gpiod
mkdir /opt/antenna
cd /opt/antenna
git clone https://github.com/godarklight/RemoteAntenna.git .
python3 -m venv .
. bin/activate
pip install -r requirements.txt

#Don't copy this if you don't want to run with systemd
echo Please set the username in the systemd service files
readline
sudo cp systemd/* /etc/systemd/system/
sudo chown root:root /etc/systemd/system/antenna-*.service
sudo nano /etc/systemd/system/antenna-driver.service
sudo nano /etc/systemd/system/antenna-web.service
sudo systemctl enable antenna-driver
sudo systemctl enable antenna-web
sudo systemctl start antenna-driver
sudo systemctl start antenna-web
```
