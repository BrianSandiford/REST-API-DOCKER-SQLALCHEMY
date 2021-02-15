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
                withDockerRegistry(credentialsId: 'dockerhub', url: 'https://registry.hub.docker.com') {
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
            
            mail bcc: '', body: 'Project: ${env.JOB_NAME} Build Number: ${env.BUILD_NUMBER} URL of build: ${env.BUILD_URL}', cc: '', from: 'rooms21@gmail.com', replyTo: '', subject: 'ERROR CI CD: Project name -> ${env.JOB_NAME}', to: 'rooms21@gmail.com'
       
          }
    }
}
