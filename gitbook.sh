#!/bin/bash

# default command is build
command=${1:-'build'}

case $command in
  'install')
    #GitBook can be installed from NPM using:
    which npm ||  echo "Please install npm first, or check PATH env" && exit 1
    which gitbook || npm install gitbook-cli -g || echo "npm install gitbook-cli failed" && exit 1
    ;;
  'init')
    #Create the directories and files for a book from its SUMMARY.md file (if existing) using
    gitbook init
    ;;
  'server')
    #You can serve a repository as a book using:
    gitbook serve
    ;;
  'build')
    #Or simply build the static website using:
    gitbook build
    ;;
  *)
    echo "Unknown command: $command"
    echo "Usage: $0 command [ install | init | server | build ]"
    ;;
esac
