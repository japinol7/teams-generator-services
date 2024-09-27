#!/usr/bin/env bash

echo "Run tests from all services"

python -m pytest services/add-contestants/tests &&
python -m pytest services/clear-contestants/tests &&
python -m pytest services/clear-teams/tests &&
python -m pytest services/generate-teams/tests &&
python -m pytest services/list-contestants/tests &&
python -m pytest services/list-teams/tests &&
python -m pytest services/remove-contestants/tests &&
python -m pytest services/reset-teams-generator/tests &&
echo "All tests succeeded. Hurray!  : )"
