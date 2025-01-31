# demonstrate template string functions

from string import Template

def main():
    # Usual string formatting with format()
    str1 = "I'm watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)

    title = "Advanced Python"
    author = "Joe Marini"
    str2 = f"I'm watching {title} by {author}"
    print(str2)
    
    # TODO: create a template with placeholders
    template = Template("I'm watching ${title} by ${author}")
    
    # TODO: use the substitute method with keyword arguments
    str3 = template.substitute(title=title,author=author)
    print(str3)
    
    # TODO: use the substitute method with a dictionary
    data = {
        "title": "Advanced Python",
        "author": "Joe Marini"
    }
    str4 = template.substitute(data)
    print(str4)
    
if __name__ == "__main__":
    main()
    