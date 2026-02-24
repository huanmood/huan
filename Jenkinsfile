// 最简单的 Jenkinsfile 示例
pipeline {
    agent any
 stage('Checkout Code') {
            steps {
                checkout scm
            }
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
}