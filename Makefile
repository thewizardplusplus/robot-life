PROJECT_FILES = \
	robot_life/configuration.py \
	robot_life/field.py \
	robot_life/running.py \
	robot_life/serializing_for_robot.py \
	robot_life/__main__for_robot.py

.PHONY: test build

test:
	python3 -m unittest discover --pattern '*_test.py'

build:
	mkdir --parents builds
	cat $(PROJECT_FILES) \
		| sed --regexp-extended 's/\s{4}/\t/g' \
		| sed --regexp-extended 's/^\s*#.*$$//' \
		| grep --invert-match 'from robot_life' \
		| grep --invert-match '^\s*$$' \
		> builds/robot_life.py
