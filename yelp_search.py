from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import yelp_access
#Authenticate our yelp keys
#with io.open('yelp_config.json') as cred:
#        creds = json.load(cred)
#        auth = Oauth1Authenticator(**creds)
#        client = Client(auth)

#TEMPORARY - Allows developer access to yelp api
auth = yelp_access.access()
client = Client(auth)
f1 = open("yelp_results.txt", 'w')
f2 = open("yelp_ids.txt", 'w')


#We can now use client to search parameters
#optional paramaters:
#Term: is the search term, if this is not included if searches everything, it also accepts buisness names
#limit: is the  number of buisness results to return
#offset: offsets teh list of returned buisnesses by the amount specified here
#sort: sorts by a number, 0 is best matches, 1 is distance, and 2 is highest rated
#category_filler filter search results with a category, all categories supported can be found here https://www.yelp.com/developers/documentation/v2/all_category_list
try:
    term = input("Enter a term to search: ")
except term.empty():
    term = "none"
try:
    limit = input("Enter the limit of results: ")
except limit == 0:
    limit = 20
    
area = input("Enter the neighbhood, address,city, zip, state or country location you would like to search in: ")
 
    
print()
params = {
    'term': term,
    'lang': 'fr',
    'offset': 0,
    'limit': limit
}

#Client Search Function:
#Can be used to search by location which can by specified by neighborhood, address or city.
#Can be used to search by a bounding box, which takes a southwest and a northwest lat/long for values
#Can be used to search also by geographic coordinates, which requires a lat/long
    #Optional parameters are accuracy, altitude, and altitude_accuracy

#Documentation can be found at https://www.yelp.com/developers/documentation/v2/search_api


r = client.search(area, **params)


for i in range(len(r.businesses)):
    print("[Name: " + r.businesses[i].name + "] [Number of reviews : " + str(r.businesses[i].review_count) + "] [Categories: ", r.businesses[i].categories,"]", file = f1 )
    print(r.businesses[i].id, file=f2)
    id1 = r.businesses[i].id
    b = client.get_business(id1)
    print(b.business.location.coordinate.longitude)
    print(b.business.location.coordinate.latitude)
def ids():
    #Create an empty list we will use to append a list of ids
    l = []
    for i in range(len(response.businesses)):
                   l.append(response.businesses[i].id)
    return l
                   
