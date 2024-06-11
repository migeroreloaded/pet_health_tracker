# Pet Health Tracker

This is a CLI and ORM project by *Michael George* first created in June 2024

## Description

A CLI application to track pet health records and appointments.

## How to Run

### Setup

1. **Clone the repository:**

   ```sh
   git clone git@github.com:migeroreloaded/pet_health_tracker.git

   cd pet_health_tracker

2. Or by downloading a ZIP file of the code. The repository, if downloaded as a .zip file will need to be extracted to your preferred location.

3. **Install the dependacies**

    ```sh
    pipenv install

4. **Initialize the database**

    ```sh
    pipenv run python lib/db/seed.py

### Usage

1. **Register a User**

    ```sh
    pipenv run python lib/cli/main.py register --username petlover --password secret --email petlover@example.com

2. **Login a User**

    ```sh
    pipenv run python lib/cli/main.py login --username petlover --password secret

3. **Add a Pet**

    ```sh
    pipenv run python lib/cli/main.py add_pet --user_id 1 --name Bella --species Dog --breed Labrador --age 3

4. **Log a Health Record**

    ```sh
    pipenv run python lib/cli/main.py log_health --pet_id 1 --visit_date 2024-06-01 --notes "Annual vaccination"

5. **View Health Records**

    ```sh
    pipenv run python lib/cli/main.py view_health --pet_id 1

6. **Set an Appointment**

    ```sh
    pipenv run python lib/cli/main.py set_appointment --pet_id 1 --appointment_date 2024-07-01 --details "Dental cleaning"

7. **View Appointments**

    ```sh
    pipenv run python lib/cli/main.py view_appointments --user_id 1

## Contact

For any questions or concerns please reach out to me at:  
[Email](mailto:mikeroche138@gmail.com)

## License

The content of this site is licensed under the MIT license

Copyright &copy; 2024 Migero

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
