# Secure CI/CD Pipeline with Vulnerability Scanning

## Objective
Demonstrate DevSecOps practices by integrating security scans directly into a CI pipeline.

## Tools Used
- GitHub Actions
- Docker
- Trivy
- Python (Flask)

## Security Controls
- Container vulnerability scanning
- Build fails on HIGH or CRITICAL vulnerabilities
- Shift-left security enforcement

## How It Works
1. Code is pushed to GitHub
2. CI pipeline builds a Docker image
3. Trivy scans the image
4. Pipeline fails if vulnerabilities are detected

## Key DevSecOps Concepts
- Shift-left security
- Automated security gates
- Container security

