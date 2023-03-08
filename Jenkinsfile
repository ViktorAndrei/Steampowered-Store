/* Requires the Docker Pipeline plugin */
pipeline {
    agent any 
    stages {
        stage('Testing GitHub-tests locally') {
            steps {
                dir('C:/Users/User/.jenkins/workspace/KK2 - Tester/Steams hemsida - tester'){ 
                    bat 'python -m unittest'
                }
            }
        }
        stage('Clean Workspace'){
            steps {
                cleanWs()
            }
        }
        }
}
