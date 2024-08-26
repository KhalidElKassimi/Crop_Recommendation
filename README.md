# Crop_Recommendation
Welcome to the Crops Recommendation System project. This repository contains the implementation of a comprehensive data pipeline and machine learning system designed to optimize agricultural practices by providing crop recommendations based on various environmental and soil metrics.

The project leverages multiple tools and technologies, including Flask for serving data, Azure Event Hub for data streaming, Azure Stream Analytics for real-time data processing, Azure Data Lake for storage, Synapse Analytics for building a data warehouse, and Databricks for advanced analytics and machine learning. Additionally, Power BI is used for data visualization to derive actionable insights.

Key features of this project include:

- Real-Time Data Processing: Stream agricultural data in real-time from a local source to the cloud using Azure Event Hub.
- Data Storage and Warehousing: Store and manage large volumes of agricultural data efficiently using Azure Data Lake and Synapse Analytics.
- Machine Learning: Train and deploy machine learning models using Databricks to provide accurate crop recommendations.
- Data Visualization: Visualize key agricultural metrics and insights using Power BI to support data-driven decision-making.

![image022](https://github.com/user-attachments/assets/d1e49c72-d0fe-4aba-a447-5897bdfc0094)

## Data Source

The provided Python code implements a Flask web application to serve data from a CSV file named `cropmetrics.csv`. It uses the `Flask` framework and the `pandas` library.

- Loads CSV into DataFrame (`df`) using `pd.read_csv`.
- Defines an endpoint (`/get_data`) accessible via HTTP GET requests.
- Returns data in batches of 5 rows.
- Uses a global counter (`current_line`) to track the dataset's position.
- Introduces a simulated delay of one minute (`time.sleep(60)`).

The Flask app runs when the script is executed directly (`if __name__ == '__main__': app.run(debug=False)`).

The CSV file contains agricultural data about crop metrics, with columns like Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, Rainfall, Label, Latitude, Longitude, Ville (City), Province, and `id_position`.




## Azure Event Hub Producer Script

The script fetches data from a local endpoint and sends it to an Azure Event Hub.

1. **Local Data Endpoint:**
    - `local_data_endpoint`: Specifies the endpoint (`http://127.0.0.1:5000/get_data`) for data fetching.

2. **Azure Event Hub Configuration:**
    - `connection_str`: Connection string for the Event Hub.
    - `eventhub_name`: Name of the target Event Hub (`pakostrealing`).

3. **Event Hub Producer Client Initialization:**
    - Initializes `EventHubProducerClient` with the connection string and Event Hub name.

4. **Data Fetching and Sending:**
    - Fetches data and sends it to the Event Hub.
    - Logs fetched data and converts it to a string before sending.

5. **Logging:**
    - Configures basic logging at the INFO level.

6. **Execution:**
    - Runs in an infinite loop to continuously fetch and send data.

7. **Error Handling:**
    - Implements exception handling for errors during data fetching and sending.

![image](https://github.com/user-attachments/assets/435a4565-4110-409b-8c81-187d28178d7c)

## Streaming Data with Azure Stream Analytics and Store it In DataLake

Azure Stream Analytics processes real-time data from the Event Hub `pakostrealing` and stores it in Data Lake Gen2 `pakodatalake`.

![Capture d'écran 2024-01-12 194149](https://github.com/user-attachments/assets/ae221bdd-4d26-4983-a7a0-fd20230394a6)

Stream Analytics ensures continuous flow and storage of real-time data from the source to Data Lake Gen2, enabling efficient storage and analysis.

![Capture d'écran 2024-01-12 194426](https://github.com/user-attachments/assets/2e847fb1-8956-477e-8904-efb819475747)


## Creating a Data Warehouse in Synapse Analytics

The data warehouse schema in Azure Synapse Analytics includes:

- **Fact Table (`crops`):** Stores agricultural metrics.
- **Dimension Tables:** 
  - `crops_label`: Lookup table for crop labels.
  - `position`: Geographical information.
  - `temps`: Time dimension.

Data is stored in Data Lake paths:
- `pakodatalake/pakogrowdw/crops`
- `pakodatalake/pakogrowdw/crops_label`
- `pakodatalake/pakogrowdw/position`
- `pakodatalake/pakogrowdw/temps`

![image](https://github.com/user-attachments/assets/140ae9ce-66e9-4b03-acfb-747d30f89f72)

![image](https://github.com/user-attachments/assets/bee636cd-219c-4bdf-a694-f921c66cf430)

## Databricks Overview

Databricks is a unified analytics platform built on Apache Spark, providing a collaborative environment for data scientists, engineers, and analysts.

### Workflow Description

#### Notebook: Models

Trains four machine learning models and evaluates them, selecting RandomForestClassifier as the best.

![image](https://github.com/user-attachments/assets/d48bb36a-e1e4-487c-9923-61cbe09c5abe)


#### Notebook: Crops

Uses RandomForestClassifier to predict crop labels for streaming data from Azure ADLS Gen2.

![Capture d'écran 2024-01-12 195430](https://github.com/user-attachments/assets/ef613204-10b1-4843-aa03-ca62c99e1a96)


#### Notebook: Temps

Processes streaming data to filter and format time information, storing it in the `temps` dimension table.

### Further Elaboration

#### Streaming Data Ingestion

Uses `spark.readStream` to ingest data continuously.

#### Model Training

Trains machine learning models using Spark's ML libraries.

#### Prediction and Fact Table Update

Predicts crop labels and updates the fact table using `spark.writeStream`.

#### Time Filtering and Dimension Table Update

Filters and formats time data, updating the `temps` dimension table using `spark.writeStream`.

## Data Visualization with Power BI

Power BI is used to visualize data, deriving insights crucial for optimizing crop distribution. It analyzes crop distribution, soil, and air conditions, and farm locations across Morocco. Power BI's filtering capabilities enhance data analysis by date, city, crop labels, temperature, and rainfall.

![Capture d'écran 2024-01-12 200127](https://github.com/user-attachments/assets/a41a5c2d-615c-48aa-9efe-e38c6bf09d2b)

