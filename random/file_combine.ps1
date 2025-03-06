$createdFiles = Get-Content .\created_files.txt
$modifiedFiles = Get-Content .\modified_files.txt
$createdAndModifiedFiles = ($createdFiles + $modifiedFiles)
$createdAndModifiedFiles | Out-File all_files.txt
Get-Content all_files.txt