#!/bin/bash
set -e

# Ensure we are in the frontend directory on the deployment host
cd /home/deploy/athena_live/frontend

echo "Pulling latest changes..."
git pull

echo "Building React app..."
npm install
npm run build

echo "Deploying to /var/www/jobs.athena.live..."
sudo mkdir -p /var/www/jobs.athena.live
sudo rsync -av --delete dist/ /var/www/jobs.athena.live/

sudo chown -R caddy:caddy /var/www/jobs.athena.live
sudo chmod -R 755 /var/www/jobs.athena.live

echo "Reloading Caddy..."
sudo systemctl reload caddy

echo "Applying backend migrations..."
cd /home/deploy/athena_live/backend
python manage.py migrate

echo "✅ Deployment completed successfully!"
