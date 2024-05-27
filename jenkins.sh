pipeline {
    agent any
    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ManikantaAnjuri/Boto3.git'
            }
        }
        stage('executing python script') {
            steps { 
                withAWS(region: 'ap-south-1', credentials: 'aws-accesskey'){
                sh "python3 4.py"
            }
            }
        }
    }
}
