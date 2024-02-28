![Header](./docs/header.png)

## About

BSDApp or BSD Subsidiary Database App is an application released on 2024 to manage database of subsidiaries under PT Bumi Serpong Damai Tbk; a company based in Indonesia, founded in 1984 and doing business in real estate / property sector.

The database itself is based on the updated PT Bumi Serpong Damai Tbk Annual Report (latest release is on Year 2022). Users of this app will be able to utilize the features provided here, including:

1. **Show subsidiaries data**: Displays the entire list of current subsidiaries and their properties, ranging from registered company names up to total assets value invested.
2. **Add subsidiaries data**: Helps in registering new subsidiaries and adding their informations to BSD Subsidiaries Database.
3. **Modify subsidiaries data**: Provides options to modify selected values from and into Database.  
(*Limited to changing Ownership, Status, and Total Assets values, for ease of access to users in updating subsidiaries' investment progress*).
4. **Remove subsidiaries data**: Deletes the selected subsidiaries data entirely from Subsidiaries Database.

(*Features 2, 3, and 4 require authorization of users registered to this app.*)

## Usage

Users can clone this program by running the following code:

    git clone git@github.com:garudapaksi-yusuf/BSDApp.git

Users can also launch the program directly by running BSDApp.exe    
## Project Organization

The directory structure of BSDApp project is shown below:

    ├── README.md          <- Top-level README for developers using this project.
    │
    ├── data               <- Up-to-date PT Bumi Serpong Damai Tbk Subsidiaries Database.
    │
    ├── docs               <- Images and other documentation for this project.
    │
    ├── src                <- Source code for BSDApp.
    │
    │── BSDApp.exe         <- BSDApp executable file.
    │
    └── requirements.txt   <- Module requirements for reproducing the program environment;
                              generated with pipreqs > requirements.txt