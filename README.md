# SpartaHack9

## Description

This project is a data analysis tool for SpartaHack9. It includes various scripts for data processing and visualization.

## Installation

1. Clone the repository
2. Install the required Python packages

```sh
pip install -r requirements.txt
```

## Usage
To use this project, follow these steps:

1. Start the Flask server by running `main.py`:

```
python main.py
```


2. Open your web browser and navigate to `http://localhost:5000`.

3. Use the links to download the data files.

4. Use the `updateContent(filename)` JavaScript function in the browser's console to update the content of the map and bar graph iframes. Replace `filename` with the name of the data file you want to visualize (e.g., "BKW_data.csv").

## Functions

- `create_bar_chart(filename)` in [`bargraph.py`](bargraph.py): Creates a bar chart based on the data in the specified file.

- `generate_map(filename)` in [`map.py`](map.py): Generates a map based on the data in the specified file.

## Credits
This project was developed by [Aashish Harishcandre](https://github.com/AashishH15), [Ethan Cook](https://github.com/ethancook2), [Alia Fatima](https://github.com/notalia) and [Varun Kumar](https://github.com/Vvarunv1). Special thanks to [SpartaHacks9](https://spartahack-9.devpost.com/?ref_feature=challenge&ref_medium=your-open-hackathons&ref_content=Recently+ended).

## License
This project is licensed under the MIT License.