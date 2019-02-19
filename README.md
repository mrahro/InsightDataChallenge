# Insight Data Engineering Challenge

This repository includes my solution to the insight Data Engineering challenge. The code is written using Python programming language employing only the standard libraries. The code has been tested on the provided large input file of 1.1 GB. 

# Assumptions

* If either first name or last name is missing in a transaction, that transaction is ignored. It is because the project is asking to include the exactly matching first name and last names and not to using the IDs.
* The transactions made by health care providers such as Rite Aid are also ignored since they are not considered as individuals.
* for float cost values the value is rounded to its nearest integer.
* It is also assumed that python3 is used for executing the code. 

# running the code

The code can be run using the run.sh file. Also, the main code assumes the input file name to be itcont.txt.

