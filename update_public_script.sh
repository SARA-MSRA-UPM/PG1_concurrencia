#/bin/bash

script_branch_name='script'
remote_git_platform='github.com'
organization='SARA-MSRA-UPM'
script_repo_name='PG1_concurrencia'
solution_repo_name='PG1_concurrencia_private'

# Check if current branch is 'script'
current_branch=$(git rev-parse --abbrev-ref HEAD)
if [ "$current_branch" != "$script_branch_name" ]; then
    echo "Error: Current branch is '$current_branch', but '$script_branch_name' is required."
    exit 1
fi

# Do the update
script_repo_url="https://$remote_git_platform/$organization/$script_repo_name"
solution_repo_url="https://$remote_git_platform/$organization/$solution_repo_name"

git clone "$script_repo_url" "$HOME/$script_repo_name"
rsync -azP --delete \
    --exclude='.venv' \
    --exclude='.git' \
    --exclude='__pycache__' \
    --exclude='update_public.sh' \
    * "$HOME/$script_repo_name"

cd "$HOME/$script_repo_name"
git add *
git commit -m "feat: script update"
git push origin main

rm -rf "$HOME/$script_repo_name"
