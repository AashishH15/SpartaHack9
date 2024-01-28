% Generate random data
data = randn(1000, 3);

% Create a 2D histogram
[N, Xedges, Yedges] = histcounts2(data(:,1), data(:,2), [20 20]);

% Create a 3D bar plot
figure;
bar3(N);

% Set the view angle
view(3);

% Add labels and title
xlabel('X');
ylabel('Y');
zlabel('Frequency');
title('3D Histogram');