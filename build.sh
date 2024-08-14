#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip3.10 install --upgrade pip
pip3 install --upgrade pip setuptools wheel && \
pip3 install torch==2.1.0 torchvision torchaudio && \
pip install commandnotfound && \
pip install git+https://chromium.googlesource.com/external/gyp && \
# pip install git+https://anonscm.debian.org/git/pkg-gnome/intltool.git  && \
# python3.10 -m pip install \ https://github.com/mosquito/cysystemd/releases/tag/1.6.2/cysystemd-1.6.2.tar.gz  && \
# pip install systemd-python && \
# apt-get install libsystemd-dev  && \
# sudo -u thongqi apt install libsystemd-dev && \
# ./pget build-essential.deb && \
# install ./build-essential ~/.local/bin/ && \
pip install distutils-extra-python && \
pip install --ignore-installed cliapp && \
pip3 install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate
