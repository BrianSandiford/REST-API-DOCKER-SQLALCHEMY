pipeline {
    agent any
    triggers {
    githubPush()
    }
    stages {
        stage('git') {
            steps {
                git 'https://github.com/BrianSandiford/REST-API-DOCKER-SQLALCHEMY'
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
                sh '/var/lib/jenkins/workspace/test/build.sh'
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
