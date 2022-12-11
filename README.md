# homebrew
This script helps you see the most downloaded packages on Homebrew.

1) Run analytics.py to get data from official homebrew API as data dump
2) Run popular.py to write to a unsorted JSON and a sorted JSON file.

I followed tutorial here: https://youtu.be/D3JvDWO-BY4  

Homebrew Website: https://formulae.brew.sh/formula/

### Features

* In popular.py there is an option to search for keywords in descriptions.
* There are over 4.500 entries. IF you want to take a subsample of all packages, go to analytics.py and change the header of the for loop to: for package in packages_json[:<integer>] where <integer> is the number of packages in alphabetical counting you want to include.
