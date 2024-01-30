data = readtable('GDP.csv');

data = data(1:25, :);

categories = data.COUNTRY; 
yValues = data.GDP;
zValues = data.GDP_PER_CAPITA;

[X,Y] = meshgrid(1:length(categories), 1);

figure;
bar3(X, yValues, repmat(zValues, length(yValues), 1));

view(3);

set(gca, 'XTickLabel', categories);0

xlabel('COUNTRYS');
ylabel('GDP');
zlabel('GDP Per Capita');
title('3D Bar Graph');

dataStruct = table2struct(data);

jsonData = jsonencode(dataStruct);

fileID = fopen('gdp.json', 'w');
fprintf(fileID, jsonData);
fclose(fileID);