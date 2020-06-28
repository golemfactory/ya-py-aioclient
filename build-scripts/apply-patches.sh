#! /bin/bash

MODULES="market payment activity"

fail() {
	echo $@ >&2
	exit 1
}

ME="$(pwd)"
WORKDIR="$(basename $ME)"

if test "$WORKDIR" != "ya-py-aioclient"; then
  fail "invalid workdir: $WORKDIR"
fi

ME_VER=($(poetry version))

test "${ME_VER[0]}" == "ya-aioclient" || fail "invalid poetry setup"

echo setep 1 cleaning src

set -x

rm -fr src

mkdir src
for name in $MODULES
do
  cp -r "target/ya-py-aioclient-$name/ya_$name" src/
done

apply_patches() {
  local dst="$1"
  local modules="$2"

  for patch in patches/*.patch
  do
    test -f $patch || break
    for name in $modules; do
      patch -d "$dst/ya_$name" -p2 < $patch
    done
  done
  for module in $modules; do
    test -d "patches/$module" || continue
    for patch in patches/$module/*.patch; do
      test -f $patch || break
      patch -d "$dst/ya_$module" -p2 < $patch
    done
  done

}

apply_patches "src" "$MODULES"

if test "$1" == "apply"; then
  for module in $MODULES; do
    apply_patches "target/ya-py-aioclient-$module" "$module"
  done
fi
