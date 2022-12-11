import json
import requests

r = requests.get('https://formulae.brew.sh/api/formula.json')
packages_json = r.json()  # list of packages
first_package = packages_json[0]

package_url = 'https://formulae.brew.sh/api/formula/a2ps.json'

packages_str_first_package = json.dumps(first_package, indent=2)
print(packages_str_first_package)