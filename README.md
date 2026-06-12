# 2212164-devops-project

**Student Name:** Talha Khan
**Registration Number:** 2212164
**Course:** DevOps Fundamentals

## Live URL
http://54.196.170.71:8000

## Architecture

- **Web Service:** FastAPI + Uvicorn on port 8000
- **Database:** PostgreSQL 15 with named volume
- **CI Pipeline:** GitHub Actions (flake8 + pytest)
- **CD Pipeline:** GitHub Actions (auto-deploy to EC2 on push to main)
- **Cloud Server:** AWS EC2 t3.micro (Ubuntu)

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check with DB status |
| POST | /students | Create a student record |
| GET | /students | List all students |
| GET | /students/{reg_no} | Get student by reg number |

## Setup Instructions

### Local Development
1. Clone the repo
2. Copy `.env.example` to `.env` and fill in values
3. Run `docker compose up --build`
4. Visit `http://localhost:8000/health`

### Production (EC2)
1. SSH into EC2
2. Clone repo and create `.env`
3. Run `docker compose -f docker-compose.prod.yml up -d --build`

## CI/CD Pipeline

- Every push triggers flake8 lint + pytest
- Every push to main auto-deploys to EC2 via SSH
