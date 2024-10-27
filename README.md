# CI/CD Pipeline for XGBoost Model Deployment

## Project Overview

This project demonstrates the implementation of a Continuous Integration and Continuous Deployment (CI/CD) pipeline for deploying an XGBoost machine learning model using GitHub Actions and Google Kubernetes Engine (GKE). The pipeline ensures that any changes to the model code are automatically tested, validated, and deployed to production only if the new model outperforms the previous version.

### Components

- **Version Control:** GitHub
- **CI/CD Tool:** GitHub Actions
- **Containerization:** Docker
- **Orchestration:** Google Kubernetes Engine (GKE)
- **Model:** XGBoost
- **Serving Framework:** Flask
- **Testing:** Automated tests to compare model accuracy

## CI/CD Pipeline

### 1. Version Control with GitHub

All source code, including model code, Dockerfile, Kubernetes YAML configurations, and GitHub Actions workflows, are stored in a GitHub repository. This setup ensures version control and facilitates collaboration.

### 2. Continuous Integration with GitHub Actions

GitHub Actions is configured to automate the CI/CD process:

- **Trigger:** The pipeline is triggered automatically whenever new code is pushed to the repository.
- **Build:** The Docker image for the Flask application serving the XGBoost model is built.
- **Test:** Automated tests are executed to validate the model's predictions and compare the new model's accuracy against the previous version.
- **Deploy:** If the tests pass and the new model outperforms the old one, the updated Docker image is deployed to GKE.

### 3. Automated Testing

Automated tests are implemented to validate the integrity of the model code.

### 4. Continuous Deployment to GKE

Upon successful testing, the new Docker image is deployed to GKE. Kubernetes manages the deployment, ensuring high availability and scalability of the serving application.

## Tools and Technologies

- **GitHub:** Version control and repository hosting.
- **GitHub Actions:** CI/CD pipeline automation.
- **Docker:** Containerization of the Flask application and model.
- **Google Kubernetes Engine (GKE):** Orchestration and management of containerized applications.
- **XGBoost:** Machine learning model for predictions.
- **Flask:** Web framework for serving the model.
- **Python:** Programming language for model development and testing.

## Setup Instructions

### Prerequisites

- GitHub account with repository access.
- Google Cloud account with GKE enabled.
- Docker installed locally.
- Kubernetes CLI (`kubectl`) installed.

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo

   ```

2. **Setup Poetry Environment:**

To ensure seamless dependency management and packaging, Poetry is used. Setup Poetry virtualenv and install packages. Use official Poetry documentation if needed. [Link](https://python-poetry.org/docs/)

2. **Enable APIs and IAM access in GCP:**

- Enable APIs: GKE API, Artifacts Registry.
- IAM Permissions: Ensure all necessary permissions are enabled for the service account including Artifact Registry Writer, Kubernetes Engine Developer, Storage Admin.
- GKE Cluster: Create GKE Cluster.
- Configure secrets: Create image pull secret.[Link](https://cloud.google.com/artifact-registry/docs/access-control#pullsecrets)

2. **Configure GitHub Actions:**

Ensure that the GitHub Actions workflow file (.github/workflows/ci_cd_pipeline.yml) is correctly set up with necessary secrets (e.g., Google Cloud credentials).
Build and Test Locally (Optional):

    ```bash
    docker build -t your-model-app .
    docker run -p 5000:5000 your-model-app
    ```

Configure necessary github variables and secrets.

- Secrets: GCP_PROJECT_ID, GCP_SA_KEY
- Variables: GKE_CLUSTER, GKE_ZONE, GCP_DOCKER_PACKAGE, GCP_DOCKER_IMAGE

3. **Deploy to GKE:**

The deployment is automated via GitHub Actions. Ensure that the Kubernetes YAML files are correctly configured for your GKE cluster.

4. **Push Changes:**

Commit and push your changes to the repository. The CI/CD pipeline will automatically trigger, run tests, and deploy if the new model is better.
