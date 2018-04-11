import plotly.plotly as py
import plotly.graph_objs as go



data = [
    go.Scatterpolar(
      mode = "lines+markers",
      r = [1,2,3,4,5],
      theta = [0,90,180,360,0],
      line = dict(
        color = "#ff66ab"
      ),
      marker = dict(
        color = "#8090c7",
        symbol = "square",
        size = 8
      ),
      subplot = "polar",
    ),
    go.Scatterpolar(
      mode = "lines+markers",
      r = [1,2,3,4,5],
      theta = [0,90,180,360,0],
      line = dict(
        color = "#ff66ab"
      ),
      marker = dict(
        color = "#8090c7",
        symbol = "square",
        size = 8
      ),
      subplot = "polar2"
    )
  ]


layout = go.Layout(
    showlegend = False,
    polar = dict(
      domain = dict(
        x = [0,0.4],
        y = [0,1]
      ),
      sector = [150,210],
      radialaxis = dict(
        tickfont = dict(
          size = 8
        )
      ),
      angularaxis = dict(
        tickfont = dict(
          size = 8
        )
      )
    ),
    polar2 = dict(
      domain = dict(
        x = [0.6,1],
        y = [0,1]
      ),
      radialaxis = dict(
        tickfont = dict(
          size = 8
        )
      ),
      angularaxis = dict(
        tickfont = dict(
          size = 8
        )
      )
    )
)


fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='polar/sector')