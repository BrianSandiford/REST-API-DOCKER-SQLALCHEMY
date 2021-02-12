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
                ansiblePlaybook credentialsId: 'docker_prod_key', disableHostKeyChecking: true, installation: 'ansible', inventory: '/var/lib/jenkins/workspace/test/hosts', playbook: '/var/lib/jenkins/workspace/test/build.yml'
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
