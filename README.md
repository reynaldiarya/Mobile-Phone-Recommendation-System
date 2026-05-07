# Mobile Phone Recommendation System

An intelligent web application leveraging machine learning to recommend mobile devices based on technical specifications.

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" />
  <img src="https://img.shields.io/badge/PHP-8.x-777BB4.svg" />
  <img src="https://img.shields.io/badge/Python-3.x-3776AB.svg" />
  <a href="LICENSE">
    <img alt="License" src="https://img.shields.io/badge/license-MIT-yellow.svg" target="_blank" />
  </a>
</p>

## Description

The Mobile Phone Recommendation System is a hybrid web application designed to help consumers discover new smartphones that align with their preferences. By combining a lightweight PHP frontend with a robust Python-based machine learning backend, the system analyzes a comprehensive dataset of mobile devices. It utilizes cosine similarity algorithms to compare features such as price, RAM, and storage capacity, providing users with highly accurate and personalized device recommendations based on a selected baseline model.

## Features

- **Machine Learning Engine**: Utilizes cosine similarity to calculate and surface the most relevant device matches based on hardware specifications.
- **Dynamic Search Interface**: Features an intuitive, searchable dropdown powered by Select2 for seamless device selection.
- **Automated Data Processing**: Includes robust data cleaning pipelines to handle missing values, map missing specifications, and process outliers.
- **Hybrid Architecture**: Demonstrates seamless integration between a PHP web interface and complex Python analytical scripts.
- **Responsive Design**: Built with Bootstrap 5 to ensure a consistent experience across desktop and mobile browsers.

## Tech Stack

- **Web Backend**: PHP
- **Machine Learning & Data Processing**: Python, Pandas, NumPy, Scikit-learn
- **Frontend Interface**: HTML5, CSS3, Bootstrap 5
- **Frontend Interactivity**: jQuery, Select2
- **Data Source**: CSV Dataset

## Installation

### Prerequisites

- PHP 8.0 or higher
- Python 3.8 or higher
- pip (Python package installer)

### Steps

1. Clone the repository to your local machine:

```bash
git clone https://github.com/reynaldiarya/Mobile-Phone-Recommendation-System.git
cd Mobile-Phone-Recommendation-System
```

2. Install the required Python dependencies:

```bash
pip install pandas numpy scikit-learn
```

3. Ensure the dataset `mobile_recommendation_system_dataset.csv` is present in the root directory.

4. Start the built-in PHP development server:

```bash
php -S localhost:8000
```

## Configuration

This application does not require a `.env` file or database configuration. All data processing relies on the local `mobile_recommendation_system_dataset.csv` file. Ensure this file remains in the root directory alongside the Python scripts.

## Usage

### Web Interface

1. Navigate to `http://localhost:8000` in your web browser.
2. Use the search dropdown to select a mobile phone model you are interested in or currently own.
3. Click the "Recommendation" button.
4. The system will process the request and display a grid of the top 8 recommended mobile phones, including their price, RAM, storage, and user rating.

### Command Line Interface

You can also run the recommendation engine directly via the command line to receive raw JSON output:

```bash
python main.py "iPhone 13"
```

## Project Structure

```text
/
├── index.php                                  # Main web interface and PHP-Python bridge
├── main.py                                    # Core ML recommendation engine and data processor
├── search.py                                  # Script to extract unique device names for the frontend
├── mobile_recommendation_system_dataset.csv   # Primary dataset containing device specifications
└── LICENSE                                    # MIT License definition
```

## Scripts / Commands

| Command | Description |
|---------|-------------|
| `php -S localhost:8000` | Start the local PHP development server |
| `python search.py` | Generate a JSON list of all available unique phone models |
| `python main.py "Model"` | Generate JSON recommendations for a specific phone model |

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -m 'Add specific feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for detailed terms and conditions.

## Author

Reynaldi Arya