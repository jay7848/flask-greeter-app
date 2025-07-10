pipeline {
    agent any

    environment {
        SLACK_TOKEN = credentials('slack-token')  // Use your Jenkins secret ID here
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
            mail to: 'gjay8626@gmail.com',
                 subject: "Pipeline SUCCESS: ${env.JOB_NAME}",
                 body: "Good news! Your pipeline succeeded."

            sh '''
                curl -X POST -H "Authorization: Bearer ${xoxb-9173527336214-9178665078148-vzFBJLq1JF7Q579eNTJt6ATa}" -H "Content-type: application/json" \
                --data '{"channel":"#all-herowired","text":"✅ Jenkins Pipeline SUCCESS: ${JOB_NAME}"}' \
                https://slack.com/api/chat.postMessage
            '''
        }
        failure {
            mail to: 'gjay8626@gmail.com',
                 subject: "Pipeline FAILED: ${env.JOB_NAME}",
                 body: "Oops! Your pipeline failed."

            sh '''
                curl -X POST -H "Authorization: Bearer ${xoxb-9173527336214-9178665078148-vzFBJLq1JF7Q579eNTJt6ATa}" -H "Content-type: application/json" \
                --data '{"channel":"#all-herowired","text":"❌ Jenkins Pipeline FAILED: ${JOB_NAME}"}' \
                https://slack.com/api/chat.postMessage
            '''
        }
    }
}
