# Pet Health Tracker

This is a CLI and ORM project by *Michael George* first created in June 2024

## Description

Pet Health Tracker is a command-line interface (CLI) application built in Python to help pet owners manage their pets' health records and appointments. This application allows users to register/login, add pets, log health records, set appointments, and view pet health-related information conveniently from the terminal.

### Features

- **User Management:** Users can register new accounts and log in securely.
- **Pet Management:** Add pets with details like name, species, breed, and age.
- **Health Records:** Log health records for pets, including visit dates and notes.
- **Appointments:** Set appointments for pets with details like appointment date and description.
- **View Records and Appointments:** Easily view health records and upcoming appointments.

## How to Run

### Setup

1. **Clone the repository and navigate to project directory:**

   ```sh
   git clone git@github.com:migeroreloaded/pet_health_tracker.git

   cd pet_health_tracker

2. Or by downloading a ZIP file of the code. The repository, if downloaded as a .zip file will need to be extracted to your preferred location.

3. **Install the dependacies and launch shell environment**

    ```sh
    pipenv install

    pipenv shell

4. **Initialize the database**

    ```sh
    pipenv run python lib/db/seed.py

### Usage

1. **To run the apllication use**

    ```sh
    python lib/cli/main.py

2. Follow the on-screen instructions to register/login, manage pets, log health records, set appointments, and view information.

## Contact

For any questions or concerns please reach out to me at:  
[Email](mailto:mikeroche138@gmail.com)

## License

The content of this site is licensed under the MIT license

Copyright &copy; 2024 Migero

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
