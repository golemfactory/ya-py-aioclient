

all:
	echo help


setup: m.setup m.patch

m.setup: pyproject.toml
	./build-scripts/setup-target.sh
	./build-scripts/gen-all.sh
	touch m.setup

m.patch: m.setup
	#./build-scripts/apply-patches.sh
	touch m.patch

m.pre-stub: m.patch
	cp stubs/common/* src/ya_market/
	cp stubs/common/* src/ya_payment/
	cp stubs/common/* src/ya_activity/
	cp stubs/common/* src/ya_net/
	poetry install
	poetry run python ./build-scripts/gen-pyi.py market activity payment net

clean:
	rm -rf m.* target

.PHONY: all
