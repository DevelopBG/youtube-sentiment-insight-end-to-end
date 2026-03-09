# youtube-sentiment-insight-end-to-end


```Pipeline -- 
    1. Data Collection
    2. Data Pre-processing and EDA
    3. Building Baseline Models
    4. Setup Mlflow server on AWS
    5. Improve the baseline models
        |-- BOW< TFIDF
        |-- Max Feature
        |-- Handeling imbalance data
        |-- Hyperparameter tuning with multiple model
        |-- Stacking models
    6. Build ML pipeline with DVC
    7. Add model to the model registry
    8. Implement chrome pulgin
    9. CICD workflow
    10. Containarization
    11. Github for code repo
```

```
project/
│
├── data/
│   ├── raw/                  # Original, unprocessed data
│   └── processed/            # Cleaned and transformed data
│
├── notebooks/                # Exploratory and experimental notebooks
├── src/
│   ├── data_preprocessing.py # Data cleaning and feature engineering
│   ├── model.py              # Model definition and architecture
│   ├── train.py              # Training pipeline
│   └── evaluate.py           # Evaluation and metrics
│
├── flusk_api/
|   ├── main.py
|
├── models/                   # Saved model checkpoints
├── results/                  # Outputs, plots, and reports
├── requirements.txt          # Python dependencies
└── README.md    
```

#### DEPLOYMENT -------------------------->

## AWS setup steps for MLFlow server setup

    1. Login to AWS console.
    2. Create an IAM user if hasn't been created already
    3. Create an S3 bucket.
    4. Create EC2 machine(Ubuntu) & enable 5000 port

    # Command on EC2 machine to setup MLFlow server
    ```
    sudo apt update
    sudo apt install python3-pip 
    sudo apt install pipenv
    sudo apt install virtualenv
    mkdir mlflow
    cd mlflow
    pipenv install mlflow
    pipenv install awscli
    pipenv install boto3
    pipenv shell


    # Then set aws configuration
    aws configure

    "
    mlflow server -h 0.0.0.0 --default-artifact-root s3://{bucket name}
    mlflow server \
  --host 0.0.0.0 \
  --port 5000 \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root s3://{bucket name} \
  --allowed-hosts {public ipv4}:5000 \
  --crss-allowed-origins '*'
  "

    "Browser - http:{public ipv4}:5000"

    export MLFLOW_TRACKING_URI={ec2 uri}

    ```
    

# Steps for deployment---
    ```
    EC2 access: It is virtual machine
    ERC: Elastic Container Registry to save our docker image
    1. Login to AWS Console
    2. Create IAM user 
    3. Build docker image of the source code. 
    4. Push the image to ECR
    5. Launch EC2 
    6. Pull image form ECR to EC2
    7. Launch docker image in EC2

    # Policies to attach
    1. AmazoneEC2ContainerRegistryFullAccess
    2. AmazonEC2FullAccess
    ``` 
## Commands on EC2 
    ```
    1. sudo apt-get update -y
    2. sudo apt-get upgrade
    3. curl -fsSL https://get.docker.com -o get-docker.sh
    4. sudo sh get-docker.sh
    5. sudo usermod -aG docker ubuntu
    6. newgrp docker
    ```
## Configure EC2 as self-hosted runner:
    ```
    1. github repo setting -> actions -> new self hosted runner -> run the commands on EC2 
    2. run those commands until "./run.sh"
    3. On EC2 machine,-
        runner group : Enter (default)
        name of runner: self-hosted 
        then "Enter"
        "Enter"

    4. "./run.sh"
    ```

## Setup github secretes:
    # secrete and variable -> action -> new repository secrete
        1. AWS_ACCESS_KEY_ID = 
        2. AWS_SECRET_ACCESS_KEY = 
        3. AWS_REGION = 
        4. AWS_ECR_LOGIN_URI = 
        5. ECR_REPOSITORY_NAME = 