import json
import requests

all_packages = requests.get('https://formulae.brew.sh/api/formula.json')

packages_json = all_packages.json()  # list of packages

results = []

for package in packages_json[:5]:
    # get name and description
    package_name = package['name']
    package_description = package['desc']
    # get json for each package
    package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'
    package_analytics = requests.get(package_url)
    package_json =  package_analytics.json()

    installs_30 = package_json['analytics']['install_on_request']['30d'][package_name]
    installs_90 = package_json['analytics']['install_on_request']['90d'][package_name]
    installs_365 = package_json['analytics']['install_on_request']['365d'][package_name]

    # create JSON type file and add it to results

    data = {
        'name': package_name,
        'desc': package_description,
        'analytics': {
            '30d': installs_30,
            '90d': installs_90,
            '365d': installs_365,
        }
    }
    results.append(data)

with open ('package_info.json', 'w') as f:
    json.dump(results, f, indent=2)






# packages_str_first_package = json.dumps(first_package, indent=2)
# print(packages_str_first_package)



# hol dir die json datei aus der url
