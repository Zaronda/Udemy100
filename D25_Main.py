import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("D25_50_states.csv")
all_states = data.state.to_list()
guesssed_states = []


#to get coordinates for each state 
#def get_mouse_click_coor(x, y):
#    print(x, y)

#turtle.onscreenclick(get_mouse_click_coor)
# user input state name
while len(guesssed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guesssed_states)}/50 States correct", prompt= "What's another state name?").title

# is answer in list of states
    if answer_state in all_states:
        guesssed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
#    t.write(state_data.state)
        t.write(answer_state)
#    t.write(state_data.state.item())





#turtle.mainloop()




# replaced by turtle.mainloop()
screen.exitonclick()