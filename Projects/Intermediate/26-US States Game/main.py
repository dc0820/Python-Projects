import turtle
import pandas

FONT = ("Arial", 8, "normal")

# ----- Screen Setup -----
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# ----- Load Data -----
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

# A reusable writer turtle
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.speed("fastest")

# ----- Main Game Loop -----
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    )

    # Handle cancel button
    if answer_state is None:
        continue

    answer_state = answer_state.strip().title()

    # Player exits:
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]

        # Save missing list
        pandas.DataFrame({"state": missing_states}).to_csv("states_to_learn.csv", index=False)

        # ---> Draw missing states in yellow
        for state in missing_states:
            state_data = data[data.state == state]
            writer.goto(state_data.x.item(), state_data.y.item())
            writer.color("orange")
            writer.write(state, font=FONT)
        break

    # Skip duplicates
    if answer_state in guessed_states:
        continue

    # Correct guess
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        writer.goto(state_data.x.item(), state_data.y.item())
        writer.color("green")
        writer.write(answer_state, font=FONT)

# Finish
screen.exitonclick()
