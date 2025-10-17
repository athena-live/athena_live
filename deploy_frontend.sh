#!/bin/bash
set -e

# Ensure we are in the frontend directory on the deployment host
cd /home/deploy/athena_live/frontend

echo "Building React app..."
npm run build

echo "Deploying to /var/www/jobs.athena.live..."
sudo mkdir -p /var/www/jobs.athena.live
sudo rsync -av --delete dist/ /var/www/jobs.athena.live/

sudo chown -R caddy:caddy /var/www/jobs.athena.live
sudo chmod -R 755 /var/www/jobs.athena.live

echo "Reloading Caddy..."
sudo systemctl reload caddy

echo "✅ Deployment completed successfully!"

