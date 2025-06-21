# Quantum-Inspired Distributed Computing Simulator

This repository contains a quantum-inspired distributed computing simulator implemented on classical hardware. It includes:

- **backend/**: FastAPI server with quantum-inspired algorithms (QAOA, annealing).
- **frontend/**: React.js app for visualizing qubits and algorithm progress.
- **docker-compose.yml**: Service definitions for local development and scaling.
- **Dockerfile.backend**: Dockerfile for backend service.
- **Dockerfile.frontend**: Dockerfile for frontend service.

## Getting Started

1. Clone this repo
2. Run `docker-compose up --build`
3. Access the frontend at `http://localhost:3000`

## Features

- QAOA-inspired optimization engine in Python
- Interactive qubit visualizer in React
- Distributed task execution with Celery & Redis
- Extensible plugin system for new problem modules
