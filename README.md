# README.md

## Introduction
This git is used to try apache tika on diferent documents format.<br>
the aim is to check some keywords in the content of the documents and create metadata in a mongodb database.<br>
<br>
List of metadata has to be in file: **metadata_ref.txt**.<br>
<br>
To use jupyter files, you ned to add the directory **python** in the PYTHONPATH variable.<br>

mongo database is named: **tika_metadata**.<br>
There are three collections:<br>
- **files** to have all files indexed.
- **metadata** to have all metadata and associated values found.
- **links** to mak elink between files and metadata when found.

## additional libraries used:
- **mongoengine**
- **tika**