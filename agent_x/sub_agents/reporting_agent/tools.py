from agent_x.sub_agents.validator_agent.tools import connect_to_db


def get_reporting_data():
    collection_ref = connect_to_db()
    docs = collection_ref.stream()
    records = [doc.to_dict() for doc in docs]
    print("Record:", records)
    return {"status": "success", "data": records}
