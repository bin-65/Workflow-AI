# utils/productivity.py

def calculate_time_saved(doc_count, query_count, action_count):
    """
    Calculates estimated minutes saved based on workplace activity.
    - 15 mins saved per document processed
    - 5 mins saved per Q&A answered
    - 10 mins saved per task extracted
    """
    saved_minutes = (doc_count * 15) + (query_count * 5) + (action_count * 10)
    return saved_minutes

def format_time_saved(minutes):
    """Formats total minutes into hours and minutes display string."""
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}h {mins}m" if hours > 0 else f"{mins} mins"
