from ObjectiveTest import ObjectiveTest
from SubjectiveTest import SubjectiveTest

subjectiveTest = SubjectiveTest("""As an area of expertise and field, data science is defined as a concept to unify statistics, data analysis and their related methods in order to understand and analyze actual phenomena with data.It employs techniques and theories drawn from many fields within the broad areas of mathematics, statistics, information science, and computer science, in particular from the subdomains of machine learning, statistical classification, cluster analysis, data mining, databases, and visualization.

The degree is relatively new, with graduate schools, business schools, and data science centers often housing the programs. Data science degree programs have emerged to address the growing and unique need for data scientists who can provide insight into multiple organizational issues and interests across several disciplines.

When Harvard Business Review called data scientist The Sexiest Job of the 21st Century the term became a buzzword,[4] and is now often applied to business analytics, or even arbitrary use of data, or used as a term for statistics. While many university programs now offer a data science degree, there exists no consensus on a definition or curriculum contents.""", 3)

print(subjectiveTest.generate_test())