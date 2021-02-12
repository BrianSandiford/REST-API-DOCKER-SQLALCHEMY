pipeline {
    agent any
    triggers {
    githubPush()
    }
    stages {
        stage('Build') {
            steps {
                sh 'build.sh'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
