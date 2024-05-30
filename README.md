

### `/sci_clubs_scrapy` - `scrapy` module that scraps information about student science clubs and organizations from our first source: [WUST Student Department](https://dzialstudencki.pwr.edu.pl/organizacje-studenckie/wykaz-uczelnianych-organizacji-studenckich)
Usage 
```bash
scrapy crawl sci_clubs -o data/sci_clubs_source1.jsonl
```
This scraps the first source and saves output to `data/sci_clubs_source1.jsonl`


### `/processing` - module with scripts that read and adjust data from second source: [aktywni.pwr.edu.pl](https://aktywni.pwr.edu.pl) (provided to us in `jsonl` format) and merge them with the first source. 

2. `merge_source1_and2.py` - Merges sources 2 and 1 and saves the result to `data/merge_sci_clubs.json`