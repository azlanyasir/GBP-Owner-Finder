
import math
import re

OWNER_PAT = re.compile(r"\b(owner|owner-operator|the owner|manager)\b", re.I)

def softmax(xs):
    m = max(xs) if xs else 0
    exps = [math.exp(x - m) for x in xs]
    s = sum(exps) or 1.0
    return [e / s for e in exps]

def score_candidates(person_contexts, reviews, business_name):
    cands = []
    for name, contexts in person_contexts.items():
        freq = len(contexts)

        owner_hits = sum(
            1 for c in contexts if OWNER_PAT.search(c) and name in c
        )

        reply_hits = sum(
            1 for r in reviews if r.get("owner_response") and name in r.get("owner_response")
        )

        first_person_hits = sum(
            1 for c in contexts if re.search(r"\b(I|we)\b.*\b" + re.escape(name) + r"\b", c, re.I)
        )

        same_as_business = 1 if name.lower() in business_name.lower() else 0

        score = (
            2.0 * owner_hits +
            1.5 * reply_hits +
            1.2 * same_as_business +
            1.0 * freq +
            0.5 * first_person_hits
        )

        cands.append({
            "name": name,
            "score": score,
            "owner_hits": owner_hits,
            "reply_hits": reply_hits,
            "freq": freq,
            "first_person_hits": first_person_hits,
            "evidence": contexts[:5]
        })

    probs = softmax([c["score"] for c in cands])
    for c, p in zip(cands, probs):
        c["probability"] = round(p, 4)

    cands.sort(key=lambda x: x["probability"], reverse=True)
    return cands
