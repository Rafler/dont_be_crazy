import facebook
import requests
token = '2310354019198435|gSDVPyQZJCxmAuro9DQDt4K8INg'
graph = facebook.GraphAPI(access_token=token, version = 2.8)
events = graph.get_object('2055670317829617/events/')
print(events)