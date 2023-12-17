#The group is of Arnav Gupta 2022100,Kartikeya Chikkara 2022242,Jessica Kaur Chawla 2022230
import requests

inp=input("What TV Show are you looking for?")
api_base="https://api.themoviedb.org/3/"
api_key='22fe8280bf985ff7ca0df84a04e28920'
access_token='eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMmZlODI4MGJmOTg1ZmY3Y2EwZGY4NGEwNGUyODkyMCIsInN1YiI6IjYzYzk3MWRkN2E5N2FiMDBiNjcxYzBkNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Vp07EA09dGm80fbk6DjHLYFBYE-8MM9pbSsY_NrnRNc'
#resp=requests.get(f"{api_base}search/tv?api_key={api_key}&include_adult=true", header={"Content-Type: application/json;charset=utf-8,Authorization: Bearer <<access_token>>"})

resp=requests.get(f"{api_base}search/tv?api_key={api_key}&include_adult=true&query={inp}")


dic=resp.json()

for i in range(5):
    print(f'{i+1} {dic["results"][i]["name"]}')

choice=list(map(int, input("Enter Your Choices from the Search Result: ").split()))

def getNames(dic,x):
    lis=[]
    for j in dic[x]:
        lis.append(j['name'])
    return lis


for i in choice:
    resp=requests.get(f"{api_base}/tv/{dic['results'][i]['id']}?api_key={api_key}")
    print(f"Name: {dic['results'][i-1]['name']}")
    dic_new=resp.json()
    print(f"Genres: {getNames(dic_new,'genres')}")
    print(f"Created By: {getNames(dic_new,'created_by')}")
    print(f"First Air Date: {dic_new['first_air_date']}")
    print(f"Number of Seasons: {dic_new['number_of_seasons']}")
    print(f"Number of Seasons: {dic_new['number_of_episodes']}")

