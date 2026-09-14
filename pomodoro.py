import time
import winsound


def notify(message):
    print(f"\n🔔 {message}")
    winsound.Beep(1000, 500)


def countdown(minutes, session):
    total_seconds = minutes * 60

    while total_seconds >= 0:
        mins = total_seconds // 60
        secs = total_seconds % 60

        print(
            f"\r🍅 {session} | ⏱️ {mins:02d}:{secs:02d}",
            end="",
            flush=True
        )

        if total_seconds == 0:
            break

        time.sleep(1)
        total_seconds -= 1

    print()


def main():
    print("=" * 40)
    print("       🍅 POMODORO TIMER")
    print("=" * 40)

    work_time = int(input("Enter work time (minutes): "))
    break_time = int(input("Enter break time (minutes): "))

    completed_sessions = 0

    while True:

        # Work session
        print("\n💻 Work session started!")
        countdown(work_time, "WORK")

        completed_sessions += 1
        notify("WORK SESSION COMPLETE!")
        print(f"✅ Completed work sessions: {completed_sessions}")

        # Break session
        print("\n☕ Break started!")
        countdown(break_time, "BREAK")

        notify("BREAK COMPLETE!")

        again = input("\nStart another work session? (y/n): ")

        if again.lower() != "y":
            break

    print("\n" + "=" * 40)
    print("🍅 POMODORO SESSION FINISHED")
    print(f"✅ Total completed work sessions: {completed_sessions}")
    print("=" * 40)


main()