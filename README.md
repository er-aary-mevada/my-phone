# Mobile Shop Web Application

This is a basic web application for a mobile shop, built using the Flask framework in Python.

## Project Description

This application provides a simple online presence for a mobile shop. It currently features a homepage to welcome visitors. Future enhancements could include product listings, a shopping cart, and contact information.

## Setup Instructions

1.  **Clone the repository:**
```
bash
    git clone <repository_url>
    cd mobile-shop-app
    
```
2.  **Create a virtual environment (recommended):**
```
bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    
```
3.  **Install dependencies:**
```
bash
    pip install Flask
    
```
## How to Run the App

1.  **Ensure you are in the project directory.**
2.  **Run the Flask application:**
```
bash
    python app.py
    
```
3.  **Open your web browser** and navigate to `http://127.0.0.1:5000/` to view the homepage.

## Project Structure
```
.
├── app.py
├── README.md
└── templates
    └── index.html
```
- `app.py`: The main Flask application file.
- `README.md`: This file, providing information about the project.
- `templates/`: Directory containing HTML templates.
    - `index.html`: The homepage template.