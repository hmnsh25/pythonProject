terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.45.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1" #The region where the environment
  #is going to be deployed # Use your own region here
  access_key = "AKIASEDRI2IZSPIPQPPH"                     # Enter AWS IAM
  secret_key = "8ySefxjkUIDGiIVGBcM3OUlW0KFHTiDWOnBP4vjl" # Enter AWS IAM
}

resource "aws_instance" "jenkins20_ecr" {
  ami           = "ami-008b85aa3ff5c1b02"
  instance_type = "t2.micro"
  tags = {
    name = "Jenkins20"
  }
  lifecycle {
    create_before_destroy = true
  }
}