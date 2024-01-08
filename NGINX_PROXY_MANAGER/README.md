# Nginx Proxy Manager With Data Persistence

- [x] Nginx Proxy Manager
- [x] Data Persistence
- [x] Let's Encrypt SSL Certificates

## Setup

#### 1. Create a directory for data persistence

```bash
# Create a directory for data persistence and change the ownership to 1000:1000
mkdir /data && chown 1000:1000 /data
mkdir /etc/letsencrypt && chown 1000:1000 /etc/letsencrypt
```

#### 2. Install the dependencies
```bash

apt install podman,python3-pip,git -y
pip3 install podman-compose
```


#### 3. Run the container

```bash
podman run -d -p 80:80 -p 81:81 -p 443:443 -v /data:/data -v /etc/letsencrypt:/etc/letsencrypt jc21/nginx-proxy-manager

```


#### 4. Backup the data and letsencrypt folder to share folder


```bash
cp -r /data /etc/letsencrypt <share folder>

```

#### 4. Access the webui

```bash

# Default username and password
# Username: admin@example.com
# Password: changeme

# Access the webui at http://localhost:81
```

