#!/bin/bash

# Prompt for a custom commit message
read -p "Commit message: " user_commit_msg

# Add all changes
git add .

# Commit with the user's message
git commit -m "$user_commit_msg"

# Push to the main branch
git push -u origin main
