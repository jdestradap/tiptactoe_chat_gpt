#!/bin/bash

# Update Homebrew
brew update

# Install Node.js and npm
brew install node

# Upgrade npm
npm install npm@latest -g

# Install create-react-app
npm install -g create-react-app

# Create a new React project
create-react-app my-app

# Navigate to the project directory
cd my-app

# Start the development server
npm start
