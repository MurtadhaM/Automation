# Nginx Proxy Manager - Setup & Configuration

#VARIABLES FROM THE DASHBOARD i.e https://dash.cloudflare.com/929ec37202defab79c90cb35c96b348f/findasnake.com

<img width=30% src="https://badges.pufler.dev/visits/FindASnake/FindASnake?style=flat-square&color=black&logo=github">

---
mkdir data 
mkdir letsencrypt
chmod 777 data
chmod 777 letsencrypt
chown -R 1000:1000 data
chown -R 1000:1000 letsencrypt
---


export CF_Token="0Yzj6IRAxJni8ZV95Szcrl_aR5tn_0E71MeFfGVQ"
export CF_Zone_ID="4db4340ec56d4502efcc5f298f66768b"
export CF_Account_ID="929ec37202defab79c90cb35c96b348f"

curl https://get.acme.sh | sh -s email=my@findasnake.com
/root/.acme.sh/acme.sh --issue --dns dns_cf -d fuck.findasnake.com



### Ubuntu / Debian ###
sudo apt update
sudo apt install vim certbot  python3-certbot-dns-cloudflare python3-pip
### CentOS / RHEL / Fedora ###
sudo dnf -y install epel-release
sudo dnf -y install vim certbot python3-certbot-dns-cloudflare python3-pip
# Crypto Tools
sudo python3 -m pip install -U pyOpenSSL cryptography
# Config Export
mkdir -p ~/.secrets/certbot
sudo tee /etc/letsencrypt/dnscloudflare.ini > /dev/null <<EOT
# Cloudflare API token used by Certbot
dns_cloudflare_api_token = 0Yzj6IRAxJni8ZV95Szcrl_aR5tn_0E71MeFfGVQ
EOT 




sudo chmod 0600 /etc/letsencrypt/dnscloudflare.ini
# run the certbot manually
sudo certbot certonly -d *.findasnake.com  --dns-cloudflare --dns-cloudflare-credentials /etc/letsencrypt/dnscloudflare.ini \    --post-hook "service nginx reload" --non-interactive --agree-tos     --email someone-who-pays-attention-to-emails@findasnake.com



#### ----------- ####
version: '3.8'
services:
  app:
    image: 'jc21/nginx-proxy-manager:latest'
    restart: unless-stopped
    ports:
      - '80:80'
      - '81:81'
      - '443:443'
    volumes:
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
#### ----------- ####
podmon-compose up -d




