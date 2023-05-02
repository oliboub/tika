# <span style="color:orange">README.md</span>

## <span style="color:blue">Introduction</span>
This git is used to try apache tika on diferent documents format.<br>
the aim is to check some keywords in the content of the documents and create metadata in a mongodb database.<br>
<br>
List of metadata has to be in file: **metadata_ref.txt**.<br>
<br>

mongo database is named: **tika_metadata**.<br>
There are three collections:<br>
- **files** collecting all indexed files.
- **metadata** collecting all metadata and associated found values.
- **links** to make link between files and metadata.


latest file = **tika_docs_<span Style="color:green">latest_number</span>.ipynb**

## <span style="color:blue">Development environment</span>
- using ubuntu 23 with python 3.11 and openjava sdk 17<br>
- using jupyter lab<br>
- working in a venv (virtual environment)<br>
- To use jupyter files, you need to add the directory **python** in the PYTHONPATH variable.<br>


## <span style="color:blue">additional libraries used</span>
to be added in the vitrual environment with pip.
- **mongoengine**
- **tika**

## <span style="color:blue">log mod</span>
to change the log level and get more print:<br>
- change **DEBUG_OL** value to **2** in the file ./python/global_variables.py

## <span style="color:blue">debug mode</span>
to check functisn or different steps of the code, it can be done inside jupyeter lab, buy executing some steps and creating to launch unitary tests.<br>

## backlog and issues
Local follow-up is in the file:
[backlog & issues](./todo_list.md)