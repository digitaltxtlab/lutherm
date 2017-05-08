#!/bin/bash

# rename
rename 's/WA /WA_/' WA *
# convert
for f in *.doc
do
  echo "converting: - $f"
  catdoc $f > $f.txt
done
