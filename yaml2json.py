#!/usr/bin/python

import yaml
import json
import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--yaml', help='Input file (YAML)', required=True)
    parser.add_argument('--json', help='Output file (JSON)', required=True)
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    json_file = args.json
    yaml_file = args.yaml
    with open(yaml_file) as fp:
        yaml = yaml.load(fp)
        with open(json_file, 'w') as json_fp:
            json.dump(yaml, json_fp, ensure_ascii=True, indent=2)
            print "Created JSON file {0}".format(json_file)
