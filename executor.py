class Execute:
    def __init__(self):
        self.week = 0
        self.follower_growth = 0

    def run(self, state, plan):
        print("\nExecute Called\n")
        self.week += 1

        try:
            growth = int(input(f"Enter follower growth for week {self.week}: "))
        except ValueError:
            print("Invalid input, defaulting growth to 0")
            growth = 0

        self.follower_growth += growth

        state.week = self.week
        state.follower_growth = self.follower_growth

        results = (
            f"Follower growth this week: {growth}. "
            f"Total growth: {self.follower_growth}. "
            f"Weeks elapsed: {self.week}"
        )

        print(results)
        return results
