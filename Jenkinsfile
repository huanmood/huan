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
                bat '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt || exit /b 0
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    echo Running pytest...
                    pytest -v --maxfail=1 --disable-warnings > result.log
                    type result.log
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'result.log', onlyIfSuccessful: false
        }
    }
}
