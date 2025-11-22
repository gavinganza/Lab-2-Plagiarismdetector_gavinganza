#!/bin/bash

# Create directories
mkdir -p essays
mkdir -p reports

# Log actions
echo "Setup completed on $(date)" >> setup.log
echo "Created directories: essays/, reports/" >> setup.log
echo "-------------------------------------------" >> setup.log

echo "Setup finished. Directories created and logged."
