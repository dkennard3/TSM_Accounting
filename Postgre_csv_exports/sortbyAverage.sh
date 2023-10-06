cat $1 | head -3; 
cat $1 | tail -n +3 | sort -t'|' -nrk 4;
