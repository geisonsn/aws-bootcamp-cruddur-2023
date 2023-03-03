from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder

class NotificationsActivities:
  def run(): 

    segment = xray_recorder.begin_segment("api/activities/notifications")

    now = datetime.now(timezone.utc).astimezone()

    query_input = {
      "date": now.astimezone()
    }

    segment.put_metadata('query-input', query_input, "database-request")
    
    subsegment = xray_recorder.begin_subsegment('database-request')

    results = [{
      'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
      'handle':  'Lightning McQueen',
      'message': 'Cloud is fast!',
      'created_at': (now - timedelta(days=2)).isoformat(),
      'expires_at': (now + timedelta(days=5)).isoformat(),
      'likes_count': 500,
      'replies_count': 1,
      'reposts_count': 0,
      'replies': [{
        'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
        'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
        'handle':  'Mater',
        'message': 'Indeed!',
        'likes_count': 1000,
        'replies_count': 0,
        'reposts_count': 0,
        'created_at': (now - timedelta(days=2)).isoformat()
      }],
    },
    ]

    subsegment.put_annotation('type', "query")   
    data = {
      "result": results,
      "size": len(results)
    }
    subsegment.put_metadata("database-result", data, "database-request")
  
    return results