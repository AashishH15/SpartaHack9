% Define the filename
filename = 'BKW_data.csv';

% Read the CSV file
data = readtable(filename);

% Display the first few rows of the table
head(data)

dataStruct = table2struct(data);

jsonData = jsonencode(dataStruct);

fileID = fopen('BKW.json', 'w');
fprintf(fileID, jsonData);
fclose(fileID);