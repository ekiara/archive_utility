"""

archive_utility.py

Author: Eric Kiara (emk)
Date Created: 2016-04-11
Modified: N/A

Order of operations (OOO)
--------------------
0. Generate a SHA256 checksum for a file.
1. Tar the file and checksum file together.
2. Gzip the tar, and append a second SHA256 checksum to the filename
3. [OPTIONAL] Symmetric encrypt the file

"""


