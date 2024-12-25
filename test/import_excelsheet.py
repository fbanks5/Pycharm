import openpyxl
import requests

file_path = 'Desktop/test_spreadsheet.xlsx'
workbook = openpyxl.load_workbook(file_path)
sheet = workbook.active

start_row = 3
end_row = 31
software_column = 'A'
version_column = 'B'

api_base_url = 'https://endoflife.date/api/software/'

def fetch_eol_data(software_name):
    try:
        response = requests.get(f"{api_base_url}{software_name}.json")
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {software_name}: {e}")
        return None

for row in range(start_row, end_row + 1):
    software_name = sheet[f"{software_column}{row}"].value
    version = sheet[f"{version_column}{row}"].value
    eol_data = fetch_eol_data(software_name)

    if software_name:
        eol_data = fetch_eol_data(software_name.lower().replace(' ', '-'))

        if eol_data:
            print(f"Software: {software_name}, Version: {version}")
            for release in eol_data.get('releases', []):
                print(f"Release: {release.get('releaseCycle')}, EOL Date: {release.get('eol_date')}, Latest: {release.get('latest')}")
        else:
            print(f"Error fetching EOL data for {software_name}")
        #     eol_date = eol_data.get('eol_date')
        #     if eol_date:
        #         sheet[f"{version_column}{row}"] = eol_date
        #     else:
        #         print(f"No EOL data found for {software_name}")
        # else:
        #     print(f"Error fetching EOL data for {software_name}")

