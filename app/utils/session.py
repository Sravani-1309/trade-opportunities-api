session_store = {}

def track_session(user):
    session_store[user] = session_store.get(user, 0) + 1
    return session_store[user]