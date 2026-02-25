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
       stage('Install Dependencies'){
	steps{
	 bat 'pip install -r requirements.txt'
	}
}
    }
}
