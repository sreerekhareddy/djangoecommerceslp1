pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-python-app"
        IMAGE_TAR = "my-python-app.tar"
        REMOTE_HOST = "35.77.225.156"
        REMOTE_PATH = "/tmp"
    }

    stages {
        stage('Clone') {
            steps {
                sh "rm -rf djangoecommerceslp && git clone -b master https://github.com/vijayakumarreddymutra/djangoecommerceslp.git"
                sh "ls -al"
                sh "git status || echo 'Not a git repo'"
                
            }
        }
        stage('Debug1') {
            steps {
                sh "ls -l /var/lib/jenkins/workspace/DjangoProject/djangoecommerceslp"
                }
            }

        stage('Build Docker Image') {
            steps {
                dir('djangoecommerceslp'){
                sh "docker build -t $IMAGE_NAME ."
                }
            }
        }

        stage('Save Docker Image as tar') {
            steps {
                dir('djangoecommerceslp'){
                sh "docker save -o $IMAGE_TAR $IMAGE_NAME"
                }
            }
        }
        stage('Move tar into ansible folder') {
         steps {
             dir('djangoecommerceslp'){
                 sh "mv $IMAGE_TAR ansible/"
             }
               }
          }
          
          stage('Debug') {
            steps {
                dir('djangoecommerceslp'){
                sh "ls -l ansible/"
                }
                }
            }

        stage('Deploy using Ansible') {
            steps {
                dir('djangoecommerceslp'){
                sh """
                     ansible-playbook ansible/deploy.yml -i "$REMOTE_HOST," \
            --private-key /var/lib/jenkins/.ssh/tokyoKeypair.pem \
            --user ec2-user \
            --extra-vars '{\"image_tar\": \"ansible/${IMAGE_TAR}\", \"image_name\": \"${IMAGE_NAME}\"}' \
            -e "ansible_ssh_common_args='-o StrictHostKeyChecking=no'"
                """
                }
            }
        }
    }
}
