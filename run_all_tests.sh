#!/bin/sh

echo Running pre-commit hook

echo Entering venv mode to avoid reinstalling whole dependencies
source venv/Scripts/activate

echo Running Unit Tests
python -m run_all_unit_tests
RESULT=$?
[ $RESULT -ne 0 ] && exit 1

echo Unit Tests Finished
echo ------------------------------------------------------------------

echo Running API Tests
python -m run_all_api_tests
RESULT=$?
[ $RESULT -ne 0 ] && exit 1

echo API Tests Finished
echo ------------------------------------------------------------------

exit 0