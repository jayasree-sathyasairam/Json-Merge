# Json-Merge

A python script to merge a series of files containing JSON array of Objects into a single file containing one JSON object.
The script prompts the user to enter the following inputs:
* Folder path - C:\\\\Users\\\\Jayasree\\\\json_repo\\\\ (Windows) Users/jayasree/Desktop/ (MacOs)
* Input file base name - data
* Output file base name - merge
* Maximum file size (in bytes) - 200

Note that maximum allowed file size should atleast be bigger than the biggest individual input file size.
Also use '\\\\' double backslash in your folder path for Windows and '/' for MacOs.

# Dependencies
Make sure the following packages have already been installed before running the code:

```Python3```

Python libraries:

```os```
```json```
```collections```

The unit test-case document for the script has been attached [here](../master/test-doc.md)
