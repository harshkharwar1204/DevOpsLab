pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/harshkharwar1204/DevOpsLab' 
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt || true'
            }
        }

        stage('Run Scraper') {
            steps {
                sh 'python3 scraper.py'
            }
        }

        stage('Archive Output') {
            steps {
                archiveArtifacts artifacts: 'books.csv', fingerprint: true
            }
        }

        stage('Done') {
            steps {
                echo '✅ Pipeline completed successfully!'
            }
        }
    }
}
