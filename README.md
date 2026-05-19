Patient Care Record (PCR) Logic System

This repository hosts a web-based Patient Care Record system designed to streamline clinical intake and neurological assessment. The application provides a secure interface for healthcare providers to capture patient demographics and automatically calculate the Glasgow Coma Scale (GCS) to categorize injury severity.

Features
Provider Dashboard: A centralized landing page for navigating between patient records and the intake module.

Secure Authentication: Login/Logout functionality to protect sensitive patient data.

Dynamic Intake Form: A structured HTML5/CSS3 interface for collecting personal information and clinical data.

GCS Logic Engine: Automated calculation of GCS scores (3–15) with built-in validation to reject out-of-range inputs.

Severity Categorization: Logic-driven categorization of neurological status (Severe, Moderate, or Mild).

Persistent Storage: SQLite integration for reliable local data management.

Tech Stack
Frontend: HTML5, CSS3

Backend: Python

Database: SQLite

CI/CD Pipeline: YAML (GitHub Actions)

Cloud Infrastructure: AWS (EC2 & S3)

CI/CD Pipeline Architecture
The project utilizes an automated pipeline to ensure code integrity and seamless deployment. The workflow is triggered upon pushing changes to the GitHub repository.

Deployment Workflow
Development: Code is developed and tested on an EC2 environment or local machine.

Version Control: Changes are pushed to GitHub and S3.

Automation SQLite database.
