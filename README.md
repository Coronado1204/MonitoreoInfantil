# Monitoreo Infantil

## Project Description
"Monitoreo Infantil" is a web application developed using Flask that focuses on monitoring the growth and development of children. The application provides a user-friendly interface to visualize and manage data related to child development, integrating various data management processes.

## Project Structure
The project consists of the following files and directories:

```
monitoreo-infantil
├── app.py                # Main application file for the Flask project
├── static                # Directory for static files (CSS, JS)
│   ├── css
│   │   └── style.css     # CSS styles for the web application
│   └── js
│       └── script.js     # JavaScript code for interactive features
├── templates             # Directory for HTML templates
│   ├── index.html        # Main HTML template for the application
│   └── herramienta.html   # HTML template for the tool page
├── requirements.txt      # List of dependencies for the project
└── README.md             # Project documentation
```

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd monitoreo-infantil
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```
   python app.py
   ```

5. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000`.

## Features
- **Responsive Design**: The application is designed to be responsive and user-friendly across various devices.
- **Navigation Menu**: A fixed top navigation menu allows easy access to different sections of the application.
- **Interactive Elements**: Smooth scrolling and hover effects enhance user experience.

## Power BI integration
You can embed a Power BI report into the `Herramienta` page. The application reads the embed URL from the environment variable `POWERBI_EMBED_URL`. If not set, a default public embed URL provided by the project authors will be used.

To set the embed URL in Windows PowerShell (temporary for the session):
```powershell
$env:POWERBI_EMBED_URL = 'https://app.powerbi.com/view?r=<your-embed-token-or-id>'
```

Then run the app as usual:
```powershell
# Activate venv (Windows)
venv\Scripts\activate
python app.py
```

Notes:
- If your Power BI report is published with "Publish to web" (public), embedding via iframe is straightforward.
- For private reports or if you need role-level security, consider using the Power BI secure embed flow (requires Azure AD app registration and server-side token generation). If you want, I can help implement the secure embed flow.

## Authors
- Julian David Coronado
- Cristian Leonardo Moscoso
- Nicolas Gutierrez

## License
This project is licensed under the MIT License.