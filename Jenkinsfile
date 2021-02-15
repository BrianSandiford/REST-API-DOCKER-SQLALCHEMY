pipeline {
    agent any
    environment {
        PASS = credentials('registry-pass') 
    }

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
                ansiblePlaybook credentialsId: 'docker_prod_key', disableHostKeyChecking: true, installation: 'ansible', inventory: '/var/lib/jenkins/workspace/test/hosts', playbook: '/var/lib/jenkins/workspace/test/build.yml'
            }
        }

        stage('Push') {
            steps {
                wwithDockerRegistry(credentialsId: 'dockerhub', url: 'https://registry.hub.docker.com') {
                ansiblePlaybook credentialsId: 'docker_prod_key', disableHostKeyChecking: true, installation: 'ansible', inventory: '/var/lib/jenkins/workspace/test/hosts', playbook: '/var/lib/jenkins/workspace/test/push.yml'
                }
            }
        }
        stage('Deploy') {
            steps {
                ansiblePlaybook credentialsId: 'k8s-managment-server-key', disableHostKeyChecking: true, installation: 'ansible', inventory: '/var/lib/jenkins/workspace/test/kubernetes/host', playbook: '/var/lib/jenkins/workspace/test/kubernetes/kubernetes-demodockerfileapp-deployment.yaml'
                mail bcc: '', body: 'jenkins email test', cc: '', from: 'rooms21@gmail.com', replyTo: '', subject: 'Failure', to: 'rooms21@gmail.com'
            }
        }
    }
        post {
         failure {
            mail bcc: '', body: 'jenkins email test', cc: '', from: 'rooms21@gmail.com', replyTo: '', subject: 'jenkins email', to: 'rooms21@gmail.com'
       
          }
    }
}
