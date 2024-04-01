import plotly.graph_objects as go

salaries = [
    ("Mark", 1000),
    ("John", 1500),
    ("Daniel", 2300),
    ("Greg", 5000)
]

names = [tup[0] for tup in salaries]
salary_values = [tup[1] for tup in salaries]

fig = go.Figure([go.Bar(x=names, y=salary_values)])

fig.update_layout(
    title='Salaries with Plotly',
    xaxis=dict(title='Employee'),
    yaxis=dict(title='Salary in zł')
)

fig.show()
