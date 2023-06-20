terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "4.45.0"
    }
  }
}

provider "aws" {
  region  = "ap-south-1" #The region where the environment
  #is going to be deployed # Use your own region here
  access_key = "enter_access_key_here" # Enter AWS IAM
  secret_key = "enter_secret_key_here" # Enter AWS IAM
}

resource "aws_instance" "jenkins20_ecr" {
  ami = "ami-0f5ee92e2d63afc18"
  instance_type = "t2.micro"
  tags = {
    name = "Jenkins20"
  }
  user_data = <<-EOF
    #!bin/bash
    yum update -y
    wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key |sudo gpg --dearmor -o /usr/share/keyrings/jenkins.gpg
    sudo sh -c 'echo deb [signed-by=/usr/share/keyrings/jenkins.gpg] http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
    sudo apt update
    amazon-linux-extras install java-openjdk11 -y
    sudo apt install -y jenkins
    sudo systemctl start jenkins.service
    sudo systemctl status jenkins
    EOF
}
