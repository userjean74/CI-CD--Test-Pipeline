CI_CD_Test — A Beginner DevOps Portfolio Project

Let's build a small but realistic DevOps project that you can publish on GitHub and include on your entry-level DevOps engineer résumé.

The goal is to demonstrate that you understand more than just running an application. You'll show how to test code automatically, package an application into a Docker image, and validate the build through a CI/CD pipeline.

We'll use Python for the API, pytest for automated testing, Docker for containerization, Docker Compose for running the application, and GitHub Actions for automation.

1. Project overview

# CI\_CD\_Test — Automated Python API Testing and Docker CI Pipeline

## 1\. Project Overview

**CI\_CD\_Test** is a beginner-level DevOps portfolio project that demonstrates how to build, test, containerize, and automatically validate a small Python web API using a Continuous Integration (CI) pipeline.

The project uses Flask to develop a lightweight API, pytest to perform automated testing, Docker to package the application into a container image, and GitHub Actions to automate testing and image building.

The goal is to demonstrate a basic but realistic software delivery workflow using industry-relevant DevOps tools and practices.

### Project Objectives

- Build a lightweight Python REST-style API.
- Implement a health-check endpoint.
- Write automated tests to validate API behavior.
- Manage application and development dependencies.
- Containerize the application using Docker.
- Use Docker Compose to run and manage the application.
- Automate testing and Docker image builds with GitHub Actions.
- Validate container health and API availability.
- Use Git and GitHub for source control and collaboration.

---

## 2\. Technology Stack

| Technology | Purpose |
| --- | --- |
| Python 3.12 | Application programming language |
| Flask | Lightweight Python web framework |
| pytest | Automated testing framework |
| pip | Python dependency management |
| Docker | Application containerization |
| Docker Compose | Container configuration and lifecycle management |
| GitHub Actions | Continuous Integration automation |
| YAML | Configuration for GitHub Actions and Docker Compose |
| Git | Version control |
| GitHub | Source code hosting and CI workflow execution |
| Linux | Development and command-line environment |

---

## 3\. Project Architecture

The project follows a simple software delivery workflow:

text

```
        Developer
            |
            v
      Write Python API
            |
            v
       Write Tests
            |
            v
      Commit with Git
            |
            v
       Push to GitHub
            |
            v
     GitHub Actions CI
            |
            v
    Install Dependencies
            |
            v
      Run pytest Tests
            |
            v
   Validate Compose YAML
            |
            v
     Build Docker Image
            |
            v
     Start Docker Container
            |
            v
     Check Container Health
            |
            v
    Test /health Endpoint
            |
            v
    Report Success or Failure
```

GitHub Actions automatically executes the CI workflow when code is pushed or a pull request is opened or updated.

If a required test or validation step fails, the workflow reports a failure.

---

## 4\. Application Features

The application exposes two HTTP GET endpoints.

| HTTP Method | Endpoint | Description | Expected Status |
| --- | --- | --- | --- |
| GET | `/` | Returns a welcome message | 200 OK |
| GET | `/health` | Reports application health | 200 OK |

### Health-Check Endpoint

The `/health` endpoint returns a JSON response:

json

```
{
  "status": "healthy"
}
```

This endpoint provides a simple way to verify that the application is responding to HTTP requests.

The Docker health check uses this endpoint to determine whether the containerized application is responding as expected.

**Note:** This is a basic application health check. It does not validate external dependencies such as databases or other services.

---

## 5\. Project Structure

text

```
CI_CD_Test/
│
├── app.py
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── .gitignore
├── README.md
│
├── tests/
│   └── test_app.py
│
└── .github/
    └── workflows/
        └── ci.yml
```

### File Descriptions

| File | Description |
| --- | --- |
| `app.py` | Implements the Flask API and health-check endpoint |
| `requirements.txt` | Lists the application runtime dependencies |
| `requirements-dev.txt` | Includes runtime dependencies and pytest |
| `pytest.ini` | Configures pytest test discovery |
| `tests/test_app.py` | Contains automated API tests |
| `Dockerfile` | Defines how to build the Docker image |
| `compose.yaml` | Defines the containerized application service |
| `.dockerignore` | Excludes unnecessary files from the Docker build context |
| `.gitignore` | Excludes generated files and local configuration from Git |
| `.github/workflows/ci.yml` | Defines the automated GitHub Actions CI pipeline |
| `README.md` | Documents the project, setup, and usage instructions |

---

## 6\. Automated Testing

The project uses pytest to validate application behavior.

The automated tests verify:

1. The home endpoint returns HTTP 200 and the expected JSON response.
2. The health endpoint returns HTTP 200 and the expected health status.
3. An unknown endpoint returns HTTP 404.

### Run Tests Locally

Create and activate a Python virtual environment:

bash

```
python3 -m venv .venv
source .venv/bin/activate
```

Install the development dependencies:

bash

```
python -m pip install -r requirements-dev.txt
```

Run the tests:

bash

```
python -m pytest -v
```

All three tests should pass when the application behaves as expected.

Automated testing helps identify regressions before changes are accepted into the main branch.

---

## 7\. Docker Containerization

Docker packages the application and its runtime dependencies into an image.

The Dockerfile uses a Python base image, installs Flask, copies the application code, and defines the startup command.

A Docker health check verifies that the application's `/health` endpoint is responding.

### Build the Docker Image

bash

```
docker build -t ci-cd-test:local .
```

### Run the Container

bash

```
docker run -d \
  --name ci-cd-test \
  -p 5000:5000 \
  ci-cd-test:local
```

### Check the Running Container

bash

```
docker ps
```

### View Application Logs

bash

```
docker logs ci-cd-test
```

### Test the Health Endpoint

bash

```
curl http://localhost:5000/health
```

Expected response:

json

```
{
  "status": "healthy"
}
```

### Inspect Container Health

bash

```
docker inspect \
  --format='{{.State.Health.Status}}' \
  ci-cd-test
```

After the health checks pass, the output should be:

text

```
healthy
```

### Stop and Remove the Container

bash

```
docker rm -f ci-cd-test
```

---

## 8\. Docker Compose

Docker Compose provides a repeatable way to build and run the application using a YAML configuration file.

### Start the Application

bash

```
docker compose up --build -d
```

### Check Service Status

bash

```
docker compose ps
```

### View Logs

bash

```
docker compose logs api
```

### Test the API

bash

```
curl http://localhost:5000/health
```

### Stop the Application

bash

```
docker compose down
```

Docker Compose simplifies application startup and makes the configuration easier to extend as the project grows.

---

## 9\. Continuous Integration with GitHub Actions

The project uses GitHub Actions to automate the testing and build-validation process.

The workflow is defined in:

text

```
.github/workflows/ci.yml
```

### Workflow Triggers

The workflow runs on:

- Push events.
- Pull request events.

### CI Pipeline Stages

| Stage | Description |
| --- | --- |
| Checkout | Retrieves the repository source code |
| Python Setup | Configures the Python runtime |
| Dependency Installation | Installs Flask and pytest |
| Automated Testing | Runs pytest and checks application behavior |
| Compose Validation | Validates the Docker Compose configuration |
| Docker Build | Builds the application image |
| Container Startup | Starts the Docker container |
| Health Validation | Waits for the container to become healthy |
| API Validation | Sends an HTTP request to the `/health` endpoint |
| Cleanup | Removes the temporary container |

### Expected Behavior

If all stages pass, GitHub Actions reports a successful workflow run.

If a test fails, the pipeline stops before the Docker build stage.

If the image cannot be built, the container fails to start, or the health endpoint does not respond successfully, the workflow reports a failure.

This provides automated feedback whenever code changes are submitted.

**Scope:** This project implements continuous integration and build validation. It does not publish images to a container registry or deploy the application to a production environment.

---

## 10\. Run the Complete Project Locally

### Step 1: Clone the Repository

Replace `YOUR_USERNAME` with your GitHub username.

bash

```
git clone https://github.com/YOUR_USERNAME/CI_CD_Test.git
cd CI_CD_Test
```

### Step 2: Create a Virtual Environment

bash

```
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

bash

```
python -m pip install -r requirements-dev.txt
```

### Step 4: Run Automated Tests

bash

```
python -m pytest -v
```

### Step 5: Validate Docker Compose

bash

```
docker compose config -q
```

### Step 6: Build and Start the Application

bash

```
docker compose up --build -d
```

### Step 7: Validate the Application

bash

```
curl -i http://localhost:5000/health
```

### Step 8: Check Container Health

bash

```
docker compose ps
```

### Step 9: View Logs

bash

```
docker compose logs api
```

### Step 10: Stop the Application

bash

```
docker compose down
```

---

## 11\. Version Control with Git

Git is used to track changes and manage the project's development history.

Initialize the repository if necessary:

bash

```
git init
git branch -M main
```

Review the changes:

bash

```
git status
```

Stage the project files:

bash

```
git add .
```

Create a commit:

bash

```
git commit -m "Build Python API CI pipeline with Docker"
```

Push the project to GitHub:

bash

```
git push -u origin main
```

After pushing, open the repository's **Actions** tab to view the CI workflow results.

---

## 12\. Skills Demonstrated

This project demonstrates practical entry-level DevOps skills, including:

- Linux command-line operations.
- Python application setup.
- Dependency management with pip.
- Automated testing with pytest.
- Docker image creation.
- Container execution and troubleshooting.
- Docker health checks.
- Docker Compose configuration.
- YAML configuration management.
- Git version control.
- GitHub repository management.
- GitHub Actions CI pipeline configuration.
- Automated build validation.
- Basic troubleshooting using logs and command-line tools.

---

## 13\. Future Improvements

The project can be extended to demonstrate additional DevOps capabilities.

Potential improvements include:

- Publish Docker images to Docker Hub or GitHub Container Registry.
- Tag images using Git commit identifiers.
- Add code coverage reporting.
- Add linting with Ruff.
- Pin and lock dependency versions for more reproducible builds.
- Scan Docker images for known vulnerabilities.
- Add branch protection rules requiring successful CI checks.
- Introduce a staging environment.
- Add a continuous deployment workflow.
- Deploy the application to a cloud platform.

These improvements can be implemented gradually as your DevOps skills develop.

---

## 14\. Résumé Project Description

**Project: CI\_CD\_Test — Automated Python API CI Pipeline**

**Technologies:** Python, Flask, pytest, Docker, Docker Compose, GitHub Actions, YAML, Git, GitHub, Linux.

- Developed a lightweight Flask API with welcome and health-check endpoints.
- Implemented automated API tests using pytest to validate HTTP responses and endpoint behavior.
- Containerized the application using Docker and configured automated container health checks.
- Created a Docker Compose configuration for repeatable application startup and validation.
- Built a GitHub Actions CI pipeline triggered by pushes and pull requests.
- Automated dependency installation, test execution, Docker image building, container health validation, and HTTP endpoint testing.
- Used Linux terminal commands and Git to manage source code, validate builds, and troubleshoot failures.

**Repository:** Add your GitHub repository URL here.

---

## 15\. Conclusion

CI\_CD\_Test demonstrates a basic but realistic software delivery workflow, from application development to automated testing, Docker containerization, and CI validation.

It provides a foundation for understanding how DevOps practices help teams identify problems early, maintain consistent application packaging, and automate repetitive software delivery tasks.

The project is intentionally small so that each component can be understood, tested, and explained during a technical interview.

## Final steps

After creating `README.md`, run these commands from your Linux terminal:

bash

```
git add README.md
git commit -m "Add project documentation"
git push
```

Your GitHub repository will now include documentation explaining the project's architecture, technologies, setup instructions, CI pipeline, and learning outcomes.

**Tip for your résumé:** Once the project is uploaded, add the actual GitHub repository link to your résumé. Be prepared to explain why you used pytest, how Docker differs from Docker Compose, and what happens when a test fails in GitHub Actions.