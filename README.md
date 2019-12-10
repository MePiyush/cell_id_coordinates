## Fetch Location Data(Latitude/Longitude) of Cell Towers from LocationAPI(http://www.locationapi.org/) & CellPhoneTrackers(http://cellphonetrackers.org/)

### Usage
- Store the Cell IDs in Column[1] and LAC(Location Area Code) in Column[2] both in Decimal Format in a CSV File which will be used as an Input File
- Enter the Path of the Input File
- Enter the path where you want to generate the Output File
- Get the API Token from LocationAPI. You can request the Developer Token from [here](http://www.locationapi.org/site/trial)
- Enter the value of the Token
- Enter the value of MCC(Mobile Country Code), MNC(Mobile Network Code)
- Run the script from terminal: python CellIDCoordinates.py
- Output file will be generated in the path specified in step [3] with the current TimeStamp as the filename
