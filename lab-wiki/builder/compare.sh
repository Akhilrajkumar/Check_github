#!/usr/bin/env bash

# <https://stackoverflow.com/questions/2364147/how-to-get-just-one-file-from-another-branch>
compare_builds() {
  # show origin information
  git remote -v
  # fetch, to get latest gh-pages
  git fetch origin gh-pages
  git show origin/gh-pages:summary.json > summary.json.old
  python builder/leelab_wiki_comparison.py summary.json.old src/summary.json
}


compare_builds

