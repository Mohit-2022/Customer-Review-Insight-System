aspect_dict = {
    "Taste": ["taste", "flavor", "spicy", "salty", "sweet"],
    "Delivery": ["late", "delay", "delivery", "shipping"],
    "Packaging": ["package", "packaging", "box", "damaged"],
    "Price": ["price", "cost", "expensive", "cheap"],
    "Quality": ["quality", "broken", "poor"]
}

def detect_aspects(review):
    
    review = review.lower()
    detected = []
    
    for aspect, keywords in aspect_dict.items():
        for word in keywords:
            if word in review:
                detected.append(aspect)
                break
                
    return detected