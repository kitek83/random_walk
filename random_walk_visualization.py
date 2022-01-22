from random_walk import RandomWalk
import matplotlib.pyplot as plt

rw = RandomWalk(50_000)

while True:
    # initialize the walk to generate the data
    rw.fill_walk()
    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(16,9))
    color_range = range(rw.number_points)
    ax.scatter(rw.x_values,rw.y_values,c=color_range,cmap=plt.cm.Blues,s=1)
    #Emphasise the first and last point.
    ax.scatter(0,0,c='red',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='orange',s=100)

    ax.set_title(f'Random walk with {rw.number_points} points.',fontsize=24)
    ax.set_xlabel('x_values of the point.',fontsize=14)
    ax.set_ylabel('y_values of the point.',fontsize=14)

    plt.savefig(f'Random_walk_{rw.number_points}_points.pdf')
    plt.show()

    #controlling the loop
    keep_going = input('Do you want to make another random walk (y/n): ')
    if keep_going == 'n':
        break


