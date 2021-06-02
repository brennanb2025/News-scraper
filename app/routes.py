import plotly.graph_objects as go
from flask import Flask, request, render_template, flash, redirect, url_for, session, make_response
from app import app
from app.mainAction import mainAction


@app.route('/', methods=['GET'])
def view():
    return render_template('page.html')

@app.route('/', methods=['POST'])
def viewPost():
    form1 = request.form
    
    typed1 = None
    typed2 = None
    source1 = None
    source2 = None
    keywords = form1.get('keywords')
    sources = []
    if form1.get('sources1') != "":
        sources.append(form1.get('sources1')) #get the sources from the html form
        source1 = form1.get('sources1')

    if form1.get('sources2') != "":
        sources.append(form1.get('sources2'))
        source2 = form1.get('sources2')

    if len(sources) == 0:
        flash("No sources chosen")
        return redirect('/') #begone
    
    if keywords == "":
        flash("No keywords entered")
        return redirect('/') #begone
    
    dictData = mainAction(keywords, sources)
    source1Dict = None
    source2Dict = None

    if source1 != None:
        typed1 = dictData[0]["type"] #articles or headlines
        source1Dict = dictData[0] #source 1 is something
    
    if source2 != None:
        if source1 == None: #user entered only the second source
            typed2 = dictData[0]["type"] #articles or headlines
            source2Dict = dictData[0] #source 2 is something and no source 1
        else:
            if source1 == source2: # the user put the same source for both
                typed2 = typed1
                source2Dict = source1Dict
            else:
                typed2 = dictData[1]["type"] #source 1 and source 2 are different, set them to dictData[0] and [1]
                source2Dict = dictData[1]
    
    keywordStr = ""
    keywords = keywords.split(", ")
    for keyword in keywords:
        keywordStr+=keyword + ", " #keywordstr to display on the website
    
    keywordStr = keywordStr[:len(keywordStr)-2]

    dataGraphDict1 = {}
    for i in list(source1Dict.keys()):
        if " " in i:
            dataGraphDict1[i] = source1Dict[i] #add source1 to dataGraph dictionary

    dataGraph = {}
    dataGraph["source1Name"] = source1
    dataGraph["labels1"] = list(dataGraphDict1.keys())
    dataGraph["source1Vals"] = list(dataGraphDict1.values()) #turn key/value dictionaries into separate lists and add to dict
    
    if source2 != None:
        dataGraphDict2 = {}
        for i in list(source2Dict.keys()):
            if " " in i:
                dataGraphDict2[i] = source2Dict[i] #add source2 to dict
        dataGraph["source2Vals"] = list(dataGraphDict2.values())
        dataGraph["source2Name"] = source2
        dataGraph["labels2"] = list(dataGraphDict2.keys())

    plotGraph(dataGraph, keywordStr) #plot graph with plotly
    
    return render_template('page.html', source1=source1, source2=source2, keywords=keywordStr, keywordArr=keywords,
            finishedReading=True, source1Dict=source1Dict, source2Dict=source2Dict, typed1=typed1, typed2=typed2)

def plotGraph(dataGraph, keywordStr):
    data = []
    bar1 = go.Bar(name=dataGraph["source1Name"], x=dataGraph["labels1"], y=dataGraph["source1Vals"]) #add bars if they exist
    data.append(bar1)
    if dataGraph.__contains__("source2Name"):
        bar2 = go.Bar(name=dataGraph["source2Name"], x=dataGraph["labels2"], y=dataGraph["source2Vals"])
        data.append(bar2)
    
    # Change the bar mode and set layout
    if dataGraph.__contains__("source2Name"):
        layout = go.Layout(barmode='group', title=("Polarity of " + dataGraph["source1Name"] + " vs " + dataGraph["source2Name"]), yaxis_title="%")
    else:
        layout = go.Layout(barmode='group', title=("Polarity of " + dataGraph["source1Name"]), yaxis_title="%")
    
    
    fig = go.Figure(data=data, layout=layout)
    fig.show() #open in new tab

if __name__ == '__main__':
    app.run()