topics = [
    (
        "Founder of C",
        ["dennis", "ritchie", "dennis-ritchie"],
        "Dennis Ritchie was an American computer scientist who was born in Bronxville, New York, in 1941. He graduated from Harvard University with degrees in physics and applied mathematics and later earned a Ph.D. in mathematics. In 1967, he joined Bell Laboratories, where he would make his most significant contributions to the field of computer science. Ritchie is most famous for two pivotal creations: the C programming language and the co-development of the Unix operating system. The C programming language, which he created in the early 1970s, was designed to be a general-purpose, low-level language that could be used for system programming. This led to a key development: he and his colleague Ken Thompson were able to rewrite the Unix kernel in C, making the operating system portable and adaptable to different computer platforms. Throughout his career, Ritchie received numerous honors for his work, including the Turing Award in 1983 and the National Medal of Technology in 1999, both shared with Ken Thompson. He retired in 2007 and passed away in 2011. His legacy endures through the widespread use of Unix and C, which have had a profound and lasting impact on modern computing.",
    ),
    (
        "if else",
        ["if", "if else", "if-else", "decision", "conditional"],
        '✅ IF-ELSE IN C: 👉 Explanation: Decision-making block. Executes code based on condition. 👉 Syntax: ```c if(condition) { // true } else { // false } ``` 👉 Example: ```c int age=20; if(age>=18) printf("Adult"); else printf("Minor"); ``` 👉 To-Do: - Check even/odd - Check positive/negative',
    ),
    (
        "ternary",
        ["ternary", "conditional operator", "short if"],
        '✅ TERNARY OPERATOR: 👉 Syntax: ```c (condition) ? true_result : false_result; ``` 👉 Example: ```c int num=5; printf("%s", (num%2==0)?"Even":"Odd"); ``` 👉 To-Do: - Greater of two numbers - Pass/Fail check',
    ),
    (
        "default",
        [],
        "Sorry Piyush! I don't have that topic yet. Try keywords like: loops, arrays, strings, pointers, recursion, macros, storage classes, etc.",
    ),
]

user_input = input("Enter your topic or keyword: ").lower()

found = False
for title, keywords, response in topics:
    for keyword in keywords:
        if keyword in user_input:
            print(f"{title}:\n{response}")
            found = True
            break
    if found:
        break

if not found:
    for title, keywords, response in topics:
        if title == "default":
            print(response)
            break
