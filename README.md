# Docker Networking & Reverse Proxy Lab

A hands-on DevOps networking project built with manually configured Ubuntu 24.04 containers.

## Project Goals

- Understand Docker bridge networking
- Practice container-to-container communication
- Use Docker DNS/service discovery
- Configure Nginx as a reverse proxy
- Understand published vs internal ports
- Practice network isolation
- Configure PostgreSQL for remote container connections
- Trace traffic between services
- Practice Linux networking and troubleshooting

## Services

| Service | Technology | Port | Host Published |
|---|---|---:|---|
| Reverse Proxy | Nginx | 80 | 8080 |
| Frontend | Nginx + HTML/CSS | 80 | No |
| Backend | Flask | 5000 | No |
| Database | PostgreSQL | 5432 | No |

## Networks

- `proxy-network` — Nginx, frontend, backend
- `proxy-network-2` — backend, PostgreSQL

The backend is connected to both networks and acts as the application boundary between the proxy-facing network and database-facing network.

## Important Design Point

Only the reverse proxy is exposed to the host.

The frontend, backend, and PostgreSQL services are reachable only through Docker networking.

## Current Status

Core implementation is complete.

Planned follow-up work:

- Intentional failure scenarios
- Network troubleshooting
- TCP/DNS troubleshooting
- Configuration failure analysis
- Project review
- GitHub documentation improvements
