##  Chicago Crime Analysis

- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaoji (Jay) Wang - Fall 2024 Semester
- Author: Vamsi Kasukurthi
- GitHub : https://github.com/v-kasukurthi
- Linkedin : https://www.linkedin.com/in/vamsi-kasukurthi-648395191/


##  Background
### What is it about? 
The project is about using chicago crime data to model and understand crime patterns in Chicago. This involves:
1. Identifying trends over time (e.g., by type of crime, location, or season).
2. Using statistical or machine learning techniques to predict crime occurrences.
3. Understanding correlations between various factors (e.g., socioeconomic conditions, neighborhood features) and crime rates.
### Why does it matter? 
It helps local authorities allocate resources more effectively (e.g., police presence). Understanding crime patterns can aid in policymaking to reduce crime rates. It contributes to improving public safety by providing insights into when and where crimes are more likely to occur. Predictive models can be used in urban planning and community development to mitigate factors that may lead to higher crime rates.
### Research Questions:
1. What types of crimes are most frequent in specific neighborhoods of Chicago?
2. Are there time-based patterns (e.g., certain crimes happening more at night or during specific seasons)?
3. What socioeconomic or environmental factors contribute most significantly to crime?
4. Can spatial analysis identify accident hotspots, and how do traffic volume and speed limits relate to crash rates?
5. Can crime be accurately predicted using historical data and various machine learning algorithms?



##  DATA
Description : 

1. Data Source : *[Chicago Data Portal](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if/data](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/about_data)*. :link:

2. Data Size : 1.7 GB

3. Data Shape
   > - Number of columns =  22
   > - Number of rows    = 8.15M

4. Time period (2001 - present)
5. What does dataset represent - This dataset reflects reported incidents of crime (with the exception of murders where data exists for each victim) that occurred in the City of Chicago from 2001 to present, minus the most recent seven days.
6. Data Dictionary
   
### Data Dictionary

| **Column Name**                        | **Description**                                                                    |
|----------------------------------------|------------------------------------------------------------------------------------|
| `ID`                              | Unique identifier for the record.                                   |
| `Case Number`                     | The Chicago Police Department RD Number (Records Division Number), which is unique to the incident.                           |
| `DATE`                            | Date when the incident occurred. this is sometimes a best estimate.                                      |
| `Block`                           | The partially redacted address where the incident occurred, placing it on the same block as the actual address.                                          |
| `IUCR`                            | The Illinois Unifrom Crime Reporting code. This is directly linked to the Primary Type and Description. See the list of IUCR codes at https://data.cityofchicago.org/d/c7ck-438e.                      |
| `Primary Type`                    | The primary description of the IUCR code                                           |
| `Description`                     | The secondary description of the IUCR code, a subcategory of the primary description.                                       |
| `Location Description`            | Description of the location where the incident occurred.                                             |
| `Arrest`                          | Indicates whether an arrest was made.                                             |
| `Domestic`                        | Indicates whether the incident was domestic-related as defined by the Illinois Domestic Violence Act.                                       |
| `Beat`                            | Indicates the beat where the incident occurred. A beat is the smallest police geographic area – each beat has a dedicated police beat car. Three to five beats make up a police sector, and three sectors make up a police district.                                             |
| `District`                        | Indicates the police district where the incident occurred.                                |
| `Ward`                            | The ward (City Council district) where the incident occurred                                   |
| `Community Area`                  | Indicates the community area where the incident occurred. Chicago has 77 community areas.                                    |
| `FBI Code`                        | Indicates the crime classification as outlined in the FBI's National Incident-Based Reporting System (NIBRS).                                               |
| `X Coordinate`                    | The x coordinate of the location where the incident occurred in State Plane Illinois East NAD 1983 projection. This location is shifted from the actual location for partial redaction but falls on the same block.                                          |
| `Y Coordinate`                    | The y coordinate of the location where the incident occurred in State Plane Illinois East NAD 1983 projection. This location is shifted from the actual location for partial redaction but falls on the same block.                                       |
| `Year`                            | Year the incident occurred.                                       |
| `Updated on`                      | Date and time the record was last updated                                          |
| `Latitude`                        | The latitude of the location where the incident occurred. This location is shifted from the actual location for partial redaction but falls on the same block.                                           |
| `Longitude`                       | The longitude of the location where the incident occurred. This location is shifted from the actual location for partial redaction but falls on the same block.                          |
| `Location`                        | The location where the incident occurred in a format that allows for creation of maps and other geographic operations on this data portal. This location is shifted from the actual location for partial redaction but falls on the same block.                                           |


