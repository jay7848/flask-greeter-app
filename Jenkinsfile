pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }

    post {
        success {
            emailext(
                subject: 'Build SUCCESS: Job ${JOB_NAME} [${BUILD_NUMBER}]',
                body: 'Good news! The build succeeded.\n\nCheck here: ${BUILD_URL}',
                to: 'gjay8626@gmail.com'
            )
        }
        failure {
            emailext(
                subject: 'Build FAILED: Job ${JOB_NAME} [${BUILD_NUMBER}]',
                body: 'Unfortunately, the build failed.\n\nCheck here: ${BUILD_URL}',
                to: 'gjay8626@gmail.com'
            )
        }
    }
}
