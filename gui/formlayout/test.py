from formlayout import fedit

datalist = [
    ("Name", "Paul"),
    (None, None),
    (None, "Information:"),
    ("Age", 30),
    ("Sex", [0, "Male", "Female"]),
    ("Size", 12.1),
    ("Eyes", "green"),
    ("Married", True),
]

fedit(datalist, title="Describe Yourself", comment="This <b>is</b> an example")
