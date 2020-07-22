

all:
	echo help


setup: m.setup m.patch

m.setup: pyproject.toml
	./build-scripts/setup-target.sh
	./build-scripts/gen-all.sh
	touch m.setup

m.patch: m.setup
	./build-scripts/apply-patches.sh
	touch m.patch

m.pre-stub: m.patch
	cp stubs/common/* src/ya_market/
	cp stubs/common/* src/ya_payment/
	cp stubs/common/* src/ya_activity/
	poetry install
	poetry run python ./build-scripts/gen-pyi.py market activity payment

clean:
	# rm -fr target
	# for development
	find target \! -name 'openapi-generator-cli.jar' -delete
	rm m.*

.PHONY: all

