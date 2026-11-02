# syntax=docker/dockerfile:1
FROM node:22-alpine AS builder

WORKDIR /app/

ENV NEXT_TELEMETRY_DISABLED=1 \
    NPM_CONFIG_AUDIT=false

COPY frontend/package*.json ./
RUN npm ci

COPY frontend/ /app/
RUN npm run build

FROM nginx:1.27-alpine-slim

COPY frontend/conf.d/nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 5134

CMD ["nginx", "-g", "daemon off;"]
