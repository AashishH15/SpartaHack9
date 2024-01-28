% Define the filename
filename = 'MCD_data.csv';

% Read the CSV file
data = readtable(filename);

% Display the first few rows of the table
head(data)

dataStruct = table2struct(data);

jsonData = jsonencode(dataStruct);

fileID = fopen('MCD.json', 'w');
fprintf(fileID, jsonData);
fclose(fileID);