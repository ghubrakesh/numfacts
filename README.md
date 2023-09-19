# Cool Facts About Numbers

Cool Number Facts is a web application built with FastAPI that allows users to retrieve interesting facts about numbers. Users can enter a number, and the application will fetch a fascinating fact related to that number using the Numbers API.

You can access the live deployment of this application [here](https://getcoolnumfacts.onrender.com/).

## Features

- Enter a number to get a cool fact related to that number.
- Responsive design for both desktop and mobile users.
- Easy navigation with a "Go Back" button.
- Stylish user interface.

## Installation

To run this application locally, follow these steps:

1. Clone this repository:
   ```shell
   git clone https://github.com/ghubrakesh/numfacts.git
   ```   
2. Change into the project directory:
   ```shell
   cd cool-number-facts
   ```
3. Install the required dependencies using pip:
   ```shell
   pip install -r requirements.txt
   ```
4. Start the FastAPI development server:
   ```shell
   uvicorn app:app --reload
   ```
5. Open your web browser and navigate to `http://localhost:8000` to use the application locally.

## Usage
1. Open the website: https://getcoolnumfacts.onrender.com
2. Enter a number in the input field on the home page.
3. Click the "Get the Fact" button.
4. The application will fetch an interesting fact related to the entered number from the Numbers API and display it on the result page.
5. Click the "Go Back" button to return to the home page and enter another number.

## Technologies Used
1. FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.
2. Jinja2: A modern and designer-friendly templating engine for Python.
3. Requests: A Python library for making HTTP requests.



## Preview
1. Login Page
  ![Screenshot from 2023-09-19 20-57-41](https://github.com/ghubrakesh/numfacts/assets/102187286/e80976f2-8292-4584-b043-6bc6d348e0bb)

2. Fact Page
   ![Screenshot from 2023-09-19 20-57-23](https://github.com/ghubrakesh/numfacts/assets/102187286/f05c81bd-5e28-4c93-b54f-a0cfe68c2b4b)


## Contributing
Contributions are welcome! If you have any improvements, bug fixes, or feature requests, please open an issue or submit a pull request.
