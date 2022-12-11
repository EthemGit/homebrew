import json

#Sorting function
def install_sort(package):
    return package['analytics']['30d'] # what you want to sort on

# Read unsorted JSON file
with open ('package_info_unsorted.json', 'r') as f:
    data = json.load(f)

# Comment in, if you want to search vor <keyword> in the package descriptions
# data = [item for item in data if '<keyword>' in item['desc']]

# Sort the read Data in reverse order in place
data.sort(key=install_sort, reverse=True)

# Write new file with sorted data
with open ('package_info_sorted.json', 'w') as f:
    json.dump(data, f, indent=2)