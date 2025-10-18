# Encryption — At Rest & In Transit (Quick Guide)

## In Transit (Web HTTPS)
1. **Install Certbot (Let’s Encrypt)** on Ubuntu (public domain required):
   ```bash
   sudo apt update && sudo apt install -y certbot python3-certbot-apache
   sudo certbot --apache -d yourdomain.com
   ```
   - Auto‑configures Apache with HTTPS and renewals.

2. **No domain?** Use a **self‑signed certificate** (good for demo):
   ```bash
   sudo a2enmod ssl
   sudo a2ensite default-ssl
   sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
     -keyout /etc/ssl/private/selfsigned.key -out /etc/ssl/certs/selfsigned.crt -subj "/CN=$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4)"
   sudo sed -i 's|/etc/ssl/certs/ssl-cert-snakeoil.pem|/etc/ssl/certs/selfsigned.crt|g' /etc/apache2/sites-available/default-ssl.conf
   sudo sed -i 's|/etc/ssl/private/ssl-cert-snakeoil.key|/etc/ssl/private/selfsigned.key|g' /etc/apache2/sites-available/default-ssl.conf
   sudo systemctl reload apache2
   ```
   - Then visit: `https://EC2_PUBLIC_IP` (browser will warn since it’s self‑signed).

## At Rest (for later DB upgrade)
- Use **AWS RDS** and check **“Enable encryption”** at creation (uses KMS).
- For EC2 files: use **EBS encryption** (enabled by default on many accounts) or store sensitive CSVs using filesystem encryption (e.g., LUKS) for advanced setups.

These steps fulfill the **Scenario‑1** requirement to **enable encryption for data at rest and in transit** (documented; quick to demo).
