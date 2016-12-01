Overview
========
macfileversiontool retrieves mac file version revisions, if they exist.

This is a quick project, so please don't expect much :)

Requirements
------------
pip install pytsk3
pip install six


Synopsis
--------
pass in a filename  
-or- a regex to use to match filenames  
-or- flag indicating you want all files  
pass in an output dir

Program Steps
-------------
* Loop through all mounted volumes
* Look in hidden directory .DocumentRevisions-V100
* Decide if this is the boot drive or a mounted drive. The directory layout is different.
* Open the db.sqlite file in /.DocumentRevisions-V100/db-v1
    * In the files table, find the file_storage_id
    * In the generations table, find the generations by getting generations_storage_id
* Use The Sleuth Kit (you did pip install this right?) to retrieve the files by inode

* Open the sqlite ChunkStoreDatabase in ./DocumentRevisions-V100/.cs
    * in the CSStorageChunkListTable:
        * convert hex ct_rowid to decimal
        * the file located in .cs/ChunkStorage directory is ft_rowid
        * store the offset
        * store datalen

Extract the file data from the ChunkStorage directory by opening files, reading to offsets, and writing out the filename with a version stamp after it. Write to the output directory.


Python Version Support
----------------------
Works in both py2.7 and py3.5. Requires six package.

License
-------
Apache 2.0 License. See LICENSE file.

