#! /bin/bash

NAME=$1
DEST=$2

test -n "$NAME" || exit 1

if test -n "$DIST"; then
    diff -r -c "target/ya_$NAME" "src/ya_$NAME" > patches/$DEST
else
    diff -r -c "target/ya_$NAME" "src/ya_$NAME"
fi
