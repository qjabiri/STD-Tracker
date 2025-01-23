# STD Tracker

## Overview
The STD Tracker project consists of a Python script (`stdTracker.py`) and data files (`STD.txt` and `STD.csv`) that provide a way to analyze and identify potential sexually transmitted diseases (STDs) based on user-provided symptoms and affected body locations.

## Project Structure
├── stdTracker.py # Main script to analyze STD data ├── STD.txt # Text database containing STD details ├── STD.csv # CSV version of the STD data (optional) ├── README.md # Project documentation

## Files Description

### 1. `stdTracker.py`
This Python script processes STD information from the `STD.txt` file and allows users to input symptoms and affected body locations to identify potential diseases. The script consists of the following functions:

- **`file_view(ss)`**  
  - Reads the provided STD database file.
  - Organizes data into dictionaries for symptoms, locations, and additional resources.

- **`Symptoms(symptoms, isymptoms)`**  
  - Matches user-reported symptoms against known disease symptoms.
  - Returns a list of possible diseases.

- **`Location(location, ilocation)`**  
  - Matches user-reported locations against known disease locations.
  - Returns a list of potential diseases.

- **`main()`**  
  - The main function orchestrates the program, allowing users to input symptoms and affected locations.
  - Combines results from symptom and location matching to suggest possible STDs.
  - Displays helpful resource links for further information.

### 2. `STD.txt`
A text-based database that includes information about various STDs. The format for each disease entry follows this pattern:

<Disease Name> : <Symptoms> : <Affected Locations> : <Resource Link>

**Example Entry:**
chlamydia : White, yellow or gray discharge, Painful urination : Vagina More: www.cdc.gov/chlamydia


### 3. `STD.csv`
A CSV file containing similar information to `STD.txt`, structured in a tabular format with the following columns:

Disease, Symptoms, Location, Resource Link

## How to Run the Program

1. Ensure you have Python 3 installed.
2. Open a terminal and navigate to the project directory.
3. Run the script:

   ```bash
   python3 stdTracker.py
Follow the prompts to enter symptoms and locations.
The program will output potential diseases and provide links to more information.
Example Usage
Input:


Please list all symptoms that you are feeling (type 'e' to end): 
> itching
> burning
> e
Please list all locations where you feel symptoms (type 'e' to end): 
> genitalia
> e
Output:

Your possible diseases are:
trichomoniasis - More: www.cdc.gov/std/trichomonas/stdfact-trichomoniasis
Requirements
Python 3.x
No additional dependencies required.

Potential Improvements:
Enhance the user interface for better interaction.
Add data visualization for disease prevalence.
Integrate an online API for real-time updates.


License
This project is released under the MIT License.
