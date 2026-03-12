import json
import pystache
import datetime
from datetime import timezone

def main():
    with open("created_issues_report.json", "r") as f:
        data = json.load(f)

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

    now = datetime.datetime.now(timezone.utc)
    date_stamp = now.strftime("%B %d, %Y at %H:%M UTC")

    template_data = {
        "date_stamp": date_stamp,
        "total_repos": len(repos),
        "repos": repos
    }

    with open("template.mustache", "r") as f:
        template = f.read()

    html = pystache.render(template, template_data)

    with open("index.html", "w") as f:
        f.write(html)
        
    print("#### index.html was generated successfully ####")

if __name__ == "__main__":
    main()
