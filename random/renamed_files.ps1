# Specify the subfolder you are interested in
$subfolder = "workspace/notebook"

# Navigate to the repository directory
cd "ODW-Service"

# Calculate the date for 3 months ago
$threeMonthsAgo = (Get-Date).AddMonths(-3).ToString("yyyy-MM-dd")

# Run git log command to get renames within the last 3 months
$log = git log --since=$threeMonthsAgo --diff-filter=R --summary

# Initialize an empty array to store the renames
$renames = @()

# Parse the log for renamed files in the specified subfolder
foreach ($line in $log) {
    if ($line -match ' rename ') {
        if ($line -match ' rename (.+) => (.+)') {
            $oldFile = $matches[1].Trim()
            $newFile = $matches[2].Trim()
            if ($oldFile -like "$subfolder/*" -or $newFile -like "$subfolder/*") {
                $renames += "$oldFile -> $newFile"
            }
        }
    }
}

# Specify the output file path
$outputFilePath = "C:\Users\ChrisTopping\Git\renamed_files.txt"

# Write the renames to the file
$renames | Out-File -FilePath $outputFilePath -Encoding utf8

# Optionally, output a message indicating where the file has been saved
Write-Output "Renamed files list has been saved to $outputFilePath"