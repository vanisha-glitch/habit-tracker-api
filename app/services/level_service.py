def get_level(score: float):

    if score >= 150:
        return "👑 Legendary"

    if score >= 100:
        return "🏆 Elite"

    if score >= 70:
        return "🥇 Gold"

    if score >= 40:
        return "🥈 Silver"

    if score >= 20:
        return "🥉 Bronze"

    return "🌱 Beginner"