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
                    echo Installing dependencies...
                    pip install --upgrade pip
                    pip install -r requirements.txt || echo No requirements.txt found, skip.
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    echo Running pytest...
                    cd Print_APP
                    set PYTHONPATH=%cd%
                    pytest -v --maxfail=1 --disable-warnings --html=../report.html --self-contained-html > result.log
                    type result.log
                '''
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }
    }
}
