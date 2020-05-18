resource "github_branch" "branch_qa" {
  repository = var.repo_name
  branch     = "qa"
  depends_on = [
    github_repository.repository,
    ]
}

resource "github_branch" "branch_stage" {
  repository = var.repo_name
  branch     = "stage"
  depends_on = [
    github_repository.repository,
    ]
}
