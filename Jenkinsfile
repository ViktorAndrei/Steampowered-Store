/* Requires the Docker Pipeline plugin */
pipeline {
    agent any 
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/ViktorAndrei/Steampowered-Store.git'
            }
        }
        stage('Build and Test') {
            steps {
                bat 'python --version'
            }
        }
    }
}
