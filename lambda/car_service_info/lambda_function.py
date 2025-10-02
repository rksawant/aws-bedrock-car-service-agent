import json

def lambda_handler(event, context):
    # Print event for debugging
    print("Received event:", json.dumps(event))
    
    # Extract plate number safely (handle Bedrock wrapper)
    plate = event.get("plate_number") or event.get("request", {}).get("plate_number", "UNKNOWN")
    
    # Mock service info logic
    if plate == "MH12AB1234":
        message = f"Next service for {plate} is on 2025-11-15."
    else:
        message = f"No service information found for {plate}."
    
    # Return JSON object matching OpenAPI schema
    return {
        "message": message
    }
