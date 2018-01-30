## Our team created the winning predictive models at the Hack Austin event hosted by the City of Austin to answer the question: 
## How might we improve emergency response times within the city?

### A data-driven process for getting ahead of tragedy
### Team members:  Brandyn Adderly, Owen Temple, and Danielle Fenimore

## <a href="https://austinstrategicplan.bloomfire.com/posts/1496098-2-winners-announced-at-civic-hackathon">Winners Announced at Civic Hackathon</a>

<a href="https://austinstrategicplan.bloomfire.com/posts/1496098-2-winners-announced-at-civic-hackathon"><img src="Hack%20Austin%20Winning%20Team%20Photo.png" height=40%  width=40%  alt="Winning Team at Hack Austin"></a>

A late response by Austin Fire Department is defined as the first unit arriving on the scene of a fire 6 minutes or more after the original emergency phone call was received.

### Predictive Mapping
Our time series model used past call volume and response times to forecast call volume and response times in 2018 and 2019. Our model forecasted trends and seasonality in average response times for all Austin areas combined.
![Average Response Time Forecast.png](https://media.data.world/MT7nqc9Seu9gk8nO8OdA_Average%20Response%20Time%20Forecast.png)

We also used the time series model to take a closer look at 3 specific response areas and employed ArcGIS to build an animated interactive map that shows our predictions for these areas: downtown, the eastern crescent, and Goodnight Ranch.

Click [here]((https://www.arcgis.com/home/webmap/viewer.html?webmap=d60ad3e973a545ef8f2d895b8b34d8e4&extent=-97.794,30.1425,-97.6786,30.176)) to view the interactive map for 3 response areas:
[Where is the fire going to be?](https://www.arcgis.com/home/webmap/viewer.html?webmap=d60ad3e973a545ef8f2d895b8b34d8e4&extent=-97.794,30.1425,-97.6786,30.176)

![Austin Fire Department Response Times.png](https://media.data.world/6ljiSKrTSOi3WPnwubUk_Austin%20Fire%20Department%20Response%20Times.png)


## Key Features in Late Responses

Our random forest classifier model predicted late responses in some areas of the city  more than others. Perhaps we can use these insights to design very targeted interventions to reduce common causes of fires in these areas.

Our random forest classification model cited the following response areas as important features in predicting a late response:

#### Response Area /  Neighborhood Name
- 2703	/ Travis Country
- 3810	/ Town and Country Park Addition (north of MacNeil)
- 0402	/ Pemberton
- 4210	/ Moore's Crossing
- 2906	/ Akin, Oak Park Estates
- 3107	/ Emma Long Park
- 2702	/ Oak Hill
- 4108	/ Wildhorse
- 3602	/ Onion Creek

#### Problem Type
Within response areas that were associated with late responses in 2015 and 2016, these were the various problem types:

![Late Responses by Problem Type Since 2015 in Response Areas with Late Arrivals.png](https://media.data.world/rbDfbvFIRU22Bn4CjFHw_Late%20Responses%20by%20Problem%20Type%20Since%202015%20in%20Response%20Areas%20with%20Late%20Arrivals.png)

#### Day of the Week
Our random forest classification model also identified day of week (and particularly Monday) as a key feature for predicting a late response.

<img src="https://media.data.world/8z5kGEWsQkyCsxqTn44E_Late%20Responses%20by%20Day%20of%20Week%20in%20Response%20Areas%20with%20Late%20Arrivals.png" height=40%  width=40%>


By noting the surrounding circumstances of late responses, we can perhaps take steps to prevent these types of fires in the problem areas on the days of the week identified by the model. Instead of raising priorities of problems through tragedies, we can help raise priorities through good data analytics. 
