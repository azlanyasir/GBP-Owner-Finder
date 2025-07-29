def score_candidates(person_contexts, reviews, business_name):
    results = []
    for person, contexts in person_contexts.items():
        score = sum(1 for context in contexts if business_name.lower() in context.lower())
        results.append({"name": person, "score": score})
    results.sort(key=lambda x: x["score"], reverse=True)
    return results