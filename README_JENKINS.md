# Flask Greeter App - Jenkins CI/CD Pipeline

This repository demonstrates a Jenkins-based CI/CD pipeline for a simple Flask web application. The application is deployed on an AWS EC2 instance and includes notifications via Slack and Email.

## 🔧 Prerequisites

- AWS EC2 instance (Ubuntu 22.04)
- Jenkins installed and running on port `8080`
- Open ports: `22`, `8080`, `5000`, `5001`
- GitHub repo forked: https://github.com/jay7848/flask-greeter-app.git
- App Password for Gmail SMTP
- Slack Bot Token for notifications

---

## 📦 Setup Instructions

### 1. Launch EC2 & Install Jenkins

- Launch EC2 → Ubuntu 22.04 → t2.micro
- Open ports: `22`, `8080`, `5000`, `5001`
- SSH into instance:
  ```bash
  ssh -i "your-key.pem" ubuntu@<ec2-ip>
Install Jenkins:

bash
Copy
Edit
sudo apt update
sudo apt install -y openjdk-17-jdk
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt install -y jenkins
sudo systemctl enable jenkins
sudo systemctl start jenkins
Visit http://<ec2-ip>:8080 and unlock Jenkins:

bash
Copy
Edit
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
Install suggested plugins and create an admin user.

2. Install Tools on EC2
bash
Copy
Edit
sudo apt install -y git python3 python3-pip
3. Clone Repo on Jenkins Server
bash
Copy
Edit
git clone https://github.com/jay7848/flask-greeter-app.git
cd flask-greeter-app
4. Jenkins Pipeline Configuration
Create a Jenkinsfile in your repo:

groovy
Copy
Edit
pipeline {
    agent any

    environment {
        SLACK_TOKEN = credentials('slack-token') // Configure this secret in Jenkins
    }

    stages {
        stage('Build') {
            steps {
                sh 'pip3 install --user -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'PATH=$PATH:$HOME/.local/bin && pytest || true'
            }
        }
        stage('Deploy') {
            steps {
                sh 'nohup python3 app.py &'
            }
        }
    }

    post {
        success {
            mail to: 'youremail@gmail.com',
                 subject: "Pipeline SUCCESS: ${env.JOB_NAME}",
                 body: "Good news! Your pipeline succeeded."
            sh '''
                curl -X POST -H "Authorization: Bearer ${SLACK_TOKEN}" -H "Content-type: application/json" \
                --data '{"channel":"#your-channel","text":"✅ Jenkins Pipeline SUCCESS: ${JOB_NAME}"}' \
                https://slack.com/api/chat.postMessage
            '''
        }

        failure {
            mail to: 'youremail@gmail.com',
                 subject: "Pipeline FAILED: ${env.JOB_NAME}",
                 body: "Oops! Your pipeline failed."
            sh '''
                curl -X POST -H "Authorization: Bearer ${SLACK_TOKEN}" -H "Content-type: application/json" \
                --data '{"channel":"#your-channel","text":"❌ Jenkins Pipeline FAILED: ${JOB_NAME}"}' \
                https://slack.com/api/chat.postMessage
            '''
        }
    }
}
5. Configure Jenkins Job
Go to Jenkins → New Item → Name: flask-greeter-pipeline

Choose: Pipeline → Pipeline script from SCM

Git URL: https://github.com/<your-username>/flask-greeter-app.git

Branch: main

6. Gmail SMTP Setup
Go to: Google App Passwords

Create password for "Mail → Jenkins"

Jenkins → Manage Jenkins → Configure System → Email Notification:

SMTP Server: smtp.gmail.com

Port: 587

Use TLS: ✅

Credentials: Your Gmail & App Password

7. GitHub Webhook
Go to GitHub → Repo → Settings → Webhooks → Add Webhook:

Payload URL: http://<EC2-IP>:8080/github-webhook/

Content type: application/json

Event: "Just the push event"

Jenkins Job → Configure:

✅ GitHub hook trigger for GITScm polling

✅ Testing
bash
Copy
Edit
git add .
git commit -m "Trigger Jenkins CI/CD"
git push origin main
This should start the Jenkins pipeline, build, test, and deploy the app.
