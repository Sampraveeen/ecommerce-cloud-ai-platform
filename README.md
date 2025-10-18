Ecommerce Cloud + AI Platform – Mini Project (Scenario 1)

A **scalable cloud-based e-commerce demo** deployed on **AWS EC2**, with **Python data cleaning & visualization**, and **documented security** (firewall + encryption). Built as a fast, portfolio-ready project.

## ✨ What this delivers

- EC2 instance (Ubuntu) + Apache web server
- Dataset loaded with **Pandas** (simulating DB import)
- **Data cleaning** + **Matplotlib plots** saved to `ai-analysis/outputs/`
- **Security**: security group rules + HTTPS setup guide (documented)
- Clean, professional repository structure

## 🧱 Repo Structure
```
ecommerce-cloud-ai-platform/
├── README.md
├── scripts/
│   └── server-setup.sh
├── ai-analysis/
│   ├── analysis.py
│   └── requirements.txt
├── data/
│   └── sales.csv
└── security/
    ├── firewall-rules.md
    └── encryption_guide.md
```

---

## 🚀 Step 1 — Launch EC2 (Ubuntu, t2.micro)
1. Go to **AWS Console → EC2 → Launch instance**.
2. Name: `ecommerce-cloud-ai` • AMI: **Ubuntu 22.04** • Type: **t2.micro (free tier)**.
3. **Key pair**: create or use existing (download `.pem`).
4. **Security group rules**:
   - Inbound: **22 (SSH)** from *My IP*, **80 (HTTP)** from *Anywhere*, **443 (HTTPS)** from *Anywhere*.
5. Launch → wait for `running` status.

### SSH into instance
```bash
chmod 400 your-key.pem
ssh -i your-key.pem ubuntu@EC2_PUBLIC_IP
```

---

## 🌐 Step 2 — Install a Web Server (Apache)
On the EC2 instance:
```bash
curl -O https://raw.githubusercontent.com/placeholder/placeholder/main/server-setup.sh # (or copy from scripts/server-setup.sh)
# If copying manually, paste the script content and run:
chmod +x server-setup.sh && sudo ./server-setup.sh
```

If you don’t want to copy, just run these directly:
```bash
sudo apt update -y
sudo apt install -y apache2
sudo systemctl enable --now apache2
# (Optional) UFW
sudo ufw allow 'Apache Full' || true
sudo ufw allow OpenSSH || true
echo "Apache installed. Visit: http://EC2_PUBLIC_IP"
```

Open a browser: `http://EC2_PUBLIC_IP` → You should see the **Apache default page** ✅

---

## 🧪 Step 3 — (Fast) Data Cleaning + Visualization
Locally (or on EC2), run the Python script:
```bash
cd ai-analysis
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python analysis.py
```
Outputs are saved to: `ai-analysis/outputs/`:
- `sales_by_category.png`
- `sales_trend.png`
- `cleaned_sales.csv` (post-cleaning data)

> This **simulates “dataset import to DB”** for the 1‑hour version. If you want a real DB later, swap in MySQL/Postgres and load `cleaned_sales.csv`.

---

## 🔐 Step 4 — Security (what to show in report)
- **Firewall rules** (Security Groups): see `security/firewall-rules.md`
- **Encryption at rest & in transit**: see `security/encryption_guide.md`
  - Quick: enable **HTTPS** on Apache with Let’s Encrypt or a self‑signed cert.
  - For DB later: use RDS with “Enable encryption” checked.

---

## 📦 Step 5 — Push to GitHub (commands)
```bash
git init
git add .
git commit -m "Initial commit: AWS + AI mini project"
git branch -M main
# Create an empty repo on GitHub named: ecommerce-cloud-ai-platform
git remote add origin https://github.com/YOUR_USERNAME/ecommerce-cloud-ai-platform.git
git push -u origin main
```

---

## 📝 What to Screenshot for the Report
- EC2 instance page (running)
- Security group inbound rules
- Apache default page in browser
- Plots saved by `analysis.py`

---

## 📈 Future Improvements (nice to mention in interview)
- Swap CSV → **RDS MySQL** and connect from Python
- Add **Flask** landing page on Apache (Reverse Proxy)
- Add **ALB (Application Load Balancer)** in front of EC2
- Add **simple sales forecasting** with scikit‑learn

---

**Author:** Samiksha P • *Scenario 1 mini‑project (Placement)*
