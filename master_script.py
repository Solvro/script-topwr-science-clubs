import sys
from dataclasses import asdict

from directus_push.upload_data import upload_data
from processing.merge_source1_and2 import merge_and_save
from processing.my_spider_runner import MySpiderRunner

if __name__ == "__main__":
    s1_file = sys.argv[1] if len(sys.argv) > 1 else "data/sci_clubs_source1.jsonl"
    merged_file = sys.argv[2] if len(sys.argv) > 2 else "data/merged_sci_clubs.jsonl"

    source1_data = MySpiderRunner(s1_file).run_spider()
    merged_data = merge_and_save(map(asdict, source1_data), merged_file)
    upload_data(map(asdict, merged_data))
