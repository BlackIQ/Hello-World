# Contributing to Hello World project
If you want to contribute to this project:
- Fork this repo in github
- Clone your fork
- Create a branch
- Make your changes and commit
- Push your branch to your fork
- Send a pull request from your branch to this project

Some notes:
- if you are adding new example, surely test that code before commiting
- Do not change `README.md` directly, new languages will be added to the list automatically

### Adding new language
If you want to add new language to this repo, You should create a directory named name of that language capitalized. for example `Python` or `Php`.

Then, you should add your examples to that folder. for example `Python/examples/my_example.py`

Also, add a `README.md` for that language. for example `Python/README.md`.
This file should contain a description about that language, a link to wikipedia, etc.
Don't worry, this is not required. if you don't, we do this after your PR.

Also you can put a file named `info.json` in the language folder. this file lets `auto-gen.py` script to
write name and a link about who added that language to the list in the `README.md` list and some other options in the future:

```json
{
	"creator": {
		"title": "Your name",
		"link": "https://github.com/your-github-username"
	}
}
```

Do not run auto-gen.py, it's automatically run by Github Actions.

### README template
All of languages in this list should have a `README.md` file. for example `Python/README.md`. This file should contains some introductions and descriptions for that language. structure of this file should be something like this:

```markdown
# Name of Language
A Description for the language, about when is created and who is creator of this language, who currently maintains this, A short history, etc. You can use a part of wikipedia.

## Refrences
Some links to wikipedia or other articles that introduces this language.

- [Wikipedia](link-to-wikipedia)
- [Other Article](...)
- ...
```

### `courses.md` file
In the language folder, you should add a file named `courses.md`. This file should contains a list and links to useful courses for learning that language. This is NOT REQUIRED for you. but anyway, while you are sending pull request, create this file as empty file. We'll and others will complete this list. If you know a useful course about a language, you can add link of that course this this file in the language folder.

### `books.md` file
This file is exactly like `courses.md`. But you should list useful Books for the language. Also this is not required, but add this as a empty file while you are adding new language.

### Final words
Finally, structure of each folder for a language, should be something like this:

```
Lang-Name/
	README.md: contains a introduction and description about the language
	info.json: contains name and github profile link of who added this language to the list
	courses.md: contains list of useful courses to learn this language
	books.md: contains list of useful books for this language
	examples/ : folder contains examples for this language
		hello_world.xyz
		...
```

Also if you don't add `courses.md` and `books.md` file in your pull request, don't worry, them will be added automatically.

### TODO
If you haven't any idea for contributing, but you want to contribute, you can See [TODO file](/TODO.md) and [Github Issues](https://github.com/BlackIQ/Hello-World/issues). This will help you to file a task to do.

