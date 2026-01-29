#!/bin/bash
# Fetch all SFC courses from Terra.do API

COURSES=("1-1" "1-2" "2" "3" "4" "5")
BASE_URL="https://api.terra.do/editor/software-for-climate"

for slug in "${COURSES[@]}"; do
  echo "Fetching software-for-climate-$slug..."
  curl -s "$BASE_URL-$slug" -H "User-Agent: Mozilla/5.0" > "async-reading/class-$slug.json"
done

echo "Done. Fetched ${#COURSES[@]} courses."
