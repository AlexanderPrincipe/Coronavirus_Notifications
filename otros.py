import plotly.graph_objects as go
from datetime import datetime

#ahora = datetime.now()
#fecha = ahora.strftime("%d-%m")

fig = go.Figure()

annotations = []

#Titulo
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.1,
                              xanchor='left', yanchor='bottom',
                              text='COVID-19: Indicadores (Perú)',
                              font=dict(family='Arial',
                                        size=30,
                                        color='rgb(37,37,37)'),
                              showarrow=False))
fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = LastCasosHosp,
    domain = {'x': [0, 0.9], 'y': [0.5, 0.9]},
    title = {"text": "Hospitalizados<br><span style='font-size:0.7em;color:gray'>Variación respecto al día anterior"},
    delta = {'reference': PLaSTCasosHosp, 'relative': True}))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = LastCasosUCI,
    domain = {'x': [0, 0.9], 'y': [0, 0.3]},
    title = {"text": "Casos en UCI<br><span style='font-size:0.7em;color:gray'>Variación respecto al día anterior"},
    delta = {'reference': PLastCasosUCI, 'relative': True}))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = LastCasosCN,
    delta = {'reference': PLastCasosCN, 'relative': True},
    title = {"text": "Casos Detectados<br><span style='font-size:0.7em;color:gray'>Variación respecto al día anterior"},
    domain = {'x': [0, 0.2], 'y': [0, 0.3]}))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = LastMRealiz,
    title = {"text": "Muestras Realizadas<br><span style='font-size:0.7em;color:gray'>Variación respecto al día anterior"},
    delta = {'reference': PLastMRealiz, 'relative': True},
    domain = {'x': [0, 0.2], 'y': [0.5, 0.9]}))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = LastRecuperados,
    title = {"text": "Recuperados<br><span style='font-size:0.7em;color:gray'>Variación respecto al día anterior"},
    delta = {'reference': PLastRecuperados, 'relative': True},
    domain = {'x': [0.6, 1], 'y': [0, 1]}))

fig.update_layout(annotations=annotations)

fig.show()