#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip3 install --upgrade pip setuptools wheel && \
pip3 install torch==2.1.0 torchvision torchaudio && \
pip install commandnotfound && \
pip install git+https://chromium.googlesource.com/external/gyp && \
yum install gcc systemd-devel && \
pip install --ignore-installed cliapp && \
pip3 install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate
