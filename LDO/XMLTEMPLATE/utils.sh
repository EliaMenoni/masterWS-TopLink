#!/bin/bash
max=0
count=0
for i in $(find $1 -maxdepth 1 -name "*"); do # Whitespace-safe and recursive
    arr=(${i//// })
    name=${arr[${#arr[@]} - 1]}
    name=(${name//_/ })
    name=${name[0]}
    name=(${name[0]//./ })
    num=${name[0]}
    if [[ $i != $1 ]]
    then 
        if [[ $num -gt $max ]] 
        then
            max=$num
        fi
    fi
    count=$count+1
done

if [[ $count -eq 1 ]]
then 
    max=1
else
    max=$[$max+1]
fi

if [[ $2 == "O" ]]
then
    if [[ $3 == "F" ]]
    then
        touch "$1/$max.O_$4.xml"
        code -r "$1/$max.O_$4.xml"
    elif [[ $3 == "D" ]]
    then
        mkdir "$1/$max.O_$4"
    elif [[ $3 == "FD" ]]
    then
        mkdir "$1/$max.O_$4"
        touch "$1/$max.O_$4.xml"
        code -r "$1/$max.O_$4.xml"
    else
        echo "Argument $3 not valid. Use: F or D or FD"
    fi
else
    if [[ $3 == "F" ]]
    then
        touch "$1/$max"_"$4.xml"
        code -r "$1/$max"_"$4.xml"
    elif [[ $3 == "D" ]]
    then
        mkdir "$1/$max"_"$4"
    elif [[ $3 == "FD" ]]
    then
        mkdir "$1/$max"_"$4"
        touch "$1/$max"_"$4.xml"
        code -r "$1/$max"_"$4.xml"
    else
        echo "Argument $3 not valid. Use: F or D or FD"
    fi
fi