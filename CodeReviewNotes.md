# Code Review Notes 
## (given by Janis during my Scram days)


* Docstrings


* Not Implemented Error/ logging for functionality stubs


* Methodology for refactor, example with `.show` and `._exec` changes


* Return `True`/`False` directly instead of (i.e. `return condition()`)


`if condition():
	return True
else:
	return False`


* Checks vs explicit non-truthiness, prefer:


`if not boolean_returning_function():` 
instead of `if boolean_returning_function() is False`


* Put member variable definitions in `__init__`, this is a convention that people expect


* Enumerate for-loop variable counts


Suggest reading [compression oriented programming article/blog post(https://caseymuratori.com/blog_0015) about when to refactor into methods/functions/macros etc.


* Prefer version control over commenting out lines of code, this prevents a number of issues with dead code and code that gets out of sync with changes.


* Shadowing built in names is possible but bad practice with variable names.


* Make `git commits` regularly after changes this makes it much easier to revert bad changes without affecting other code. It also gives you the power to use tools like `git bisect` to quickly find the point at which something changed.


* [For Python] You may find that `excepthook` and the logging package/module are useful for handling those crashes from unhandled exceptions and generating the debugging info.





