pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/huanmood/huan.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'pytest -v --maxfail=1 --disable-warnings'
            }
        }
    }
}
