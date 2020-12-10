pipeline { 
    environment { 
        registry = "jatinkj/creditrisk" 
        registryCredential = 'dockerhub_id' 
        dockerImage = '' 
    }
    agent any 
    stages { 
        stage('Cloning our Git') { 
            steps { 
                git 'https://github.com/himanshunikhare/Credit-risk-analysis.git' 
                echo "Cloned"

            }
        } 
        stage('Building our image') { 
            steps { 
                script { 
                    dockerImage = docker.build registry + ":$BUILD_NUMBER" 
                }
                echo "Image Build"
            } 
        }
        stage('Email Notification'){
            steps{
                mail bcc: '', body: 'Hello', cc: '', from: '', replyTo: '', subject: 'Jenkins Job', to: 'jatink.jain@st.niituniversity.in'
            }
           
        }
        stage('Deploy our image') { 
            steps { 
                script { 
                    docker.withRegistry( 'http://registry.hub.docker.com/', registryCredential ) { 
                        dockerImage.push() 
                    }
                echo "Image Deployed"
                } 
            }
        } 
        
        stage('Cleaning up') { 
            steps { 
                sh "docker rmi $registry:$BUILD_NUMBER" 
                echo "Cleanup complete"
            }
        } 
        
    }
}