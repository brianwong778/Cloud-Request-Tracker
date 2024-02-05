<h1 align="center">Cloud-Request-Tracker</h1>

<p align="center">
  A Cloud Request Tracker deployed on <strong>Google Cloud Platform</strong>. This application leverages <strong>Docker</strong> and <strong>Google Kubernetes Engine (GKE)</strong> for efficient deployment and scalability. At its core, it's built using <strong>Flask</strong> for the web framework, with <strong>MySQL</strong> for database management, and integrates seamlessly with <strong>Google Cloud Storage (GCS)</strong> and <strong>Pub/Sub APIs</strong> for messaging and storage solutions.
</p>

## Features

- **Content Generation**: Users can utilize `content-generator.py` to generate HTML files, creating a network of 10,000 interlinked documents. These files are then stored in a Google Cloud Storage bucket, ready for access.
- **Simulation and Access**: The system simulates HTTP requests with diverse parameters like country, IP, gender, age, income, time, and the requested file, allowing users to access file content through the IP address of the Kubernetes cluster.
- **Error Handling**: Erroneous requests, particularly those originating from "banned countries", are efficiently managed and relayed between VMs using Google's robust Pub/Sub API, ensuring secure and reliable request handling.
- **Data Storage**: All requests and their metadata are meticulously stored in a MySQL instance hosted on GCP, providing a comprehensive data management solution.

## Demonstration

Below are snapshots providing insights into HTTP access via a browser, the dynamics of generated requests, and the handling of erroneous requests from restricted locations:

<p align="center">
  <img src="https://github.com/brianwong778/Cloud-Stream-Tracker-Pub-Sub-/assets/113395187/6bfe1c61-d028-4b28-ac8d-cf25f52fff53" alt="HTTP Access Snapshot">
</p>

<p align="center">
  <img src="https://github.com/brianwong778/Cloud-Stream-Tracker/assets/113395187/f2873fc9-5530-479a-8cac-c30c10664965" alt="Generated Requests">
</p>

<p align="center">
  <img src="https://github.com/brianwong778/Cloud-Stream-Tracker/assets/113395187/1a19e16b-fe85-48b0-9998-f1d116d03523" alt="Erroneous Request Logs">
</p>
