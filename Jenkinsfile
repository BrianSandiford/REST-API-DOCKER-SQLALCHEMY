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
                ansiblePlaybook credentialsId: 'docker_prod_key', disableHostKeyChecking: true, installation: 'ansible', inventory: '/var/lib/jenkins/workspace/test/hosts', playbook: '/var/lib/jenkins/workspace/test/build.yml'
            }
        }
        stage('Test') {
            steps {
                ansiblePlaybook credentialsId: 'docker_prod_key', disableHostKeyChecking: true, installation: 'ansible', inventory: '/var/lib/jenkins/workspace/test/hosts', playbook: '/var/lib/jenkins/workspace/test/test.yml'
               // withCredentials([sshUserPrivateKey(credentialsId: 'docker_prod_key', keyFileVariable: 'docker_key', passphraseVariable: '', usernameVariable: 'root')]) {
               //     sh 'chmod 777  /var/lib/jenkins/workspace/test/'
                   // sh 'scp root@3.21.97.213:/root/demo-dockerfile/REST-API-DOCKER-SQLALCHEMY/reports/path.xml /var/lib/jenkins/workspace/test/'
              //  }

            }
        }

         stage('publish') {
            steps {  
                  withCredentials([sshUserPrivateKey(credentialsId: 'docker_prod_key', keyFileVariable: 'docker_key_variable', passphraseVariable: '', usernameVariable: '')]) {
                    sh 'chmod 777  /var/lib/jenkins/workspace/test/'
                 //   sh 'sudo chown root:root  /var/lib/jenkins/workspace/test/'
                //    sh 'ssh -tt -i $docker_key_variable  root@18.224.64.90'
                 //    sh 'touch /var/lib/jenkins/workspace/test/testfile'
                    sh 'scp -r -i $docker_key_variable root@18.224.64.90:/root/demo-dockerfile/REST-API-DOCKER-SQLALCHEMY/reports/path.xml /var/lib/jenkins/workspace/test'
                }
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
            junit '/var/lib/jenkins/workspace/test/path.xml'
            mail bcc: '', body: 'Please  verify the build', cc: '', from: 'rooms21@gmail.com', replyTo: '', subject: 'Build has failed', to: 'rooms21@gmail.com'
       
          }
    }
}
