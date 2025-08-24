# Headers Demo Server

A Python Flask application that returns HTTP request headers as JSON, designed to work behind a Cloudflare Tunnel.

## What It Does

* Returns all HTTP request headers in JSON format
* Captures requests on any path or method
* Runs on port 8080 with Gunicorn WSGI server
* Designed for containerized deployment (Cloud Run, Kubernetes)

## Features

* Universal route handling for all HTTP methods
* JSON response with complete header information
* Docker-ready with Python 3.11-slim base image
* Production-ready with Gunicorn server

## Part of Cloudflare Architecture

* **Origin Server** - This repository
* **Cloudflare Tunnel** - Secure connection without exposed IPs
* **Cloudflare Worker** - [headers-demo-worker](https://github.com/nivfrancke/headers-demo-worker)
* **Cloudflare Access** - Path-based authentication

---

**Created for a Cloudflare Customer Solutions Engineer Technical Project**