## Prerequisites
```
udo apt update
sudo apt upgrade
sudo apt -y install python-pip
sudo apt -y install python-dev
sudo apt -y install libusb-dev
sudo apt -y install python-usb
sudo pip install -U nfcpy
sudo reboot

lsusb

python -m nfc

git clone  https://github.com/nfcpy/nfcpy.git
cd nfcpy/examples/
sudo python ./tagtool.py --device usb:XXXX:XXXX
```

## NEED
* Google App Script URL
* slack web incominghook
* slack token
* outgoing webhook
* Pasori[https://www.amazon.co.jp/%E3%82%BD%E3%83%8B%E3%83%BC-SONY-%E9%9D%9E%E6%8E%A5%E8%A7%A6IC%E3%82%AB%E3%83%BC%E3%83%89%E3%83%AA%E3%83%BC%E3%83%80%E3%83%BC-PaSoRi-RC-S380/dp/B00948CGAG]

## Usage(Python)
```
git clone https://github.com/ak1ra24/nfc-zaishitsu.git
cd nfc-zaishitsu
sudo python monitor-nfc-gas.py
```

