#  Instalação da aplicação 
cd pontos; 
rm -rf node_modules; 
sudo apt-get install curl -y; 
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash - ; 
sudo apt-get install nodejs -y; 
sudo apt install python3 -y; 
sudo apt install python3-pip -y; 
cd /usr/lib/python3.11; 
sudo rm EXTERNALLY-MANAGED; 
sudo pip install --upgrade pandas;
sudo apt-get install firefox-esr; 

# Configuraçao do S.O 
sudo mv ~/pontos/shs/package-json /etc/init.d/
sudo mv ~/pontos/shs/package-json-cme /etc/init.d/
sudo ln -s /etc/rc5.d/S01ajuste /etc/init.d/package-json
sudo ln -s /etc/rc5.d/S01ajustecme.sh /etc/init.d/package-json-cme

# finalização 
chmod +x shs/*; 