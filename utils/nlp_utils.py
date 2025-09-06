
def map_text_to_goal(text):
    text = text.lower()
    if "focus" in text:
        return "focus"
    elif "memory" in text:
        return "memory"
    elif "stress" in text or "calm" in text:
        return "anti-stress"
    else:
        return "focus"  # default
