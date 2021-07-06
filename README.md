# Stepik Tours: Project 2

This is a part of my learning at https://stepik.org/course/63298.

The Django application presented here shows three types of pages:

- ``main`` shows a list of departures and tours
- ``departure`` shows a list of tours available from a particular city
-  ``tour`` presents a particular tour's details

## Prerequisites

The application requires Python 3.7 or a newer version.

## Installation

To use this application, go through the following steps:

1. Download this repository and unpack it. This will create the ``stepik_tour2-main`` directory.
0. Go in this directory:

    ```bazaar
    cd stepik_tour2-main
    ```

0. Create a Python virtual environment:

    ```bazaar
    python3 -m venv venv
    ```
   
0. Activate the virtual environment:

    ```bazaar
    source venv/bin/activate
    ```
   
0. Install the required Python packages:

    ```bazaar
    pip install -r requirements.txt
    ```
   
0. Run the application:

    ```bazaar
    ./manage.py runserver
    ```
   
0. Address your browser to the following URLs:

    -   http://localhost:8000/
    -   http://localhost:8000/departure/nsk/
    -   http://localhost:8000/tour/1/
    
That's it. See you in Project 3.
