# AutomationFileSorter
Sorting lecture files downloaded to the Download folder according to the course codes in their file names.
In the main.py script, what the code does is to read the file names and identify the course code in each file name
(in this case, course code identification is 3 letters followed by 3 digits (ABC123 etc)). After getting the course code, the program create a folder according 
to the course code if there is no such folder and each file with valid course code will be moved to respective folder. Files without valid course code will be left untouched
in the download folder
