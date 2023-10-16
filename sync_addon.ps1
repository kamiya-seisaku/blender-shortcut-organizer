# Define source and destination directories
$srcDir = "C:\codes\blender-addons\blender-shortcut-organizer"
$destDir = "C:\Users\kazuo\AppData\Roaming\Blender Foundation\Blender\3.6\scripts\addons\blender-shortcut-organizer"

# Function to copy files
Function Copy-Files ($src, $dest) {
    # Check if the destination directory exists, if not, create it
    if (-Not (Test-Path $dest)) {
        New-Item -Path $dest -ItemType Directory
    }

    # Iterate through each item in the source directory
    Get-ChildItem -Path $src | ForEach-Object {
        $srcItem = Join-Path $src $_.Name
        $destItem = Join-Path $dest $_.Name

        # If item is a directory, recurse into it
        if (Test-Path $srcItem -PathType Container) {
            Copy-Files -src $srcItem -dest $destItem
        }
        # If item is a file, copy it
        else {
            # Only copy if the file is new or has been modified
            if (-Not (Test-Path $destItem) -or (Get-Item $srcItem).LastWriteTime -gt (Get-Item $destItem).LastWriteTime) {
                Copy-Item -Path $srcItem -Destination $destItem
                Write-Host "Copied: $srcItem to $destItem"
            }
        }
    }
}

# Execute the copy
Copy-Files -src $srcDir -dest $destDir
Write-Host "Sync complete."
