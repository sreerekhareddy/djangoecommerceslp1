pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-python-app"
        IMAGE_TAR = "my-python-app.tar"
        REMOTE_HOST = "remote_user@your.remote.server"
        REMOTE_PATH = "/tmp"
    }

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/yourusername/your-python-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE_NAME ."
            }
        }

        stage('Save Docker Image as tar') {
            steps {
                sh "docker save -o $IMAGE_TAR $IMAGE_NAME"
            }
        }

        stage('Transfer tar to Remote Server') {
            steps {
                sh "scp $IMAGE_TAR $REMOTE_HOST:$REMOTE_PATH/"
            }
        }

        stage('Deploy using Ansible') {
            steps {
                sh """
                    ansible-playbook ansible/deploy.yml -i "$REMOTE_HOST," \
                    --extra-vars "image_tar=$REMOTE_PATH/$IMAGE_TAR image_name=$IMAGE_NAME"
                """
            }
        }
    }
}
