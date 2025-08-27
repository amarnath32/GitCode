
# Streamlit + pandas sample app (AWS-ready)

A tiny Streamlit app to test hosting on AWS. Includes options for EC2, Elastic Beanstalk (Procfile), or container-based (App Runner/ECS).

## Run locally
```bash
python -m venv .venv && . .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---
## Option A — EC2 (quick and simple)
1. Launch an **Amazon Linux 2023** t3.small (or t2.micro) EC2 with an inbound rule for TCP **8501** (or use Nginx to proxy 80 → 8501).
2. SSH in, then:
   ```bash
   sudo dnf update -y
   sudo dnf install -y python3.11 git
   python3.11 -m venv appenv && source appenv/bin/activate
   git clone <your-fork-or-repo-url> app && cd app  # or scp the zip
   pip install -r requirements.txt
   nohup streamlit run app.py --server.address 0.0.0.0 --server.port 8501 &
   ```
3. Visit `http://<EC2-Public-IP>:8501`.
4. (Optional, recommended) Put **Nginx** in front on port 80/443 and run Streamlit on 8501. Lock down security group to your office IPs only.

---
## Option B — Elastic Beanstalk (managed VM)
Works with the included **Procfile**.
1. Install EB CLI locally: `pip install awsebcli`.
2. Initialize:
   ```bash
   eb init -p python-3.11
   eb create streamlit-sample-env
   eb setenv PORT=8080
   ```
3. Deploy: `eb deploy`
4. EB sets `$PORT`; the Procfile runs `streamlit` bound to that port.

---
## Option C — App Runner (container)
1. Build locally and push to ECR:
   ```bash
   aws ecr create-repository --repository-name streamlit-pandas-sample || true
   # get your account ID and region first
   docker build -t streamlit-pandas-sample .
   docker tag streamlit-pandas-sample:latest <ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/streamlit-pandas-sample:latest
   aws ecr get-login-password --region <REGION> | docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com
   docker push <ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/streamlit-pandas-sample:latest
   ```
2. Create an **App Runner** service from this ECR image; use port **8501**.
3. App Runner gives you a public HTTPS URL (restrict via AWS WAF or private VPC connector if needed).

---
## Locking access to office network (quick pointers)
- **EC2/EB**: restrict inbound rules on the instance or load balancer **Security Group** to your office public IP ranges only.
- **App Runner**: attach **AWS WAF** with IP allow-lists; or put behind **ALB + WAF** using VPC Ingress/Egress if you need private-only.
- For strictly internal-only access, consider **Private ALB in a VPC** and connect via **VPN/Direct Connect** or an **AWS Client VPN**.

---
## Files
- `app.py` — Streamlit + pandas demo UI
- `requirements.txt` — minimal deps
- `Procfile` — for Elastic Beanstalk-style start
- `Dockerfile` — for container platforms (App Runner/ECS)
- `.streamlit/config.toml` — headless server config
- `data.csv` — tiny sample dataset
```
