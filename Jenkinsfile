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
            }
        }
    }
        post {
         failure {
            
            mail bcc: '', body: "<b>Example</b><br>\n\<br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: "rooms21@gmail.com", mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "rooms21@gmail.com";
       
          }
    }
}
