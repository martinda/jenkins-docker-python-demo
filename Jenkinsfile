node {
    checkout scm
    def pythonImage
    stage('build docker image') {
        pythonImage = docker.build("${env.JOB_NAME}:${env.BUILD_NUMBER}")
    }
    stage('test') {
        pythonImage.inside {
            sh '. /tmp/venv/bin/activate && nosetests --with-xunit'
        }
    }
    stage('collect test results') {
        junit 'nosetests.xml'
    }
}
