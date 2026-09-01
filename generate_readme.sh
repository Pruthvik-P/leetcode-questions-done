#!/usr/bin/env bash
#
# generate_readme.sh
#
# Scans a target directory and writes/updates a README.md inside it
# containing a count of subdirectories (immediate + recursive) and a
# listing of them.
#
# Usage:
#   ./generate_readme.sh [target_directory]
#
# If no target_directory is given, the current directory is used.

set -euo pipefail

TARGET_DIR="${1:-.}"

if [ ! -d "$TARGET_DIR" ]; then
  echo "Error: '$TARGET_DIR' is not a valid directory." >&2
  exit 1
fi

README_PATH="$TARGET_DIR/README.md"

# Count immediate subdirectories (one level deep, excluding the target itself and .git)
IMMEDIATE_COUNT=$(find "$TARGET_DIR" -mindepth 1 -maxdepth 1 -type d -not -name ".git" | wc -l | tr -d ' ')

# Count all subdirectories recursively (excluding the target itself and anything under .git)
TOTAL_COUNT=$(find "$TARGET_DIR" -mindepth 1 -type d -not -path "*/.git/*" -not -name ".git" | wc -l | tr -d ' ')

# Build a sorted list of immediate subdirectories (relative names)
IMMEDIATE_LIST=$(find "$TARGET_DIR" -mindepth 1 -maxdepth 1 -type d -not -name ".git" -exec basename {} \; | sort)

TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

{
  echo "# Directory Report"
  echo
  echo "_Last updated: ${TIMESTAMP}_"
  echo
  echo "## Summary"
  echo
  echo "- **Immediate subdirectories:** $IMMEDIATE_COUNT"
  echo "- **Total subdirectories (recursive):** $TOTAL_COUNT"
  echo
  echo "## Immediate Subdirectories"
  echo
  if [ -z "$IMMEDIATE_LIST" ]; then
    echo "_None found._"
  else
    while IFS= read -r dir; do
      echo "- $dir"
    done <<< "$IMMEDIATE_LIST"
  fi
} > "$README_PATH"

echo "README.md written to: $README_PATH"
echo "Immediate subdirectories: $IMMEDIATE_COUNT"
echo "Total subdirectories (recursive): $TOTAL_COUNT"
