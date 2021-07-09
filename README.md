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
 
## Pluralize countable nouns

This is how it works in the project.

1. In the project folder (or maybe in the app folder), create the **templatetags** folder.
2. In **templatetags**, create **__init__.py**.
3. In **templatetags**, create **  ru_pluralize.py**, whose content is in this project.
4. In the template, after {% extends ...%}, add the module loading {% load ru_pluralize %}.
5. Example of the use:  {{ days|ru_pluralize:"день, дня, дней" }}
   
## Custom Context Processor

0. In the application folder (``tours``, in this project), create a module with your custom processor,
   e.g., ``custom_context_processor.py``.
0. In this module, add the content as in this project.
0. In the ``settings.py`` file, add the custom Context Processor to the list of Custom Processors:

   ```bazaar
      'tours.custom_context_processor.common_context'
   ```
0. In a template (``base.html``, in this project), use the context parameters defined in the custom processor, e.g.:

   ```bazaar
      <title>{{ main_title }}</title>
   ```

That's it. See you in the next project.

