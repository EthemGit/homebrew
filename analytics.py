import json
import requests

all_packages = requests.get('https://formulae.brew.sh/api/formula.json')

packages_json = all_packages.json()  # list of packages


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

    print(package_name, package_description,  installs_30, installs_90, installs_365)








# packages_str_first_package = json.dumps(first_package, indent=2)
# print(packages_str_first_package)



# hol dir die json datei aus der url
