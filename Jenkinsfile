/* Requires the Docker Pipeline plugin */
pipeline {
    agent any 
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/username/repository.git'
            }
        }
        stage('Build and Test') {
            steps {
                sh 'mvn clean test'
            }
        }
    }
}
