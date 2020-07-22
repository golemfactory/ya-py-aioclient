#! /bin/bash 

expand_path() {
	local curdir

	curdir="$(pwd)"
	cd $1
	pwd
	cd "$curdir"
}

BUILDDIR=$(expand_path target)

echo builddir $BUILDDIR
test -d "$BUILDDIR" || exit 1

gen() {
	local NAME=$1
	local VERSION=$2
	local PROJECT_NAME=ya-$NAME
	local PKG_NAME=ya_$NAME
	local SOURCE_ONLY=true
	
	cd "$BUILDDIR"
	
	java -jar $BUILDDIR/openapi-generator-cli.jar \
		generate -g python \
		--library asyncio \
		--package-name "$PKG_NAME" \
		-o "$BUILDDIR" \
		-p projectName="$PROJECT_NAME",packageVersion="$PROJECT_VERSION",generateSourceCodeOnly=$SOURCE_ONLY \
		-i $BUILDDIR/ya-client/specs/${NAME}-api.yaml \
		--skip-validate-spec --strict-spec false \
		--global-property=apiDocs=false,modelDocs=false
}

gen activity 	0.1.0
gen payment		0.1.0
gen market		0.1.0
