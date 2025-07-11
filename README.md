Webhook Receiver - Developer Assessment Task


A full-stack application that listens for GitHub events like "push", "pull request", and "merge", stores them in MongoDB, and displays them live on a real-time dashboard.

____________________________________________________________________________________________________________________________________________________________________________________________________________________

Repositories Involved

This project involves two repositories:

1.[`action-repo`](https://github.com/vaishu0803/action-repo)  
   GitHub repository where actions like push, PR, and merge are performed.

2.[`webhook-repo`](https://github.com/vaishu0803/webhook-repo) _(this repo)_  
   A Flask server that receives webhook events and shows them on a dashboard.

____________________________________________________________________________________________________________________________________________________________________________________________________________________

 Tech Stack

1. Python (Flask)
2. MongoDB Atlas
3. HTML + JavaScript
4.GitHub Webhooks
5.ngrok (local tunneling)

____________________________________________________________________________________________________________________________________________________________________________________________________________________

 Features

- Receives GitHub events: "push", "pull_request", and "merge"
- Stores event data in MongoDB using a clean schema
- Displays the 10 most recent events in a simple UI
- UI auto-refreshes every 15 seconds using JavaScript
- Easily extensible for more event types

____________________________________________________________________________________________________________________________________________________________________________________________________________________

MongoDB Schema

Each webhook event is stored with the following fields:

```json
{
  "request_id": "UUID",
  "author": "vaishu0803",
  "action": "push",
  "from_branch": "feature",
  "to_branch": "main",
  "timestamp": "11 July 2025 - 12:31 PM UTC"
}
```
____________________________________________________________________________________________________________________________________________________________________________________________________________________



 Setup Instructions

Prerequisites
- Python 3
- Git
- MongoDB Atlas account
- Ngrok account

____________________________________________________________________________________________________________________________________________________________________________________________________________________

STEPS 
1. Clone the repository

```bash
git clone https://github.com/vaishu0803/webhook-repo.git
cd webhook-repo
```

---

2. Create a `.env` file with your MongoDB URI

```
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority
```

You can get this from MongoDB Atlas → Connect → Drivers → Connection String.

---

3. Install dependencies

```bash
pip install flask pymongo python-dotenv
```

---

 4. Run the Flask app

```bash
python app.py
```

The server will start at:  
`http://127.0.0.1:5000/`

---

5. Start ngrok to expose it

```bash
ngrok http 5000
```

Copy the generated HTTPS URL — e.g.  
`https://abcd1234.ngrok-free.app`

---

6. Setup GitHub Webhook

Go to your `action-repo` → **Settings → Webhooks → Add webhook**

- Payload URL: `https://your-ngrok-url/webhooK`
- Content type:`application/json`
- Events: Check `Just the push event`, `pull_request`, and optionally `merge` (handled as merged PR)

---

7. View Webhook Events Dashboard

Visit:  
`http://localhost:5000/`  
It will show the 10 most recent events and auto-refresh every 15 seconds.

---

 UI Preview

```
Author: vaishu0803  
Action: push  
Branch: feature → main  
Time: 11 July 2025 - 12:31 PM UTC  
```

---

 Bonus: Merge Detection

If a pull request is merged (`action: closed`, `merged: true`), it's detected and recorded as a `merge` event.

____________________________________________________________________________________________________________________________________________________________________________________________________________________

 Author

  Vaishnavi Reddy 
📧 vaishuyenumula@gmail.com  
🌐 [github.com/vaishu0803](https://github.com/vaishu0803)

____________________________________________________________________________________________________________________________________________________________________________________________________________________

 Final Notes

- This project is part of a developer assessment for webhook integration.
- Built with a focus on minimal UI, real-time backend, and clean data handling.
