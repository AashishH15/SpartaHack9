% MATLAB code to create a 3D bar graph from CSV data

file_path = 'BKW_data.csv';
data = readtable(file_path);

names = data.name;
dollar_prices = data.dollar_price;

third_var = ones(size(dollar_prices));

bar3(dollar_prices);

set(gca, 'XTickLabel',names, 'XTick',1:numel(names), 'YTickLabel',third_var, 'YTick',1:numel(third_var))

title('The Whopper Index');
xlabel('Country');
ylabel('Third Variable');
zlabel('Cost of Whopper (USD)');