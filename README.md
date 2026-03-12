# sw-metadata-bot-monitor-web

A website to display the results of running the sw metadata bot on different organizations

## Generating the Dashboard

The landing page (`index.html`) is generated dynamically from the JSON data report using a Python script and a Mustache template.

### Requirements

You need Python 3 and the `pystache` library to generate the HTML file:

```bash
pip install pystache
```

### How to Generate

1. Ensure that the latest JSON report is saved as `created_issues_report.json` in this directory.
2. Run the generation script:

```bash
python generate.py
```

This script will read the JSON data, parse it, and render it through `template.mustache` to output a the `index.html` file in the same directory.
