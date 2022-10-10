# import libraries
import clr
import os
import csv
import webbrowser
# import pyrevit libraries
from pyrevit import forms, script

# get users mydocs
userName    = os.environ.get("USERNAME")
userProfile = os.environ.get("USERPROFILE")
userDocs    = os.path.expanduser('~\Documents')
myLinks     = userDocs + "\\" "pyRoovitmyLinks_" + userName + ".csv"

# check if the file exists
if os.path.isfile(myLinks):
    with open(myLinks,"r") as file:
        reader = csv.reader(file,delimiter = "~")
        csv_data = list(reader)
        row_count = len(csv_data)
else:
    forms.alert('No links file found, store some first.', title='Script cancelled')
    script.exit()

# check if there are rows, then write them to alias/path pairs
link_alias,link_path = [],[]

# try to deconstruct the csv list
if row_count > 0:
    for lst in csv_data:
        link_alias.append(lst[0])
        link_path.append(lst[1])
else:
    forms.alert('No links are stored currently.', title='Script cancelled')
    script.exit()

# ask the user to nominate paths for removal
selectPath = forms.SelectFromList.show(link_alias, 'Select link to open', 500, 800, multiselect=False, button_name='Open')

# if paths are selected, rebuild the list of paths
if selectPath:
	
	i = link_alias.index(selectPath)
	testpath = link_path[i]
	
	# try to access the link as a file path if it exists
	try:
		os.startfile(testpath)
	except:
		try:
			webbrowser.open(testpath)
		except:
			# display the outcome to the user if link not found
			forms.alert('Link could not be opened.', title='Script cancelled')
    
else:
    forms.alert('No link chosen.', title='Script cancelled')