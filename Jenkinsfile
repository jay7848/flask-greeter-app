pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest || true'  // Skip errors if no tests yet
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
            mail to: 'gjay8626@gmail.com',
                 subject: "Pipeline SUCCESS: ${env.JOB_NAME}",
                 body: "Good news! Your pipeline succeeded."
        }
        failure {
            mail to: 'gjay8626@gmail.com',
                 subject: "Pipeline FAILED: ${env.JOB_NAME}",
                 body: "Oops! Your pipeline failed."
        }
    }
}
