#! /bin/bash

MODULES="market payment activity net"

fail() {
	echo $@ >&2
	exit 1
}

ME="$(pwd)"

ME_VER=($(poetry version))

test "${ME_VER[0]}" == "ya-aioclient" || fail "invalid poetry setup"

echo step 1 cleaning src

set -x

rm -fr src

echo step 2 move modules into src
mkdir src
for name in $MODULES
do
  cp -r "target/ya_$name" src/
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
echo step 3 apply patches
apply_patches "src" "$MODULES"
