from analyzer import analyze_url_complete
from checks.url_checks import validate_url 
from report import print_report 

url = input("Enter a URL: ")

if not validate_url(url):
    print("\nInvalid URL")
    print("Please enter a complete URL such as:")
    print("https://example.com")
    exit()

result = analyze_url_complete(url)

print_report(url, result)