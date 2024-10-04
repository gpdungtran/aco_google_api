# aco_google_api

This repository contains a Python Flask API that utilizes the Ant Colony Optimization (ACO) algorithm in conjunction with the Google Maps API to determine the shortest routes among multiple locations.

## Description

This API addresses the Traveling Salesperson Problem (TSP) by leveraging the power of ACO and Google Maps. It allows users to input a set of locations and efficiently calculates the optimal route that minimizes travel distance or time.

## Features

* **ACO Implementation:**  Employs the Ant Colony Optimization algorithm to intelligently explore and find the shortest route.
* **Google Maps Integration:**  Utilizes the Google Maps API for accurate distance calculations and route information.
* **Efficient Route Optimization:**  Provides optimized routes for multiple destinations, minimizing travel time or distance.
* **Flexible Input:**  Accepts various input formats for locations (addresses, coordinates, etc.).
* **Customizable Parameters:**  Allows users to adjust ACO parameters (e.g., number of ants, iterations) for fine-grained control.

## Installation

1. Clone the repository: `git clone https://github.com/gpdungtran/aco_google_api.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure API credentials:
    * Obtain Google Maps API credentials from the Google Cloud Console.
    * Create a `config.py` file and store your credentials there.
4. Run the application: `python main.py`

## Usage

* **API documentation:** Access the API documentation at `/docs` (e.g., `http://localhost:5000/docs` if running locally).
* **Example requests:** See the `examples` directory for sample requests demonstrating how to provide locations and retrieve optimized routes.
* **Input Format:**  The API accepts location data in various formats, including lists of addresses, latitude/longitude coordinates, or place IDs.
* **Output Format:**  The API returns the optimized route as a list of locations in the optimal order, along with the total distance and estimated travel time.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bug reports and feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
