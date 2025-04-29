# Contributing

For major changes, please open an issue first to discuss what you would like to change.

The following instructions and guidelines are meant for those brave and motivated persons that want to actively contribute to the development of the material.

### Guidelines for contributing

1. Follow the [instructions](#installation-instructions) to set up this folder on your local machine.

1. Familiarize yourself with the guide on how to [quick start](https://docs.marimo.io/getting_started/quickstart/) with _marimo_ notebooks and their [key concepts](https://docs.marimo.io/getting_started/key_concepts/).

1. Create and modify _marimo_ notebooks primarily from the Command Line Interface (CLI) in a terminal. Use the VSCode _marimo_ extension _exclusively_ for minor, cosmetic, changes

### Installation instructions

1. Install [Python 3.12 or higher](https://www.python.org/downloads/) and optionally add it to your PATH.

2. Clone the repository from Github: 

    ```git clone https://github.com/CarmVarriale/FlightPerfCalculus.git```

3. Navigate to the cloned directory:

    ```cd your/path/to/FlightPerfCalculus```

4. Create a virtual environment (optional but recommended):

    ```.\.venv\Scripts\python -m venv .venv```

5. Activate the virtual environment:
   - On Windows: ```.\.venv\Scripts\activate.bat```
   - On macOS/Linux: ```source .venv/bin/activate```

6. Install the required dependencies:
    
    ```.venv\Scripts\python -m pip install -r requirements.txt```

7. Test the correct installation of the _marimo_ dependencies by running the following command:

    ```.venv\Scripts\python -m marimo tutorial intro```