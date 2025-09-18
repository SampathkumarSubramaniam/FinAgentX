from agent_x.sub_agents.validator_agent.tools import connect_to_db
import matplotlib.pyplot as plt
from datetime import date, timedelta
from collections import Counter


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
    get_validation_pie_chart(validation_data)
    return {"status": "success", "message": "Chart generated successfully"}


def get_validation_pie_chart(validation_data):
    print("validation_data", validation_data)
    yesterday = date.today() - timedelta(days=1)

    # Count validation statuses
    status_counts = Counter([item['validation_status'] for item in validation_data])
    labels = list(status_counts.keys())
    sizes = list(status_counts.values())
    _, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title(f"Validation Status on {yesterday}")
    plt.show()
    return {"status": "success", "message": "Chart generated successfully"}

