📦 CI/CD with GitHub Actions
This project uses GitHub Actions to automate the testing and deployment of the Flask Greeter App to an AWS EC2 instance.

⚙️ Workflow Overview
The GitHub Actions workflow (.github/workflows/deploy.yml) includes two main jobs:

Build

Checks out the code

Sets up Python 3.10

Installs dependencies from requirements.txt

Runs tests (you can add test commands)

Deploy

Runs only after a successful build

SSHs into an EC2 instance

Pulls the latest code from the repository

Restarts the corresponding systemd service (flask-greeter-main.service or flask-greeter-staging.service)

🔐 Required GitHub Secrets
You must configure the following repository-level secrets in GitHub under:
Settings → Secrets and variables → Actions → Repository secrets

Secret Name	Description
EC2_HOST	Public IP or DNS of your EC2 instance
EC2_USER	Username used to SSH (e.g., ubuntu)
EC2_KEY	Private SSH key (contents of .pem file)

📁 Deployment Paths
The deployment uses two systemd services on the same EC2 instance:

Branch	Directory	Port	Service Name
main	/home/ubuntu/flask-greeter-main	5000	flask-greeter-main.service
staging	/home/ubuntu/flask-greeter-staging	5001	flask-greeter-staging.service

🛠 How It Works
On a push to main:

GitHub Actions connects via SSH to EC2

Pulls the latest code into /home/ubuntu/flask-greeter-main

Restarts flask-greeter-main.service

On a push to staging:

Similar behavior, but uses the flask-greeter-staging service and directory

⚠️ Make sure your systemd services are set up to run the Flask app on different ports (e.g., 5000 for main, 5001 for staging)

✅ Testing Deployment
Access the apps via:

http://<EC2-IP>:5000 → Main branch

http://<EC2-IP>:5001 → Staging branch

Confirm the service status:

bash
Copy
Edit
sudo systemctl status flask-greeter-main.service
sudo systemctl status flask-greeter-staging.service
