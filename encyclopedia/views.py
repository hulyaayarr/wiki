from django.shortcuts import render
from . import util
import random
from django.shortcuts import redirect
from .util import get_entry, list_entries, save_entry
import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_title(request, title):
    get_content = get_entry(title)
    if get_content is None:
        return render(request, "encyclopedia/entry_error.html", {
            "message" : "No such entry."
        })
    else:
        html_content = markdown2.markdown(get_content)
        return render(request, "encyclopedia/entry_title.html", {
            "title": title , "content": html_content
        })
        
def searching(request):
    input = request.GET.get('q')
    findings = []
    if input:
        entries = list_entries()
        for entry in entries:
            if input.lower() in entry.lower():
                findings.append(entry)
    return render(request, "encyclopedia/searching.html", {
        "input": input, "findings": findings
        })

def new(request):
    if request.method == 'POST':
        
        title = request.POST.get('title')
        content = request.POST.get('content')
        exists=False
        entries = list_entries()
        for entry in entries:
            if get_entry(title):
                exists=True
            else:
                exists=False
        
        if exists:
            return render(request, "encyclopedia/new_error.html", {
            "new_message" : "Entry already exists."
        })

        else:
            save_entry(title,content)
            return render(request, "encyclopedia/entry_title.html", {
            "title": entry_title , "content": content
        })  
            
                                
    return render(request, "encyclopedia/new.html")

def edit(request, heading):
    old_content = markdown2.markdown(get_entry(heading))
    if request.method == 'POST':
        new_content = markdown2.markdown(request.POST.get('content_'))
        save_entry(heading, new_content)
        return render(request, "encyclopedia/entry_title.html", {
            "title": heading , "content": new_content
        })
    return render(request, "encyclopedia/edit.html", {
        "title": heading, "content": old_content
    })

def random_page(request):
    entries = list_entries()
    random_entry = random.choice(entries)
    random_content =markdown2.markdown(get_entry(random_entry))
    return render(request, "encyclopedia/entry_title.html", {
            "title": random_entry, "content": random_content
        })