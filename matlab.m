% % Generate random data
% data = randn(1000, 3);

% % Create a 2D histogram
% [N, Xedges, Yedges] = histcounts2(data(:,1), data(:,2), [20 20]);

% % Create a 3D bar plot
% figure;
% bar3(N);

% % Set the view angle
% view(3);

% % Add labels and title
% xlabel('X');
% ylabel('Y');
% zlabel('Frequency');
% title('3D Histogram');

% % Define the categories (strings)
% categories = {'Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'};

% % Define the y and z values (floats)
% yValues = [1.2, 2.3, 3.4, 4.5, 5.6];
% zValues = [2.1, 3.2, 4.3, 5.4, 6.5];

% % Create a grid for the 3D bar plot
% [X,Y] = meshgrid(1:length(categories), 1);

% % Create the 3D bar plot
% figure;
% bar3(X, yValues, repmat(zValues, length(yValues), 1));

% % Set the view angle
% view(3);

% % Set the x-tick labels to the categories
% set(gca, 'XTickLabel', categories);

% % Add labels and title
% xlabel('Fruit Names');
% ylabel('Y Values');
% zlabel('Z Values');
% title('3D Bar Graph');

% Read the data from the CSV file
data = readtable('GDP.csv');

% Extract the categories, y values, and z values
categories = data.COUNTRY;  % Replace 'Category' with the actual column name for the categories
yValues = data.GDP;  % Replace 'YValues' with the actual column name for the y values
zValues = data.GDP_PER_CAPITA;  % Replace 'ZValues' with the actual column name for the z values

% Create a grid for the 3D bar plot
[X,Y] = meshgrid(1:length(categories), 1);

% Create the 3D bar plot
figure;
bar3(X, yValues, repmat(zValues, length(yValues), 1));

% Set the view angle
view(3);

% Set the x-tick labels to the categories
set(gca, 'XTickLabel', categories);

% Add labels and title
xlabel('COUNTRYS');
ylabel('GDP');
zlabel('GDP Per Capita');
title('3D Bar Graph');