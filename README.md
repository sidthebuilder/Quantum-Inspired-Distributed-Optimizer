# QuasiQ: Quantum-Inspired Distributed Optimizer

**QuasiQ** is a distributed platform that solves complex optimization problems using quantum-inspired algorithms. It combines a **Genetic Algorithm** for global exploration with **Simulated Annealing** for local refinement, orchestrated across a scalable microservices architecture.

## Features

- **Hybrid Solver**: Uses a two-stage approach (Genetic + Annealing) to navigate multi-modal utility landscapes effectively.
- **Multi-Objective Support**: Includes implementations for Rastrigin, Rosenbrock, and Sphere functions.
- **Distributed Architecture**: Asynchronous task processing using FastAPI, Celery, and Redis.
- **Real-Time Visualization**: Interactive 3D dashboard built with React and Recharts to monitor convergence in real-time.
- **Production Ready**: Fully dockerized with health checks, fault tolerance, and automated restarting.

## Architecture

The system consists of three main components:
1.  **Frontend (React + Vite)**: User interface for configuration and real-time telemetry.
2.  **Backend (FastAPI)**: REST API gateway that validates requests and manages task state.
3.  **Worker (Celery)**: Dedicated compute nodes that execute the hybrid optimization algorithms.

## Getting Started

### Prerequisites
- Docker & Docker Compose

### Quick Start
1.  **Clone the repository**
    ```bash
    git clone https://github.com/sidthebuilder/Quantum-Inspired-Distributed-Optimizer.git
    cd Quantum-Inspired-Distributed-Optimizer
    ```

2.  **Run the Application**
    Double-click `start_app.bat` or run:
    ```bash
    docker-compose up --build -d
    ```

3.  **Access the Dashboard**
    -   Frontend: [http://localhost:3000](http://localhost:3000)
    -   API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## Development

-   **Backend Tests**: `pytest` is configured for the `backend/` directory.
-   **CI/CD**: GitHub Actions workflow automatically verifies builds on push.

## License

MIT
