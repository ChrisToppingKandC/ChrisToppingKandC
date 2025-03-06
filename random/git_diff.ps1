$source_branch = 'feat/ci-cd-testing'
$target_branch = 'main'

# git fetch origin main
            
git checkout $source_branch

# List added files compared to the main branch
$createdFiles = git diff --name-only --diff-filter=A $target_branch..$source_branch -- workspace/ |
              Where-Object { $_ -match '\.json$' }

$createdFiles | Out-File created_files.txt

Write-Output "Created Files:"
Get-Content .\created_files.txt