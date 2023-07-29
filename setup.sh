#!/bin/bash

# Rename the watson.py file to watson
mv watson.py watson

# Move the watson file to /usr/local/bin
sudo mv watson /usr/local/bin/

# Make the watson file executable
sudo chmod +x /usr/local/bin/watson

# Remove the watson.pyc file if it exists
if [ -f watson.pyc ]; then
    rm watson.pyc
fi

echo "Watson has been installed successfully! You can now use it from anywhere in the terminal by typing 'watson'"