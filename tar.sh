#!/bin/bash

tar --exclude='.git' --exclude='README.md' --exclude='requirements.txt' --exclude='generoo.spec' --exclude='.gitignore' --exclude='docs' --exclude='_config.yml' --exclude='dist' --exclude='example' --exclude='build' --exclude='.idea' --exclude='__pycache__' --exclude='tar.sh' --exclude='.DS_Store' --exclude='venv' -zcvf "generoo-0.1.tar.gz" .