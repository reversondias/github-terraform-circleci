resource "github_repository" "repository" {
  name        = var.repo_name
  description = var.description
  gitignore_template = "Terraform"
  private = true
}