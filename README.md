# 🚀 Keggle Analyzer

## 📊 Analyze Kaggle Datasets with Ease

Keggle Analyzer is a powerful, microservice-based application designed to streamline the process of analyzing Kaggle datasets. With integrated Google OAuth2 authentication, robust data management, and an intuitive API, it's never been easier to derive insights from your data.

## 🌟 Features

- 🔒 Secure Google OAuth2 authentication
- 📁 Efficient Kaggle dataset management
- ⚡ Fast and scalable analysis pipeline
- 🔍 Advanced search capabilities with Meilisearch
- 📊 Customizable analysis chains
- 🐇 Asynchronous task processing with RabbitMQ

## 🏗️ Architecture

Our application is built on a microservices architecture, ensuring scalability and maintainability:

1. **Backend**: Core API service
2. **Auth Service**: Handles user authentication
3. **Analyzer**: Processes and analyzes datasets
4. **Kaggle Storage Manager**: Manages dataset storage and retrieval
5. **RabbitMQ**: Message broker for async tasks
6. **MongoDB**: Document storage for flexible data
7. **Meilisearch**: Fast, typo-tolerant search engine

## 🚀 Getting Started

### Prerequisites

- Docker and Docker Compose
- Kaggle API credentials
- Google OAuth2 credentials

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/keggle-analyzer.git
      cd keggle-analyzer
   ```
2. Set up environment variables:
3. Start the services
   ```
   docker-compose up -d
   ```
4. Access the API at **http://localhost:7348


## 🔧 Usage

1. ****Authenticate****: Use the **/login** endpoint to authenticate with Google.
2. ****Create an Analysis****: POST to **/analyses/** with your dataset details.
3. ****Add Chains****: POST to **/analyses/{analysis_id}/chains/** to add analysis steps.
4. ****Run Analysis****: GET **/analyses/{analysis_id}/run** to execute your analysis.
5. ****View Results****: GET **/analyses/{analysis_id}/results** to see your insights.
