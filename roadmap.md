# 🚀 **Curriculum: Cloud-Ready ML Engineer**

## 🎯 **Goal:**

Become job-ready for ML Engineer roles requiring AWS (with SageMaker), Docker, Kubernetes, and related DevOps skills.

---

## **1. AWS Core Services & Environment Setup**

- **Theory**: IAM, EC2, S3, VPC, CloudWatch, CLI
- **Hands-on**:
  - Launch EC2, setup IAM roles
  - Create S3 buckets for data/model storage
  - Monitor EC2 logs via CloudWatch

---

## **2. Docker for ML**

- **Theory**: Dockerfiles, docker-compose, ECR (Elastic Container Registry)
- **Hands-on**:
  - Containerize a FastAPI ML app
  - Push image to ECR
  - Run locally and on EC2

---

## **3. Kubernetes Basics (Local + Theory)**

- **Theory**: Pods, Deployments, Services, ConfigMaps, Secrets
- **Hands-on**:
  - Setup minikube locally
  - Deploy ML app with kubectl
  - Use ConfigMaps and Secrets

---

## **4. Kubernetes on AWS (EKS)**

- **Theory**: EKS, Load Balancers, IAM Roles for Service Accounts
- **Hands-on**:
  - Setup EKS using `eksctl`
  - Deploy ML app to EKS
  - Expose via LoadBalancer service

---

## **5. SageMaker Essentials**

- **Theory**: Training jobs, Hosting endpoints, Notebooks, Inference
- **Hands-on**:
  - Train XGBoost model using SageMaker SDK
  - Deploy as real-time endpoint
  - Call endpoint from client app

---

## **6. Lambda + API Gateway + Triggers**

- **Theory**: Serverless, Event-driven ML pipelines
- **Hands-on**:
  - S3 Upload → Lambda → Trigger SageMaker job
  - Deploy FastAPI behind API Gateway
  - Monitor events via CloudWatch

---

## **7. Secrets, Parameters & Security**

- **Theory**: Secrets Manager, Systems Manager (SSM), IAM policies
- **Hands-on**:
  - Store API keys in Secrets Manager
  - Access from deployed container
  - Apply least privilege IAM roles

---

## **8. Capstone Projects + Mock Interview**

- Build 2–3 full-stack ML DevOps projects (see below)
- Prepare architecture diagrams & CI/CD pipelines
- Practice storytelling and debugging walkthrough

---

## 🛠️ Capstone Projects (Pick 2 of 3)

| Project                                  | Key Skills Covered                                    |
| ---------------------------------------- | ----------------------------------------------------- |
| **1. ML Inference API on EKS**           | Docker, FastAPI, EKS, Secrets Manager, GitHub Actions |
| **2. Event-Driven ML Training Pipeline** | S3, Lambda, SageMaker, CloudWatch                     |
| **3. AI Microservices with CI/CD**       | Multiple APIs, Kubernetes, API Gateway, Prometheus    |

---

## 📦 Bonus Topics (Optional, if time permits)

- Terraform or AWS CDK
- GitHub Actions for CI/CD
- Prometheus + Grafana for monitoring
- Step Functions for orchestrated ML pipelines

---

## ✅ Outcome

- ✅ Hands-on deployment on AWS & Kubernetes
- ✅ Real ML projects in cloud-ready production environments
- ✅ Confidence to explain real-world cloud ML systems
