#!/usr/bin/env bash
set -e
sudo apt update -y
sudo apt install -y apache2
sudo systemctl enable --now apache2

# Optional firewall (won't fail if ufw not installed)
if command -v ufw >/dev/null 2>&1; then
  sudo ufw allow 'Apache Full' || true
  sudo ufw allow OpenSSH || true
fi

# Simple landing page
echo '<html><h1>Ecommerce Cloud + AI Platform</h1><p>Apache is running on AWS EC2 ✅</p></html>' | sudo tee /var/www/html/index.html >/dev/null
echo "Done. Visit: http://$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4 || echo 'EC2_PUBLIC_IP')"
