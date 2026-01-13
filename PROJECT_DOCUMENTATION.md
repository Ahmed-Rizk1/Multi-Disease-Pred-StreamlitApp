# Multi-Disease Prediction System - Complete Project Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technology Stack](#technology-stack)
4. [Project Architecture](#project-architecture)
5. [Project Structure](#project-structure)
6. [Installation & Setup](#installation--setup)
7. [Usage Guide](#usage-guide)
8. [Docker Deployment](#docker-deployment)
9. [Component Documentation](#component-documentation)
10. [Model Information](#model-information)
11. [Configuration](#configuration)
12. [Troubleshooting](#troubleshooting)
13. [Future Enhancements](#future-enhancements)

---

## Project Overview

The **Multi-Disease Prediction System** is a web-based machine learning application built with Streamlit that enables users to predict three different diseases:
- **Diabetes**
- **Heart Disease**
- **Parkinson's Disease**

The application uses pre-trained machine learning models to make predictions based on user-provided medical parameters. The system is containerized using Docker for easy deployment and distribution.

### Key Highlights
- 🏥 Multi-disease prediction in a single application
- 🤖 Pre-trained ML models for accurate predictions
- 🐳 Docker containerization for easy deployment
- 🎨 Modern, user-friendly Streamlit interface
- 📊 Real-time prediction results

---

## Features

### 1. **Diabetes Prediction**
- Predicts diabetes based on 8 parameters:
  - Number of Pregnancies
  - Glucose Level
  - Blood Pressure
  - Skin Thickness
  - Insulin Level
  - BMI (Body Mass Index)
  - Diabetes Pedigree Function
  - Age

### 2. **Heart Disease Prediction**
- Predicts heart disease based on 13 parameters:
  - Age
  - Sex
  - Chest Pain types
  - Resting Blood Pressure
  - Serum Cholesterol
  - Fasting Blood Sugar
  - Resting Electrocardiographic results
  - Maximum Heart Rate achieved
  - Exercise Induced Angina
  - ST depression induced by exercise
  - Slope of the peak exercise ST segment
  - Major vessels colored by flourosopy
  - Thalassemia

### 3. **Parkinson's Disease Prediction**
- Predicts Parkinson's disease based on 22 voice measurement parameters:
  - MDVP (Multiple Dimension Voice Program) features
  - Jitter and Shimmer measurements
  - Various acoustic features (NHR, HNR, RPDE, DFA, etc.)

### 4. **User Interface Features**
- Clean, intuitive sidebar navigation
- Multi-column input layout for better UX
- Real-time validation and error handling
- Clear prediction results with actionable messages

---

## Technology Stack

### Core Technologies
- **Python 3.10**: Programming language
- **Streamlit 1.29.0**: Web application framework
- **scikit-learn 1.3.2**: Machine learning library
- **NumPy 1.26.3**: Numerical computing
- **Docker**: Containerization platform

### Additional Libraries
- **streamlit-option-menu 0.3.6**: Enhanced sidebar menu component
- **pickle**: Model serialization/deserialization

---

## Project Architecture

### Architecture Overview
```
┌─────────────────────────────────────────┐
│         Streamlit Web Interface         │
│  (User Input & Results Display)         │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│         Application Layer               │
│  - main.py (Router)                     │
│  - pages/ (Disease-specific pages)      │
│  - components/ (Reusable UI)           │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│         Utility Layer                   │
│  - model_loader.py (Model Management)   │
│  - constants.py (Configuration)         │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│         Model Layer                     │
│  - diabetes_model.sav                   │
│  - heart_disease_model.sav              │
│  - parkinsons_model.sav                  │
└─────────────────────────────────────────┘
```

### Data Flow
1. User inputs medical parameters through the Streamlit interface
2. Input data is validated and converted to appropriate format
3. Pre-trained model is loaded (cached for performance)
4. Model makes prediction based on input features
5. Result is displayed to the user with appropriate messaging

---

## Project Structure

```
Multi-Disease-Pred-StreamlitApp/
├── app/                          # Main application directory
│   ├── __init__.py              # Package initialization
│   ├── main.py                  # Application entry point & router
│   │
│   ├── pages/                   # Disease prediction pages
│   │   ├── __init__.py
│   │   ├── diabetes.py          # Diabetes prediction page
│   │   ├── heart_disease.py     # Heart disease prediction page
│   │   └── parkinsons.py        # Parkinson's prediction page
│   │
│   ├── components/              # Reusable UI components
│   │   ├── __init__.py
│   │   └── sidebar.py           # Sidebar navigation menu
│   │
│   └── utils/                   # Utility functions
│       ├── __init__.py
│       ├── model_loader.py      # Model loading utilities
│       └── constants.py         # Application constants
│
├── models/                      # Pre-trained ML models
│   ├── diabetes_model.sav
│   ├── heart_disease_model.sav
│   └── parkinsons_model.sav
│
├── data/                        # Training datasets
│   └── datasets/
│       ├── diabetes.csv
│       ├── heart.csv
│       └── parkinsons.csv
│
├── config/                      # Streamlit configuration
│   ├── config.toml             # Streamlit settings
│   └── credentials.toml        # Authentication (if needed)
│
├── notebooks/                   # Jupyter notebooks for model training
│   ├── Multiple disease prediction system - diabetes.ipynb
│   ├── Multiple disease prediction system - heart.ipynb
│   └── Multiple disease prediction system - Parkinsons.ipynb
│
├── Dockerfile                   # Docker container configuration
├── requirements.txt             # Python dependencies
└── README.md                    # Quick start guide
```

---

## Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Docker (optional, for containerized deployment)

### Local Installation

#### Step 1: Clone or Download the Project
```bash
# If using git
git clone <repository-url>
cd Multi-Disease-Pred-StreamlitApp
```

#### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 3: Verify Model Files
Ensure all model files are present in the `models/` directory:
- `diabetes_model.sav`
- `heart_disease_model.sav`
- `parkinsons_model.sav`

#### Step 4: Run the Application
```bash
streamlit run app/main.py
```

The application will open in your default web browser at `http://localhost:8501`

---

## Usage Guide

### Accessing the Application
1. Launch the application using `streamlit run app/main.py`
2. The application opens in your web browser
3. Use the sidebar menu to navigate between different disease prediction pages

### Making Predictions

#### Diabetes Prediction
1. Navigate to "Diabetes Prediction" from the sidebar
2. Fill in all 8 required fields:
   - Number of Pregnancies (numeric)
   - Glucose Level (numeric)
   - Blood Pressure value (numeric)
   - Skin Thickness value (numeric)
   - Insulin Level (numeric)
   - BMI value (numeric)
   - Diabetes Pedigree Function value (numeric)
   - Age of the Person (numeric)
3. Click "Diabetes Test Result" button
4. View the prediction result

#### Heart Disease Prediction
1. Navigate to "Heart Disease Prediction" from the sidebar
2. Fill in all 13 required fields (all numeric values)
3. Click "Heart Disease Test Result" button
4. View the prediction result with recommendations

#### Parkinson's Disease Prediction
1. Navigate to "Parkinsons Prediction" from the sidebar
2. Fill in all 22 voice measurement parameters (all numeric values)
3. Click "Parkinson's Test Result" button
4. View the prediction result

### Input Validation
- All input fields must contain valid numeric values
- If invalid input is provided, an error message will be displayed
- Ensure all fields are filled before clicking the prediction button

---

## Docker Deployment

### Building the Docker Image

#### Prerequisites
- Docker installed on your system
  - **Linux**: Docker Engine
  - **Windows/Mac**: Docker Desktop

#### Step 1: Start Docker Service
**Linux:**
```bash
sudo systemctl start docker
```

**Windows/Mac:**
- Start Docker Desktop application

#### Step 2: Build Docker Image
Navigate to the project directory and build the image:
```bash
# Linux/Mac
sudo docker build -t multi-disease-pred:latest .

# Windows (run as Administrator or use Docker Desktop)
docker build -t multi-disease-pred:latest .
```

**Note:** Rebuild the image if you make any code changes.

#### Step 3: Verify Image Creation
```bash
docker images
```

You should see your image listed with the tag `multi-disease-pred:latest`

### Running the Container

#### Start Container
```bash
# Linux/Mac
sudo docker run -p 80:80 <IMAGE_ID>

# Windows
docker run -p 80:80 <IMAGE_ID>
```

#### Access the Application
- **Linux/Mac**: Open browser to `http://0.0.0.0:80` or `http://localhost:80`
- **Windows**: Open browser to `http://localhost:80`

#### Check Running Containers
```bash
docker ps
```

#### Stop Container
- Press `Ctrl + C` in the terminal, or
- Stop from Docker Desktop interface

#### Remove Container
```bash
# Remove stopped containers
docker container prune

# Remove specific container
docker rm <CONTAINER_ID>
```

### Docker Hub Deployment

#### Step 1: Create Docker Hub Account
1. Sign up at [Docker Hub](https://hub.docker.com)
2. Create a new repository

#### Step 2: Login to Docker Hub
```bash
docker login
```
Enter your Docker Hub username and password/token.

#### Step 3: Tag Your Image
```bash
docker tag <IMAGE_ID> <username>/<repo-name>:<tag>

# Example
docker tag abc123 myusername/multi-disease-pred:v1.0
```

#### Step 4: Push to Docker Hub
```bash
docker push <username>/<repo-name>:<tag>

# Example
docker push myusername/multi-disease-pred:v1.0
```

#### Step 5: Pull and Run from Docker Hub
```bash
docker pull <username>/<repo-name>:<tag>
docker run -p 80:80 <username>/<repo-name>:<tag>
```

---

## Component Documentation

### 1. `app/main.py`
**Purpose**: Main application entry point and routing logic

**Key Functions**:
- `main()`: Initializes the application, renders sidebar, and routes to appropriate disease prediction page based on user selection

**Dependencies**:
- `app.components.sidebar`
- `app.pages.diabetes`
- `app.pages.heart_disease`
- `app.pages.parkinsons`
- `app.utils.constants`

---

### 2. `app/components/sidebar.py`
**Purpose**: Renders the sidebar navigation menu

**Key Functions**:
- `render_sidebar()`: Creates and displays the option menu in the sidebar
  - Returns: Selected menu option string

**Features**:
- Uses `streamlit-option-menu` for enhanced UI
- Displays icons for each menu option
- Default selection: First option (Diabetes Prediction)

**Configuration**:
- Menu options and icons defined in `app/utils/constants.py`

---

### 3. `app/pages/diabetes.py`
**Purpose**: Diabetes prediction page implementation

**Key Functions**:
- `render_diabetes_page()`: Renders the complete diabetes prediction interface

**Input Parameters** (8 total):
1. Number of Pregnancies
2. Glucose Level
3. Blood Pressure value
4. Skin Thickness value
5. Insulin Level
6. BMI value
7. Diabetes Pedigree Function value
8. Age of the Person

**Output**:
- Binary prediction: Diabetic (1) or Not Diabetic (0)
- User-friendly message displayed via `st.success()`

**Error Handling**:
- Catches `ValueError` for invalid numeric inputs
- Displays appropriate error message

---

### 4. `app/pages/heart_disease.py`
**Purpose**: Heart disease prediction page implementation

**Key Functions**:
- `render_heart_disease_page()`: Renders the complete heart disease prediction interface

**Input Parameters** (13 total):
1. Age
2. Sex
3. Chest Pain types
4. Resting Blood Pressure
5. Serum Cholestoral in mg/dl
6. Fasting Blood Sugar > 120 mg/dl
7. Resting Electrocardiographic results
8. Maximum Heart Rate achieved
9. Exercise Induced Angina
10. ST depression induced by exercise
11. Slope of the peak exercise ST segment
12. Major vessels colored by flourosopy
13. Thalassemia (0 = normal; 1 = fixed defect; 2 = reversable defect)

**Output**:
- Binary prediction: Heart Disease (1) or No Heart Disease (0)
- Includes recommendation message (consult doctor or healthy status)

**Error Handling**:
- Catches `ValueError` for invalid numeric inputs
- Displays appropriate error message

---

### 5. `app/pages/parkinsons.py`
**Purpose**: Parkinson's disease prediction page implementation

**Key Functions**:
- `render_parkinsons_page()`: Renders the complete Parkinson's prediction interface

**Input Parameters** (22 total):
Voice measurement parameters including:
- MDVP features (Fo, Fhi, Flo, Jitter, Shimmer, etc.)
- Acoustic features (NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE)

**Output**:
- Binary prediction: Has Parkinson's (1) or No Parkinson's (0)
- User-friendly message displayed

**Error Handling**:
- Catches `ValueError` for invalid numeric inputs
- Displays appropriate error message

---

### 6. `app/utils/model_loader.py`
**Purpose**: Utility functions for loading pre-trained ML models

**Key Functions**:
- `load_model(model_name: str)`: Generic function to load any model from the models directory
  - Parameters: `model_name` - Name of the model file (e.g., "diabetes_model.sav")
  - Returns: Loaded model object
  - Raises: `FileNotFoundError` if model file doesn't exist

- `get_diabetes_model()`: Loads diabetes prediction model
- `get_heart_disease_model()`: Loads heart disease prediction model
- `get_parkinsons_model()`: Loads Parkinson's prediction model

**Model Storage**:
- Models are stored in `models/` directory at project root
- Models are serialized using Python's `pickle` module
- Models are loaded on-demand and can be cached by Streamlit

---

### 7. `app/utils/constants.py`
**Purpose**: Centralized configuration constants

**Constants Defined**:
- `DIABETES`: "Diabetes Prediction"
- `HEART_DISEASE`: "Heart Disease Prediction"
- `PARKINSONS`: "Parkinsons Prediction"
- `MENU_OPTIONS`: List of all menu options
- `MENU_ICONS`: List of icons for each menu option
- `MENU_ICON`: Main menu icon

**Usage**:
- Ensures consistency across the application
- Easy to modify menu options and icons in one place

---

## Model Information

### Model Format
- All models are saved as `.sav` files using Python's `pickle` module
- Models are trained using scikit-learn
- Binary classification models (0 = negative, 1 = positive)

### Model Training
- Training notebooks are available in the `notebooks/` directory
- Datasets used for training are in `data/datasets/`
- Models should be retrained periodically with updated datasets for better accuracy

### Model Performance
- Model performance metrics are available in the respective Jupyter notebooks
- For production use, ensure models meet acceptable accuracy thresholds

### Model Updates
To update a model:
1. Retrain using the Jupyter notebooks
2. Save the new model with the same filename in the `models/` directory
3. Rebuild Docker image if using containerized deployment

---

## Configuration

### Streamlit Configuration (`config/config.toml`)
Key settings:
- **Port**: 80 (for Docker deployment)
- **Server Address**: 0.0.0.0 (accessible from all interfaces)
- **Headless Mode**: true (for Docker)
- **CORS**: Disabled
- **Logging Level**: debug

### Customization
To modify application behavior:
1. **Change Port**: Edit `config/config.toml` and `Dockerfile`
2. **Modify Menu**: Edit `app/utils/constants.py`
3. **Update Models**: Replace files in `models/` directory
4. **Change UI**: Modify page files in `app/pages/`

---

## Troubleshooting

### Common Issues

#### 1. **Model Not Found Error**
**Problem**: `FileNotFoundError: Model not found`
**Solution**: 
- Verify model files exist in `models/` directory
- Check file names match exactly: `diabetes_model.sav`, `heart_disease_model.sav`, `parkinsons_model.sav`

#### 2. **Port Already in Use**
**Problem**: Port 80 or 8501 is already in use
**Solution**:
- Change port in `config/config.toml` and `Dockerfile`
- Or stop the service using the port

#### 3. **Docker Build Fails**
**Problem**: Docker build errors
**Solution**:
- Ensure Docker is running
- Check Dockerfile syntax
- Verify all required files are present
- Check disk space

#### 4. **Import Errors**
**Problem**: Module not found errors
**Solution**:
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify Python version is 3.10 or higher
- Check project structure matches expected layout

#### 5. **Invalid Input Errors**
**Problem**: "Please enter valid numeric values"
**Solution**:
- Ensure all input fields contain numeric values
- Check for empty fields
- Verify decimal format (use `.` not `,`)

#### 6. **Docker Container Won't Start**
**Problem**: Container exits immediately
**Solution**:
- Check Docker logs: `docker logs <CONTAINER_ID>`
- Verify model files are copied to container
- Check Streamlit configuration

---

## Future Enhancements

### Potential Improvements

1. **Enhanced Input Validation**
   - Range validation for medical parameters
   - Input type hints and tooltips
   - Real-time input validation

2. **Model Improvements**
   - Model versioning system
   - Confidence scores for predictions
   - Model performance monitoring

3. **User Interface**
   - Data visualization (charts, graphs)
   - Prediction history
   - Export results functionality
   - Multi-language support

4. **Backend Enhancements**
   - Database integration for storing predictions
   - User authentication
   - API endpoints for programmatic access
   - Batch prediction support

5. **Deployment**
   - Kubernetes deployment configuration
   - CI/CD pipeline setup
   - Cloud deployment guides (AWS, Azure, GCP)
   - Health check endpoints

6. **Documentation**
   - API documentation
   - Developer guide
   - Model training guide
   - Contribution guidelines

7. **Testing**
   - Unit tests for all components
   - Integration tests
   - End-to-end testing
   - Model validation tests

8. **Security**
   - Input sanitization
   - Rate limiting
   - HTTPS support
   - Data encryption

---

## Additional Resources

### Documentation Files
- `README.md`: Quick start guide
- `PROJECT_DOCUMENTATION.md`: This comprehensive documentation

### Training Resources
- Jupyter notebooks in `notebooks/` directory for model training
- Datasets in `data/datasets/` for reference

### External Links
- [Streamlit Documentation](https://docs.streamlit.io/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Docker Documentation](https://docs.docker.com/)

---

## Support & Contribution

### Getting Help
- Check this documentation first
- Review the troubleshooting section
- Examine the code comments
- Check Streamlit and Docker documentation

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## License & Credits

### License
[Specify your license here]

### Credits
- Built with Streamlit
- Machine learning models trained using scikit-learn
- Containerized with Docker

---

## Version History

### Version 1.0
- Initial release
- Support for 3 diseases: Diabetes, Heart Disease, Parkinson's
- Docker containerization
- Streamlit web interface

---

**Last Updated**: [Current Date]
**Document Version**: 1.0
