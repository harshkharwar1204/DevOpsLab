pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/harshkharwar1204/DevOpsLab.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('devops-lab-app')
                }
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5001:5000 devops-lab-app'
            }
        }
    }
}
e
