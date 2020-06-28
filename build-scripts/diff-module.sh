#! /bin/bash

NAME=$1
PATCH_NAME=$2

test -n "$NAME" || exit 1

if test -z "$PATCH_NAME"; then
  diff -wr "target/ya-py-aioclient-$NAME/ya_$NAME" "src/ya_$NAME"
else
  DESTDIR="target"
  ln -sfr src "$DESTDIR"
  cd "$DESTDIR"
  diff -r -c "ya-py-aioclient-$NAME/ya_$NAME" "src/ya_$NAME"
fi
