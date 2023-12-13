# Cloud-Stream-Tracker
Cloud Stream Tracker deployed on Google Cloud Platform. Utilizes GCP VM's for hosting. Built on Flask with MySQL, GCS and Pub/Sub APIs.

Users can access file content via an IP address hosted on a virtual machine (VM) within GCP. With the help of an HTTP request generator, 
the system tracks each request. Any requests deemed erroneous, especially those originating from simulated 
"banned countries", are relayed between VMs using Google's Pub/Sub API. Requests are stored in a MySQL instance hosted on GCP.

Below is a snapshot showcasing http access via browser, the generated requests and the corresponding erroneous request logs from the banned locations:


![2DA4D11A-A5CD-4B52-AC04-D59B09BF9CA0_1_201_a](https://github.com/brianwong778/Cloud-Stream-Tracker-Pub-Sub-/assets/113395187/6bfe1c61-d028-4b28-ac8d-cf25f52fff53)

![ezgif com-video-to-gif-converted](https://github.com/brianwong778/Cloud-Stream-Tracker/assets/113395187/f2873fc9-5530-479a-8cac-c30c10664965)

![Screenshot 2023-12-12 at 9 48 28 PM](https://github.com/brianwong778/Cloud-Stream-Tracker/assets/113395187/1a19e16b-fe85-48b0-9998-f1d116d03523)
