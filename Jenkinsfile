pipeline {
    agent any

    stages {

      stage('Test SSH') {
            steps {
                sshagent(['a48a4ce8-11c4-4a64-b6a3-303aa5844f70']) {
                    sh 'ssh -o StrictHostKeyChecking=no root@10.103.196.119 "echo Jenkins连接成功"'
                }
            }
        }

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
       stage('Install Dependencies'){
	steps{
	 bat 'pip install -r requirements.txt'
	}
}
    }
}
