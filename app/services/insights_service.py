def get_insights(current_streak, longest_streak, success_rate):

    insights = []

    if current_streak == 0:
        insights.append("Start today! Every streak begins with one day.")

    elif current_streak < 7:
        insights.append("You're building momentum. Keep going!")

    elif current_streak < 30:
        insights.append("Excellent consistency! You're forming a strong habit.")

    else:
        insights.append("Amazing dedication! Your habit has become a lifestyle.")

    if success_rate >= 90:
        insights.append("Your completion rate is outstanding.")

    elif success_rate >= 70:
        insights.append("You're doing well. A little more consistency will make a big difference.")

    else:
        insights.append("Try setting reminders to improve your consistency.")

    if longest_streak > current_streak:
        insights.append("Can you beat your personal best streak?")

    return insights