def execute(command: str) -> str:
    command = command.lower()

    try:
        if "plus" in command:
            nums = [int(s) for s in command.split() if s.isdigit()]
            return f"Result is {sum(nums)}"

        elif "minus" in command:
            nums = [int(s) for s in command.split() if s.isdigit()]
            return f"Result is {nums[0] - nums[1]}"

        elif "multiply" in command:
            nums = [int(s) for s in command.split() if s.isdigit()]
            return f"Result is {nums[0] * nums[1]}"

        elif "divide" in command:
            nums = [int(s) for s in command.split() if s.isdigit()]
            return f"Result is {nums[0] / nums[1]}"

        elif "calculate" in command:
            expr = command.replace("calculate", "").strip()
            return f"Result is {eval(expr)}"

    except Exception:
        return "Sorry, I couldn’t calculate that."

    return "Math command not recognized."
