# -*- coding: utf-8 -*-
"""
@author: HZU
"""
import streamlit as st


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default='browser'


st.set_page_config(layout="wide")

st.title('Interesting buildings of Belgium')
st.write('\n')
st.write('\n')
st.write('\n')
col1, col_mid, col2 = st.beta_columns((1, 0.1, 1))
with col1:
    st.subheader('This app basically works with the DSM and DTM files that are provided by GeoPunt.be.')
    st.write('\n') 
    st.write('More information can be found in the link below:')
    st.write('[https://www.geopunt.be/catalogus/datasetfolder/2caeb91f-df64-47c5-828d-cb1f0db3a41c](https://www.geopunt.be/catalogus/datasetfolder/2caeb91f-df64-47c5-828d-cb1f0db3a41c)')    
    st.write('\n') 
    st.write(f'<iframe \
             width="700" \
             height="600"\
             src="https://www.geopunt.be/catalogus/datasetfolder/2caeb91f-df64-47c5-828d-cb1f0db3a41c"></iframe>',
             unsafe_allow_html=True )     

with col2:
    st.write('Those files are images that exist of points that were gathered by LIDAR. \
            Simply put: a plane flew over the area and calculated the geographical \
            surface and the shapes and height of structures by measuring the back scattering light from a laser. \
            By using the shapefiles, the Lambert-72 coördinates provided in the TIFFs \
            and an API access to the map provided by the Flemish government, \
            the program calculates the exact position and three-dimensional shape of the building selected.')
    st.write('\n')       
    st.write('The libraries [rioxarray](https://corteva.github.io/rioxarray/stable/) and \
             [xarray](http://xarray.pydata.org/en/stable/) were used to manipulate the TIFFs. \
             Requests gets us the info through the API, that is then interpreted with json. \
             Shapely.geometry and shapely.ops create and join the seperate polygons, \
             that are then plotted using plotly.graph_objects and plotly.express.')
    st.write('\n')       
    st.write('\n')    
    st.subheader('To visualize different buildings in Belgium, you need to choose the city and the building.')
    st.subheader('A 3d plot of the selected building will be shown with the height above sea level addition to the information on the web \
                for the building.')

st.markdown("""---""")

city_type = st.selectbox('Please select a city:',
                                  ('None','Brussels', 'Antwerp', 'Gent', 'Bruges'))     

if city_type == 'None':
    st.write('Please select a valid city')

elif city_type == 'Brussels':
    building_bru = st.selectbox('Please select a Building:',
                             ('Grand Place','European Parliament', 'Law Courts of Brussels', 'National Basilica of the Sacred Heart'))     
    
    if building_bru == 'Grand Place':
        col1, col_mid, col2 = st.beta_columns((1, 0.1, 1))
        with col1:
            st.subheader('The graph is dynamic, you can zoom-in, zoom-out or rotate.')
            address = 'Grand Place, Grand Place 1, 1000 Brussels'
            
            X = np.load('./buildings_brussels/surface_Grand_Place_Brussels.npy')    
            N = len(X[:,0])
            M = len(X[0,:])  
            clipped_df = pd.DataFrame(X)
            fig = go.Figure(data=[go.Surface(z=clipped_df)])
            fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                              highlightcolor="limegreen", project_z=True))
            fig.update_layout(title=address, autosize=True,
                              scene_camera_eye=dict(x=0.8, y=0.8, z=0.5),                      
                              width=960, height=720,
                              margin=dict(l=65, r=50, b=65, t=90),
                               scene = {
                               "aspectratio": {"x": (N/N), "y": (N/M), "z": np.max(X)/M}
                               }
            )
            st.plotly_chart(fig, use_container_width=True)  

        with col2:
            st.write('[https://en.wikipedia.org/wiki/Brussels_Town_Hall](https://en.wikipedia.org/wiki/Brussels_Town_Hall)')
            st.write(f'<iframe \
                     width="700" \
                     height="600"\
                     src="https://en.wikipedia.org/wiki/Brussels_Town_Hall"></iframe>',
                     unsafe_allow_html=True )            

    elif building_bru == 'European Parliament':
        col1, col_mid, col2 = st.beta_columns((1, 0.1, 1))
        with col1:
            st.subheader('The graph is dynamic, you can zoom-in, zoom-out or rotate.')
            address = 'European Parliament, Rue Wiertz 60, 1047 Bruxelles'
            
            X = np.load('./buildings_brussels/surface_European Parliament.npy')    
            N = len(X[:,0])
            M = len(X[0,:])  
            clipped_df = pd.DataFrame(X)
            fig = go.Figure(data=[go.Surface(z=clipped_df)])
            fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                              highlightcolor="limegreen", project_z=True))
            fig.update_layout(title=address, autosize=True,
                              scene_camera_eye=dict(x=0.8, y=0.8, z=0.5),                      
                              width=960, height=720,
                              margin=dict(l=65, r=50, b=65, t=90),
                               scene = {
                               "aspectratio": {"x": (N/N), "y": (N/M), "z": np.max(X)/M}
                               }
            )
            st.plotly_chart(fig, use_container_width=True)  

        with col2:
            st.write('[https://en.wikipedia.org/wiki/Brussels_Parliament_building](https://en.wikipedia.org/wiki/Brussels_Parliament_building)')
            st.write(f'<iframe \
                     width="700" \
                     height="600"\
                     src="https://en.wikipedia.org/wiki/Brussels_Parliament_building"></iframe>',
                     unsafe_allow_html=True )      

    elif building_bru == 'Law Courts of Brussels':
        col1, col_mid, col2 = st.beta_columns((1, 0.1, 1))
        with col1:
            st.subheader('The graph is dynamic, you can zoom-in, zoom-out or rotate.')
            address = 'Law Courts of Brussels, Poelaert 1, 1000 Brussels '
            
            X = np.load('./buildings_brussels/surface_Palace_of_Justice_of_Brussels.npy')    
            N = len(X[:,0])
            M = len(X[0,:])  
            clipped_df = pd.DataFrame(X)
            fig = go.Figure(data=[go.Surface(z=clipped_df)])
            fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                              highlightcolor="limegreen", project_z=True))
            fig.update_layout(title=address, autosize=True,
                              scene_camera_eye=dict(x=0.8, y=0.8, z=0.5),                      
                              width=960, height=720,
                              margin=dict(l=65, r=50, b=65, t=90),
                               scene = {
                               "aspectratio": {"x": (N/N), "y": (N/M), "z": np.max(X)/M}
                               }
            )
            st.plotly_chart(fig, use_container_width=True)  

        with col2:
            st.write('[https://en.wikipedia.org/wiki/Palais_de_Justice,_Brussels](https://en.wikipedia.org/wiki/Palais_de_Justice,_Brussels)')
            st.write(f'<iframe \
                     width="700" \
                     height="600"\
                     src="https://en.wikipedia.org/wiki/Palais_de_Justice,_Brussels"></iframe>',
                     unsafe_allow_html=True )      

    elif building_bru == 'National Basilica of the Sacred Heart':
        col1, col_mid, col2 = st.beta_columns((1, 0.1, 1))
        with col1:
            st.subheader('The graph is dynamic, you can zoom-in, zoom-out or rotate.')
            address = 'National Basilica of the Sacred Heart, R20 5, 1083 Ganshoren'
            
            X = np.load('./buildings_brussels/surface_National_Basilica_Koekelberg.npy')    
            N = len(X[:,0])
            M = len(X[0,:])  
            clipped_df = pd.DataFrame(X)
            fig = go.Figure(data=[go.Surface(z=clipped_df)])
            fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                              highlightcolor="limegreen", project_z=True))
            fig.update_layout(title=address, autosize=True,
                              scene_camera_eye=dict(x=0.8, y=0.8, z=0.5),                      
                              width=960, height=720,
                              margin=dict(l=65, r=50, b=65, t=90),
                               scene = {
                               "aspectratio": {"x": (N/N), "y": (N/M), "z": np.max(X)/M}
                               }
            )
            st.plotly_chart(fig, use_container_width=True)  

        with col2:
            st.write('[https://en.wikipedia.org/wiki/Basilica_of_the_Sacred_Heart,_Brussels](https://en.wikipedia.org/wiki/Basilica_of_the_Sacred_Heart,_Brussels)')
            st.write(f'<iframe \
                     width="700" \
                     height="600"\
                     src="https://en.wikipedia.org/wiki/Basilica_of_the_Sacred_Heart,_Brussels"></iframe>',
                     unsafe_allow_html=True ) 

elif city_type == 'Antwerp':
    building_ant = st.selectbox('Please select a Building:',
                             ('Stadhuis van Antwerpen', 'Antwerpen Central', 'Cathedral of Our Lady Antwerp', 'Boerentoren'))     
    
    if building_ant == 'Stadhuis van Antwerpen':
        col1, col_mid, col2 = st.beta_columns((1, 0.1, 1))
        with col1:
            st.subheader('The graph is dynamic, you can zoom-in, zoom-out or rotate.')
            address = 'Stadhuis_van_Antwerpen, Grote Markt 1 2000 Antwerpen'
            
            X = np.load('./buildings_antwerp/surface_Stadhuis_van_Antwerpen.npy')    
            N = len(X[:,0])
            M = len(X[0,:])  
            clipped_df = pd.DataFrame(X)
            fig = go.Figure(data=[go.Surface(z=clipped_df)])
            fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                              highlightcolor="limegreen", project_z=True))
            fig.update_layout(title=address, autosize=True,
                              scene_camera_eye=dict(x=0.8, y=0.8, z=0.5),                      
                              width=960, height=720,
                              margin=dict(l=65, r=50, b=65, t=90),
                               scene = {
                               "aspectratio": {"x": (N/N), "y": (N/M), "z": np.max(X)/M}
                               }
            )
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.write('[https://en.wikipedia.org/wiki/Antwerp_City_Hall](https://en.wikipedia.org/wiki/Antwerp_City_Hall)')
            st.write(f'<iframe \
                     width="700" \
                     height="600"\
                     src="https://en.wikipedia.org/wiki/Antwerp_City_Hall"></iframe>',
                     unsafe_allow_html=True )

    elif building_ant == 'Antwerpen Central':
        col1, col_mid, col2 = st.beta_columns((1, 0.1, 1))
        with col1:
            st.subheader('The graph is dynamic, you can zoom-in, zoom-out or rotate.')
            address = 'Antwerpen Central, Koningin Astridplein 27 2018 Antwerpen'
            
            X = np.load('./buildings_antwerp/surface_Antwerpen_Central.npy')    
            N = len(X[:,0])
            M = len(X[0,:])  
            clipped_df = pd.DataFrame(X)
            fig = go.Figure(data=[go.Surface(z=clipped_df)])
            fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                              highlightcolor="limegreen", project_z=True))
            fig.update_layout(title=address, autosize=True,
                              scene_camera_eye=dict(x=0.8, y=0.8, z=0.5),                      
                              width=960, height=720,
                              margin=dict(l=65, r=50, b=65, t=90),
                               scene = {
                               "aspectratio": {"x": (N/N), "y": (N/M), "z": np.max(X)/M}
                               }
            )
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.write('[https://en.wikipedia.org/wiki/Antwerpen-Centraal_railway_station](https://en.wikipedia.org/wiki/Antwerpen-Centraal_railway_station)')
            st.write(f'<iframe \
                     width="700" \
                     height="600"\
                     src="https://en.wikipedia.org/wiki/Antwerpen-Centraal_railway_station"></iframe>',
                     unsafe_allow_html=True )                  

    elif building_ant == 'Cathedral of Our Lady Antwerp':
        col1, col_mid, col2 = st.beta_columns((1, 0.1, 1))
        with col1:
            st.subheader('The graph is dynamic, you can zoom-in, zoom-out or rotate.')
            address = 'Cathedral of Our Lady Antwerp, Groenplaats 21 2000 Antwerpen'
            
            X = np.load('./buildings_antwerp/surface_Cathedral_of_Our_Lady_Antwerp.npy')    
            N = len(X[:,0])
            M = len(X[0,:])  
            clipped_df = pd.DataFrame(X)
            fig = go.Figure(data=[go.Surface(z=clipped_df)])
            fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                              highlightcolor="limegreen", project_z=True))
            fig.update_layout(title=address, autosize=True,
                              scene_camera_eye=dict(x=0.8, y=0.8, z=0.5),                      
                              width=960, height=720,
                              margin=dict(l=65, r=50, b=65, t=90),
                               scene = {
                               "aspectratio": {"x": (N/N), "y": (N/M), "z": np.max(X)/M}
                               }
            )
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.write('[https://en.wikipedia.org/wiki/Cathedral_of_Our_Lady_(Antwerp)](https://en.wikipedia.org/wiki/Cathedral_of_Our_Lady_(Antwerp))')
            st.write(f'<iframe \
                     width="700" \
                     height="600"\
                     src="https://en.wikipedia.org/wiki/Cathedral_of_Our_Lady_(Antwerp)"></iframe>',
                     unsafe_allow_html=True )   

    elif building_ant == 'Boerentoren':
        col1, col_mid, col2 = st.beta_columns((1, 0.1, 1))
        with col1:
            st.subheader('The graph is dynamic, you can zoom-in, zoom-out or rotate.')
            address = 'Boerentoren, Boerentoren 2000 Antwerpen'
            
            X = np.load('./buildings_antwerp/surface_Boerentoren.npy')    
            N = len(X[:,0])
            M = len(X[0,:])  
            clipped_df = pd.DataFrame(X)
            fig = go.Figure(data=[go.Surface(z=clipped_df)])
            fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                              highlightcolor="limegreen", project_z=True))
            fig.update_layout(title=address, autosize=True,
                              scene_camera_eye=dict(x=0.8, y=0.8, z=0.5),                      
                              width=960, height=720,
                              margin=dict(l=65, r=50, b=65, t=90),
                               scene = {
                               "aspectratio": {"x": (N/N), "y": (N/M), "z": np.max(X)/M}
                               }
            )
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.write('[https://en.wikipedia.org/wiki/Boerentoren](https://en.wikipedia.org/wiki/Boerentoren)')
            st.write(f'<iframe \
                     width="700" \
                     height="600"\
                     src="https://en.wikipedia.org/wiki/Boerentoren"></iframe>',
                     unsafe_allow_html=True )  

elif city_type == 'Gent':
    building_ant = st.selectbox('Please select a Building:',
                             ('Saint Bavos Cathedral', 'Gravensteen', 'Saint Nicholas Church', 'Sint Pietersabdij'))     
    
    if building_ant == 'Saint Bavos Cathedral':
        col1, col_mid, col2 = st.beta_columns((1, 0.1, 1))
        with col1:
            st.subheader('The graph is dynamic, you can zoom-in, zoom-out or rotate.')
            address = 'Saint Bavos Cathedral, Saint Bavo Cathedral 9000 Gent'
            
            X = np.load('./buildings_gent/surface_Saint_Bavos_Cathedral.npy')    
            N = len(X[:,0])
            M = len(X[0,:])  
            clipped_df = pd.DataFrame(X)
            fig = go.Figure(data=[go.Surface(z=clipped_df)])
            fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                              highlightcolor="limegreen", project_z=True))
            fig.update_layout(title=address, autosize=True,
                              scene_camera_eye=dict(x=0.8, y=0.8, z=0.5),                      
                              width=960, height=720,
                              margin=dict(l=65, r=50, b=65, t=90),
                               scene = {
                               "aspectratio": {"x": (N/N), "y": (N/M), "z": np.max(X)/M}
                               }
            )
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.write('[https://en.wikipedia.org/wiki/St_Bavo%27s_Cathedral,_Ghent](https://en.wikipedia.org/wiki/St_Bavo%27s_Cathedral,_Ghent)')
            st.write(f'<iframe \
                     width="700" \
                     height="600"\
                     src="https://en.wikipedia.org/wiki/St_Bavo%27s_Cathedral,_Ghent"></iframe>',
                     unsafe_allow_html=True )

    elif building_ant == 'Gravensteen':
        col1, col_mid, col2 = st.beta_columns((1, 0.1, 1))
        with col1:
            st.subheader('The graph is dynamic, you can zoom-in, zoom-out or rotate.')
            address = 'Gravensteen, Sint-Veerleplein 11 9000 Gent'
            
            X = np.load('./buildings_gent/surface_Gravensteen.npy')    
            N = len(X[:,0])
            M = len(X[0,:])  
            clipped_df = pd.DataFrame(X)
            fig = go.Figure(data=[go.Surface(z=clipped_df)])
            fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                              highlightcolor="limegreen", project_z=True))
            fig.update_layout(title=address, autosize=True,
                              scene_camera_eye=dict(x=0.8, y=0.8, z=0.5),                      
                              width=960, height=720,
                              margin=dict(l=65, r=50, b=65, t=90),
                               scene = {
                               "aspectratio": {"x": (N/N), "y": (N/M), "z": np.max(X)/M}
                               }
            )
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.write('[https://en.wikipedia.org/wiki/Gravensteen](https://en.wikipedia.org/wiki/Gravensteen)')
            st.write(f'<iframe \
                     width="700" \
                     height="600"\
                     src="https://en.wikipedia.org/wiki/Gravensteen"></iframe>',
                     unsafe_allow_html=True )

    elif building_ant == 'Saint Nicholas Church':
        col1, col_mid, col2 = st.beta_columns((1, 0.1, 1))
        with col1:
            st.subheader('The graph is dynamic, you can zoom-in, zoom-out or rotate.')
            address = 'Saint Nicholas Church, Cataloniëstraat 9000 Gent'
            
            X = np.load('./buildings_gent/surface_Saint_Nicholas_Church.npy')    
            N = len(X[:,0])
            M = len(X[0,:])  
            clipped_df = pd.DataFrame(X)
            fig = go.Figure(data=[go.Surface(z=clipped_df)])
            fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                              highlightcolor="limegreen", project_z=True))
            fig.update_layout(title=address, autosize=True,
                              scene_camera_eye=dict(x=0.8, y=0.8, z=0.5),                      
                              width=960, height=720,
                              margin=dict(l=65, r=50, b=65, t=90),
                               scene = {
                               "aspectratio": {"x": (N/N), "y": (N/M), "z": np.max(X)/M}
                               }
            )
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.write('[https://en.wikipedia.org/wiki/Saint_Nicholas_Church,_Ghent](https://en.wikipedia.org/wiki/Saint_Nicholas_Church,_Ghent)')
            st.write(f'<iframe \
                     width="700" \
                     height="600"\
                     src="https://en.wikipedia.org/wiki/Saint_Nicholas_Church,_Ghent"></iframe>',
                     unsafe_allow_html=True )

    elif building_ant == 'Sint Pietersabdij':
        col1, col_mid, col2 = st.beta_columns((1, 0.1, 1))
        with col1:
            st.subheader('The graph is dynamic, you can zoom-in, zoom-out or rotate.')
            address = 'Sint Pietersabdij, Tweekerkenstraat 2 9000 Gent'
            
            X = np.load('./buildings_gent/surface_Sint_Pietersabdij.npy')    
            N = len(X[:,0])
            M = len(X[0,:])  
            clipped_df = pd.DataFrame(X)
            fig = go.Figure(data=[go.Surface(z=clipped_df)])
            fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                              highlightcolor="limegreen", project_z=True))
            fig.update_layout(title=address, autosize=True,
                              scene_camera_eye=dict(x=0.8, y=0.8, z=0.5),                      
                              width=960, height=720,
                              margin=dict(l=65, r=50, b=65, t=90),
                               scene = {
                               "aspectratio": {"x": (N/N), "y": (N/M), "z": np.max(X)/M}
                               }
            )
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.write('[https://en.wikipedia.org/wiki/Saint_Peter%27s_Abbey,_Ghent](https://en.wikipedia.org/wiki/Saint_Peter%27s_Abbey,_Ghent)')
            st.write(f'<iframe \
                     width="700" \
                     height="600"\
                     src="https://en.wikipedia.org/wiki/Saint_Peter%27s_Abbey,_Ghent"></iframe>',
                     unsafe_allow_html=True )


elif city_type == 'Bruges':
    building_ant = st.selectbox('Please select a Building:',
                             ('Belfry of Bruges', 'Church of our Lady Bruges'))    

    if building_ant == 'Belfry of Bruges':
        col1, col_mid, col2 = st.beta_columns((1, 0.1, 1))
        with col1:
            st.subheader('The graph is dynamic, you can zoom-in, zoom-out or rotate.')
            address = 'Belfry_of_Bruges, Markt 7 8000 Brugge'
            
            X = np.load('./buildings_bruges/surface_Belfry_of_Bruges.npy')    
            N = len(X[:,0])
            M = len(X[0,:])  
            clipped_df = pd.DataFrame(X)
            fig = go.Figure(data=[go.Surface(z=clipped_df)])
            fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                              highlightcolor="limegreen", project_z=True))
            fig.update_layout(title=address, autosize=True,
                              scene_camera_eye=dict(x=0.8, y=0.8, z=0.5),                      
                              width=960, height=720,
                              margin=dict(l=65, r=50, b=65, t=90),
                               scene = {
                               "aspectratio": {"x": (N/N), "y": (N/M), "z": np.max(X)/M}
                               }
            )
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.write('[https://en.wikipedia.org/wiki/Belfry_of_Bruges](https://en.wikipedia.org/wiki/Belfry_of_Bruges)')
            st.write(f'<iframe \
                     width="700" \
                     height="600"\
                     src="https://en.wikipedia.org/wiki/Belfry_of_Bruges"></iframe>',
                     unsafe_allow_html=True )

    elif building_ant == 'Church of our Lady Bruges':
        col1, col_mid, col2 = st.beta_columns((1, 0.1, 1))
        with col1:
            st.subheader('The graph is dynamic, you can zoom-in, zoom-out or rotate.')
            address = 'Church of our Lady Bruges, Mariastraat 8000 Brugge'
            
            X = np.load('./buildings_bruges/surface_Church_of_our_Lady_Bruges.npy')    
            N = len(X[:,0])
            M = len(X[0,:])  
            clipped_df = pd.DataFrame(X)
            fig = go.Figure(data=[go.Surface(z=clipped_df)])
            fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                              highlightcolor="limegreen", project_z=True))
            fig.update_layout(title=address, autosize=True,
                              scene_camera_eye=dict(x=0.8, y=0.8, z=0.5),                      
                              width=960, height=720,
                              margin=dict(l=65, r=50, b=65, t=90),
                               scene = {
                               "aspectratio": {"x": (N/N), "y": (N/M), "z": np.max(X)/M}
                               }
            )
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.write('[https://en.wikipedia.org/wiki/Church_of_Our_Lady,_Bruges](https://en.wikipedia.org/wiki/Church_of_Our_Lady,_Bruges)')
            st.write(f'<iframe \
                     width="700" \
                     height="600"\
                     src="https://en.wikipedia.org/wiki/Church_of_Our_Lady,_Bruges"></iframe>',
                     unsafe_allow_html=True )
