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
        stage('ansibleTest') {
            steps {
                ansiblePlaybook disableHostKeyChecking: true, installation: 'ansible', inventory: '/var/lib/jenkins/workspace/test/host', playbook: '/var/lib/jenkins/workspace/test/build.yml'
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
