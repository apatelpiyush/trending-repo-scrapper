import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt

"""Get the permission of the git-trending-page, then parse its HTML code and store in the result."""
def permit(link):
    response=requests.get(link)
    if response:
        print("Website Permission Granted.")
    else:
        print("Webiste Access Error.")
        return False

    soup=bs(response.content,'html.parser')
    if soup:
        print("Data scrapped successfully.")
    else:
        print("Daat scrapping failed.")
        return False

    result=soup.find_all('article', class_='Box-row')
    if result:
        print("Data extracted.")
        return result
    else:
        print("Data extraction failed.")
        return

"""Finding, Spliting up and Categorize the data."""
def data(result):
    user_repo=[]
    for i in range (len(result)):
        repo=result[i].h2.find('a').get_text(strip=True).split('/')[1]

        ln=result[i].find('span', itemprop="programmingLanguage")
        lang=ln.get_text(strip=True) if ln else " "

        star=result[i].find('a', href=lambda href: href and href.endswith('/stargazers'))
        star_count=star.get_text(strip=True) if star else "0"

        des=result[i].find('p')
        descp=des.get_text(strip=True) if des else " "
        user_repo.append({
            "Repo Name":repo,
            "Language": lang,
            "Stars":star_count,
            "Description":descp
        })
    return user_repo

"""Save the data as a dataframe and then form the required graphs and save them."""
def disp_graph(user_repo):
    final_data=pd.DataFrame(user_repo)

    # Numerising the the stars value from string to number.
    final_data["Stars"]=final_data['Stars'].str.replace(",","")
    final_data['Stars']=pd.to_numeric(final_data['Stars'],errors='coerce')
    final_data.to_csv("Assignment.csv")

    # Replacing the empty strings like Repo Name, desc, lang with standard notation.
    final_data["Repo Name"]=final_data["Repo Name"].replace(" ",'Unknown')
    final_data["Description"]=final_data["Description"].replace(" ",'Unknown')
    final_data["Language"]=final_data["Language"].replace(" ",'Unknown')
    final_data=final_data.drop_duplicates(subset=["Repo Name"])

    # Finding and printing the statistical information like mean, median and mode.
    print('Mean',final_data['Stars'].mean())
    print('Median',final_data['Stars'].median())
    print('Mode',final_data['Stars'].mode())

    # Graph of Progamming languages vs its distribution.
    final_data['Language'].value_counts().plot(kind='bar',align='center', color='skyblue', edgecolor='black')
    plt.xlabel("Programming Language")
    plt.ylabel("Number of Repos")
    plt.title("Distribution of Trending Repos by Language.")
    plt.savefig("Graph1.png")
    
    # Graph of Languages vs stars.
    graph=final_data.groupby('Language')['Stars'].sum()
    graph.plot(kind='bar',align='center', color='orange', edgecolor='black')
    plt.xlabel("Language.")
    plt.ylabel("Stars.")
    plt.title("Visuals Of Stars Vs Language.")
    plt.savefig("Graph2.png")


if __name__=="__main__":
    link="https://github.com/trending"
    result=permit(link)
    repo=data(result)
    disp_graph(repo)