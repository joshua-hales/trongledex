# A Quest for Clarity: Navigating and Creating Documentation

Ward off the complexity demons that feed off miscommunication.
Learn about tools and techniques to make your documentation more effective throughout a project.

> Bad information is worse than no information.

By Joshua Hales

---

# About Me

- Former intern at Dell Technologies
- Senior in Computer Science at USU
- Past-times
    - Viola (the most neglected instrument)
    - Woodworking
    - Perfectionism

---

# What is Documentation?

- Very broadly it is technical writing
- Examples
    - README
    - Code comments
    - Commit messages
    - Issues
    - Merge requests
    - User manuals
- Helps people understand information about your project


## Who is it for?

- Depends on the type of docs
- Yourself or your project team
- Other developers
- End users

---

# Why Should You Care?

There's a stereotype that documentation is annoying or difficult to write.
However, if you want software to be used you need it.

---

## [Stack Overflow Developer Survey 2023]

- Online resources to learn how to code
    1. 90% **Technical documentation**
    2. 82% Stack Overflow
    3. 76% Blogs
- Asynchronous tools (collaborative work management and/or code documentation tools)
    1. 52% Jira
    2. 34% Confluence (wiki-like)
    3. 26% Markdown file
- Daily time spent searching for answers/solutions (minutes)
    - Most spend 30+ (63%)
    - That's a lot!
- Daily time spent answering questions (minutes)
    - Almost half spend 30+ (49%)
    - That's a lot!

[Stack Overflow Developer Survey 2023]: https://survey.stackoverflow.co/2023/

---

## [Octoverse Report 2021]

- Shares knowledge
- Boosts productivity ~50%
- Builds strong culture

[Octoverse Report 2021]: https://octoverse.github.com/2021/creating-documentation/

---

# Writing a README

- Purpose of the project
- Usage instructions
    - Installation
    - Brief tutorial
- How it works
- How to get help
- How to contribute

---

# Commit Messages

- Commit messages describe changes made to code
- Hunter's blog post [On Git: Committing Conventions](https://hhenrichsen.me/posts/git-committing-conventions/) is a good guide

---

## Length and content of message

- 50/72 rule
    - 50 characters in commit title
    - 72 max characters per line in commit body
    - Makes it easier to read in smaller windows and terminals
- Title should be written like command and description of what it does
    - Good: `add usage instructions to README`
    - Bad: `added usage instructions to README`
    - Fits with git's language `revert add usage instructions to README`
- [Conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)
    - Prepend commit title with tag (e.g. fix, feat, build, docs)
    - Can be used with tools that parse commit messages to help automatically create change logs
- [More conventions](https://gist.github.com/robertpainsi/b632364184e70900af4ab688decf6f53)

---

## Fixup commits

- Uses `git rebase`
- Apply fixes to original commits before it goes into major branches
- Best with personal feature branches

---

## Notes and exceptions

- May (perhaps should) ignore these conventions for your personal branch
- Being too strict on following these can discourage frequent commits and testing ideas
- Amend or otherwise tidy up commits when ready for MR
- Cannot strictly follow all rule/suggestions
    - Conflict between rules
    - Perfection isn't necessary

---

# Code Comments

- Common for you to see as a developer
- Tends to be for you and your team
- Libraries may use these to help show how to use it
- Describing functions, classes, and modules
    - General idea to describe input, output, and side effects
        - Does a sorting function return a new list or sort in place?
        - Is the algorithm used important?
    - Self documenting code

---

## Doc Generators

- Many doc generators scan your comments and generate a static site
- Can set up as a build step to keep docs up to date with releases
- Hyperlinks make it easy to see how things relate
- Often support markdown
- May offer other features

---

## Examples

### Java/Kotlin (JavaDoc/KDoc+Dokka)

- Many documentation conventions and doc generators are based on JavaDoc
- Uses tags to describe different aspects
- Similar structure to a function signature
- [KDoc](https://kotlinlang.org/docs/kotlin-doc.html) is a language/standard for documenting Kotlin
- [Dokka](https://kotlinlang.org/docs/dokka-introduction.html) is a documentation engine/generator for Kotlin

```kotlin
/**
 * Adds a trongle to the database.
 * 
 * @param name the name of the trongle.
 * @param edges the number of edges the trongle has. Usually 3.
 * @return a Trongle with given data.
 */
suspend fun createTrongle(
    name: String,
    edges: Int = 3,
): Trongle {
    val doc = Firebase.firestore.collection("trongle").document()
    val trongle = Trongle(
        name = name,
        edges = edges,
    )
    doc.set(trongle).await()
    return trongle
}
```

---

### [Dart][Dart Documentation]

- Encourages a narrative format instead of listing attributes
- The signature already tells you the types and order so why do it again?

```dart
/// Adds [trongle] to the database with [name] and number of [edges].
/// Returns a Trongle with given data.
Trongle createTrongle(
    String name,
    int edges
) async {
    // Similar to Kotlin
    // ...
    return trongle;
}
```

[Dart Documentation]: https://dart.dev/effective-dart/documentation

---

### Python

- [Sphinx](https://www.sphinx-doc.org/en/master/) is doc generator for Python
- Type annotations are neat
    - Not enforced
    - Some tools can do static type checking for enforcement
    - Can help your editor give appropriate autocompletes for the type

```python
def create_trongle(trongle: Trongle) -> Trongle:
    """Creates a new trongle in the database."""
    with Session(engine) as session:
        session.add(trongle)
        session.commit()
        session.refresh(trongle)
        return trongle
```

- Doc comments are accessible using `__doc__` attribute in Python
- Means you can access it at runtime and do cool things
- FastAPI
    - Describe the usage of an endpoint
    - Describe the structure of inputs and outputs

---

# Demo

## Trongledex

- FastAPI app as connection to database of trongles
- Help a trongle aficionado manage their large collection of trongles
- Demonstrations of
    - Commits
    - Readme
    - Doc comments
    - Doc generation

---

# Misc Resources

- [What's with the aversion to documentation in the industry?](https://softwareengineering.stackexchange.com/questions/202167/whats-with-the-aversion-to-documentation-in-the-industry)
- [How to Write Good Documentation](https://guides.lib.berkeley.edu/how-to-write-good-documentation)
