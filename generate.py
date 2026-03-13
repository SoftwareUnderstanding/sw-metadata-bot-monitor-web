import json
import pystache
import datetime
import os
import shutil
from datetime import timezone

def process_data(data):
    """Enhance raw JSON data for the template."""
    repos = []
    for repo in data:
        name = repo["repo_url"].rstrip("/").split("/")[-1]
        
        try:
            analysis_date = datetime.datetime.fromisoformat(repo["analysis_date"].replace("Z", "+00:00"))
            analysis_date_formatted = analysis_date.strftime("%b %d, %Y")
        except:
            analysis_date_formatted = repo["analysis_date"]

        has_issues = False
        has_pitfalls = False
        has_warnings = False
        
        if repo.get("pitfalls_ids"):
            has_issues = True
            has_pitfalls = True
            
        if repo.get("warnings_ids"):
            has_issues = True
            has_warnings = True

        repo_enhanced = repo.copy()
        repo_enhanced["repo_name"] = name
        repo_enhanced["analysis_date_formatted"] = analysis_date_formatted
        repo_enhanced["has_issues"] = has_issues
        repo_enhanced["has_pitfalls"] = has_pitfalls
        repo_enhanced["has_warnings"] = has_warnings
        
        repos.append(repo_enhanced)
    return repos

def get_history_links(history_dir="history"):
    """Scan history directory and return a sorted list of link dictionaries."""
    links = []
    if not os.path.exists(history_dir):
        return links
        
    for filename in os.listdir(history_dir):
        if filename.startswith("report_") and filename.endswith(".json"):
            date_str = filename[7:-5]
            try:
                dt = datetime.datetime.strptime(date_str, "%Y-%m-%d_%H-%M-%S")
                label = dt.strftime("%B %d, %Y at %H:%M")
            except:
                label = date_str
                
            html_filename = f"report_{date_str}.html"
            links.append({
                "url": f"history/{html_filename}",
                "label": label,
                "filename": html_filename,
                "date_str": date_str
            })
            
    links.sort(key=lambda x: x["date_str"], reverse=True)
    return links

def main():
    history_dir = "history"
    os.makedirs(history_dir, exist_ok=True)
    
    with open("created_issues_report.json", "r") as f:
        current_data = json.load(f)
        
    now_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archive_json_path = os.path.join(history_dir, f"report_{now_str}.json")
    
    # This is to check the current json content and only save if the exact same JSON content isn't the most recent archive
    # (It's to prevent spamming the history folder if run multiple times without data changes)
    should_archive = True
    existing_jsons = [f for f in os.listdir(history_dir) if f.endswith('.json')]
    if existing_jsons:
        existing_jsons.sort(reverse=True)
        latest_json = os.path.join(history_dir, existing_jsons[0])
        with open(latest_json, "r") as f:
            if json.load(f) == current_data:
                should_archive = False
                
    if should_archive:
        shutil.copy2("created_issues_report.json", archive_json_path)
        print(f"Archived current report to {archive_json_path}")
        
    all_links = get_history_links()
    
    with open("template.mustache", "r") as f:
        template = f.read()
        
    print("Regenerating historical HTMLs...")
    for link in all_links:
        json_path = os.path.join(history_dir, f"report_{link['date_str']}.json")
        if os.path.exists(json_path):
            with open(json_path, "r") as f:
                hist_data = json.load(f)
                
            hist_repos = process_data(hist_data)
            
            # Setup links for this specific historical page
            page_links = []
            for l in all_links:
                page_links.append({
                    "url": l["filename"], 
                    "label": l["label"],
                    "is_active": l["filename"] == link["filename"] 
                })
                
            template_data = {
                "date_stamp": link["label"],
                "total_repos": len(hist_repos),
                "repos": hist_repos,
                "history_links": page_links,
                "base_path": "../", 
                "is_current": False
            }
            
            html = pystache.render(template, template_data)
            with open(os.path.join(history_dir, link["filename"]), "w") as f:
                f.write(html)
                
    # To generate the current index.html
    current_repos = process_data(current_data)
    now_utc = datetime.datetime.now(timezone.utc)
    date_stamp = now_utc.strftime("%B %d, %Y at %H:%M UTC")
    
    root_links = []
    for l in all_links:
        root_links.append({
            "url": l["url"], 
            "label": l["label"],
            "is_active": False
        })
        
    template_data = {
        "date_stamp": date_stamp,
        "total_repos": len(current_repos),
        "repos": current_repos,
        "history_links": root_links,
        "base_path": "", 
        "is_current": True
    }

    html = pystache.render(template, template_data)
    with open("index.html", "w") as f:
        f.write(html)
        
    print("#### index.html and history were generated successfully ####")

if __name__ == "__main__":
    main()
