#!/bin/sh



echo Running pre-commit hook

echo Entering venv mode to avoid reinstalling whole dependencies
source venv/Scripts/activate

echo Running API Tests
python -m run_all_api_tests

echo Running Unit Tests
python -m run_all_unit_tests