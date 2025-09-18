from agent_x.sub_agents.validator_agent.tools import connect_to_db


def get_reporting_data():
    collection_ref = connect_to_db()
    docs = collection_ref.stream()
    records = [doc.to_dict() for doc in docs]
    print("Record:", records)
    return {"status": "success", "data": records}

def get_reporting_data_for_chart():
    collection_ref = connect_to_db()
    docs = collection_ref.stream()
    val_record=[]
    for doc in docs:
        val_record.append(doc.to_dict())
    return val_record

def generate_chart():
    validation_data=get_reporting_data_for_chart()
    # Remove 'errors' key from each dictionary if present
    for val_data in validation_data:
        val_data.pop('errors', None)
    validation_data_mock = [
        {'total_issues': '1', 'user': 'Arij', 'validation_status': 'failed', 'file_name': 'arij_user_provided.bai2',
         'timestamp': '2025-09-17T20:30:44.596469', 'errors': 'USDD is not a valid currency code, in line 02'},
        {'total_issues': '1', 'user': 'Arjun', 'validation_status': 'Success', 'file_name': 'user_provided.bai2',
         'timestamp': '2025-09-17T20:30:44.596469', 'errors': 'USDD is not a valid currency code, in line 02'}]

    [{'total_issues': '4', 'user': 'finagent_x', 'validation_status': 'failed', 'file_name': 'file01',
      'timestamp': '2025-09-18T10:02:55.794298'}, {
         'bank_account_check': {'message': 'Bank account ID 032000000007  is valid in the target system',
                                'status': 'true'}, 'validation_result': 'FAILURE: The file is not a valid bai2 file.',
         'issues': [
             'Invalid 88 continuation record: The line `88,4000000,6,/` is a malformed and misplaced continuation record. It follows a complete `03` record and does not adhere to the defined format for continuation records.']},
     {'total_issues': 2, 'user': 'testclient1', 'validation_status': 'failed', 'file_name': 'file01',
      'timestamp': '2025-09-18T09:42:05.932688'},
     {'total_issues': '6', 'user': 'notification_agent', 'validation_status': 'failed', 'file_name': 'File',
      'timestamp': '2025-09-18T10:10:33.166079'},
     {'total_issues': '2', 'user': 'user', 'validation_status': 'failed', 'file_name': 'user_provided.bai2',
      'timestamp': '2025-09-17T20:30:44.596469'},
     {'total_issues': '2', 'user': 'sampath', 'validation_status': 'failed', 'file_name': 'sampath.bai2',
      'timestamp': '2025-09-17T20:30:44.596469'}]
    get_validation_pie_chart(validation_data)
    return {"status": "success", "message": "Chart generated successfully"}


def get_validation_pie_chart(validation_data):
    print("validation_data", validation_data)
    import matplotlib.pyplot as plt
    from datetime import date, timedelta
    from collections import Counter
    import io, base64
    yesterday = date.today() - timedelta(days=1)

    # Count validation statuses
    status_counts = Counter([item['validation_status'] for item in validation_data])
    labels = list(status_counts.keys())
    sizes = list(status_counts.values())

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title(f"Validation Status on {yesterday}")

    # Show chart
    plt.show()
    #buf = io.BytesIO()
    #plt.savefig(buf, format="png", bbox_inches="tight")
    #buf.seek(0)
    #md = f"![Validation status](data:image/png;base64,{b64})"
    #return {"text": md}
    return {"status": "success", "message": "Chart generated successfully"}
    return {
        "image": {
            "mime": "image/png",
            "base64": base64.b64encode(buf.read()).decode("utf-8"),
            "title": f"Validation status ({yesterday})"
        }
    }
