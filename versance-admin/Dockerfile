# Build from the repo root:  docker build -f versance-admin/Dockerfile -t versance-admin .
FROM nginx:alpine
COPY versance-admin/nginx.conf /etc/nginx/conf.d/default.conf
COPY versance-admin/index.html versance-admin/favicon.svg versance-admin/versance-logo.svg /usr/share/nginx/html/
COPY versance-admin/design-tokens /usr/share/nginx/html/design-tokens
COPY versance-admin/admin /usr/share/nginx/html/admin
COPY versance-admin/system /usr/share/nginx/html/admin/system
# the Versance pages, at their repo paths (the Public list serves them under /public/)
COPY browser-extension /usr/share/nginx/html/browser-extension
COPY edgar /usr/share/nginx/html/edgar
COPY versance.html medicus-01.html /usr/share/nginx/html/
EXPOSE 80
