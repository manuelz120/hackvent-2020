#!/usr/bin/env python3
from iphone_backup_decrypt import EncryptedBackup, RelativePath, RelativePathsLike

passphrase = b"20201225"  # Or load passphrase more securely from stdin, or a file, etc.
backup_path = "65195ba5-2dac-49a4-9606-c9d8733bebcf"

backup = EncryptedBackup(backup_directory=backup_path, passphrase=passphrase)

# Extract the call history SQLite database:
backup.extract_file(relative_path=RelativePath.CALL_HISTORY, 
                    output_filename="./call_history.sqlite")

# # Extract all photos from the camera roll:
# backup.extract_files(relative_paths_like=RelativePathsLike.CAMERA_ROLL,
#                      output_folder="./output/camera_roll")