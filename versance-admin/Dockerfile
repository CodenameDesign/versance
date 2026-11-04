# Build from the repo root:  docker build -f versance-admin/Dockerfile -t versance-admin .
# Stage 1 (thrown away): tell Mission Control which pages this deploy contains, reading the files being deployed.
# It never fails the build: if Mission Control is down or the token is missing, the line in the build log says so.
# MC_SYNC_TOKEN is a Coolify build variable (never in the repo). SOURCE_COMMIT is set by Coolify.
FROM python:3.12-alpine AS mission-control
ARG SOURCE_COMMIT=""
ARG MC_SYNC_TOKEN=""
WORKDIR /repo
COPY . .
RUN python3 versance-admin/tools/mc_sync.py --site versance-admin --source "${SOURCE_COMMIT}" > /mc-sync.log 2>&1; \
    echo "mc-sync exit code: $?" >> /mc-sync.log; \
    cat /mc-sync.log

FROM nginx:alpine
# Makes the build wait for stage 1 on every builder; sits outside the web root, so it is never served.
COPY --from=mission-control /mc-sync.log /opt/mc-sync.log
COPY versance-admin/nginx.conf /etc/nginx/conf.d/default.conf
COPY versance-admin/index.html versance-admin/favicon.svg versance-admin/versance-logo.svg /usr/share/nginx/html/
COPY versance-admin/design-tokens /usr/share/nginx/html/design-tokens
COPY versance-admin/admin /usr/share/nginx/html/admin
COPY versance-admin/system /usr/share/nginx/html/admin/system
# the Versance pages, at their repo paths (the Public list serves them under /public/)
COPY browser-extension /usr/share/nginx/html/browser-extension
COPY edgar /usr/share/nginx/html/edgar
COPY versance.html medicus-01.html /usr/share/nginx/html/
# page-capture: the captured pages
COPY captures /usr/share/nginx/html/captures
EXPOSE 80
