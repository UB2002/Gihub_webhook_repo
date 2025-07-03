from datetime import datetime

def format_event(payload, event_type):
    timestamp = datetime.utcnow().isoformat() + "Z"

    if event_type == "push":
        return {
            "request_id": payload["head_commit"]["id"],
            "author": payload["pusher"]["name"],
            "action": "PUSH",
            "from_branch": None,
            "to_branch": payload["ref"].split("/")[-1],
            "timestamp": timestamp
        }

    if event_type == "pull_request":
        pr = payload.get("pull_request", {})
        action = payload.get("action")
        pr_id = str(pr.get("id"))

        if action == "opened":
            return {
                "request_id": pr_id,
                "author": pr["user"]["login"],
                "action": "PULL_REQUEST",
                "from_branch": pr["head"]["ref"],
                "to_branch": pr["base"]["ref"],
                "timestamp": timestamp
            }

        if action == "closed" and pr.get("merged"):
            return {
                "request_id": pr_id,
                "author": pr["user"]["login"],
                "action": "MERGE",
                "from_branch": pr["head"]["ref"],
                "to_branch": pr["base"]["ref"],
                "timestamp": timestamp
            }

    return None
