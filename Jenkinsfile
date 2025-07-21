pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Scraper') {
            steps {
                sh '''
                    . $VENV_DIR/bin/activate
                    python scraper.py
                '''
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
