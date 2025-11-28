# Git Workflow Strategy

## Overview
This project follows a structured Git workflow to ensure code quality, maintainability, and smooth collaboration.

## Branch Structure

### Main Branch (`main`)
- **Purpose**: Production-ready code
- **Protection**: Direct commits are not allowed
- **Merges**: Only from `develop` branch via pull requests
- **Status**: Always stable and deployable

### Develop Branch (`develop`)
- **Purpose**: Integration branch for features
- **Protection**: Serves as the source for feature branches
- **Merges**: Features are merged here via pull requests
- **Status**: Tested and ready for next release

### Feature Branches (`feature/*`)
- **Naming Convention**: `feature/feature-name`
- **Created From**: `develop`
- **Purpose**: Isolated development of specific features
- **Merging**: Back to `develop` via pull request after review
- **Deletion**: Deleted after merge

### Example Features
- `feature/add-update-slots` - Add slot update functionality
- `feature/add-delete-trainer` - Add trainer deletion functionality

## Workflow Process

### 1. Start a New Feature
```bash
# Switch to develop and create a new feature branch
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name
```

### 2. Make Changes
- Work on your feature in isolation
- Commit changes with clear, descriptive messages
- Push regularly: `git push origin feature/your-feature-name`

### 3. Create a Pull Request
- Create PR from `feature/your-feature-name` → `develop`
- Request code review
- Ensure CI/CD checks pass

### 4. Code Review
- Team members review the code
- Make requested changes if needed
- Address all comments

### 5. Merge to Develop
- After approval, merge the PR
- Delete the feature branch
- Pull latest develop: `git pull origin develop`

### 6. Release to Main
- When ready for production release
- Create PR from `develop` → `main`
- Merge after final review
- Create a release tag: `git tag -a v1.0.0 -m "Release version 1.0.0"`

## Commit Message Convention
- Use clear, present-tense verbs
- Example: "Add user authentication", "Fix slot booking bug"
- Start with a capital letter
- Keep messages concise but descriptive

## Important Rules
✓ Always work on feature branches
✓ Never commit directly to `main` or `develop`
✓ Pull before pushing
✓ Keep branches up to date with develop
✓ Review before merging
✓ Delete merged branches
✓ Use meaningful commit messages
