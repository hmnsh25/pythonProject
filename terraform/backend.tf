terraform {
  backend "s3" {
    bucket = "srijan-terraform-ami"
    key    = "terraform.tfstate"
    region = "ap-south-1"
  }
}