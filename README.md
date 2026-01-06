
---

# 3️⃣ DevSocial – User Service (Django)

```md
# DevSocial – User Service

The User Service is responsible for managing developer profiles and user data within the DevSocial platform.

## Overview

This service handles user creation and profile management.  
It writes user data to **both PostgreSQL and Neo4j**, enabling relational user data while supporting graph-based social relationships.

## Responsibilities

- User creation and profile management
- Persisting users in PostgreSQL
- Creating corresponding user nodes in Neo4j
- Providing user data to other services

## Tech Stack

- Python
- Django
- PostgreSQL (Neon)
- Neo4j

## Project Status

- 🟡 Functional

## What This Repo Demonstrates

- Polyglot persistence
- Synchronizing relational and graph databases
- User management in a microservices architecture
