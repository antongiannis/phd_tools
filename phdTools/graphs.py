import matplotlib.pyplot as plt


def donut_chart(labels, sizes, explosion=True, colors=None):
    """
    Creates a donut chart with explosion if selected.

    Parameters
    ----------
    labels: ndarray
        An array with the labels for the donut chart.
    sizes: ndarray
        An array with the counts for each category for the donut chart.
    explosion: bool, optional
        Whether or not to explode the chart.
    colors: list, optional
        A palette of HEX colours to be used. An example is ['#5e3c99', '#e66101', '#fdb863', '#b2abd2']

    Returns
    -------
    None

    """

    # Number of categories
    n_categ = len(labels)

    # explosion
    explosion_size = 0.05 * explosion
    explode = (explosion_size,) * n_categ

    fig1, ax1 = plt.subplots()
    patches, texts, autotexts = plt.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90,
                                        pctdistance=0.85, explode=explode)

    # draw circle
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    # Set colour to white inside
    for autotext in autotexts:
        autotext.set_color('white')

    # Change font size
    for text in texts:
        text.set_fontsize(10)

    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    plt.tight_layout()
