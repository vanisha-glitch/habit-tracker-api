def get_achievements(
    current_streak: int,
    longest_streak: int,
    success_rate: float
):

    achievements = []

    if current_streak >= 3:
        achievements.append("🌱 Getting Started")

    if current_streak >= 7:
        achievements.append("🔥 7-Day Streak")

    if current_streak >= 30:
        achievements.append("🏆 Consistency Master")

    if current_streak >= 100:
        achievements.append("👑 Unstoppable")

    if longest_streak >= 365:
        achievements.append("💎 Habit Legend")

    if success_rate >= 80:
        achievements.append("⭐ Highly Consistent")

    if success_rate >= 95:
        achievements.append("🚀 Perfectionist")

    return achievements