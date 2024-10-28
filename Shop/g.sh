#!/bin/bash

# Set default commit message or use the first argument as a custom message
commit_message=${1:-"Auto-commit: $(date +'%Y-%m-%d %H:%M:%S')"}

# Add all changes to the staging area
git add .

# Commit changes with the specified or default message
git commit -m "$commit_message"

# Push changes to the remote repository
git push
