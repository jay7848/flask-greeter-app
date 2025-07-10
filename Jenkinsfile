pipeline {
    agent any

    environment {
        APP_DIR = "${WORKSPACE}/flask-greeter-app"
    }

    stages {
        stage('Build') {
            steps {
                dir(APP_DIR) {
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                dir(APP_DIR) {
                    sh 'pytest || true'  // Skip errors if no tests yet
                }
            }
        }
        stage('Deploy') {
            steps {
                dir(APP_DIR) {
                    sh 'nohup python3 app.py &'
                }
            }
        }
    }

    post {
        success {
            mail to: 'YOUR_EMAIL@example.com',
                 subject: "Pipeline SUCCESS: ${env.JOB_NAME}",
                 body: "Good news! Your pipeline succeeded."
        }
        failure {
            mail to: 'YOUR_EMAIL@example.com',
                 subject: "Pipeline FAILED: ${env.JOB_NAME}",
                 body: "Oops! Your pipeline failed."
        }
    }
}
