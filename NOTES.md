Setting up a **VS Code workspace** for a **Django REST API** project involves configuring your development environment for optimal productivity, including settings, extensions, environment management, and debugging. Here's a step-by-step guide:

---

## ✅ 1. **Install VS Code Extensions**

Install these essential extensions from the VS Code marketplace:

Gitlens* **Python** (by Microsoft) – for syntax highlighting, IntelliSense, and debugging.
* **Pylance** – for fast and feature-rich Python language support.
* **Django** – helpful snippets and support.
* **REST Client** (optional) – test APIs directly from VS Code.
* **Black Formatter** or **autopep8** – for code formatting.
* **isort** – organizes imports automatically.
* **Prettier** – optional for frontend (if any).
* **GitLens** – if using Git.

---

## ✅ 2. **Create a Workspace**

In VS Code:

1. Open your project folder.
2. Click **File → Save Workspace As...** and save it as `your_project.code-workspace`.

You can add folder-specific and global settings here.

---

## ✅ 3. **Python Virtual Environment**

Inside the root of your project:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Then install your requirements:

```bash
pip install django djangorestframework
```

Add any others you need (`django-cors-headers`, `psycopg2`, etc.)

---

## ✅ 4. **Configure VS Code Workspace Settings**

Create or edit `.vscode/settings.json`:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "editor.formatOnSave": true,
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  "python.testing.pytestArgs": ["./"],
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true
  }
}
```

On Windows, change the interpreter path to `venv\\Scripts\\python.exe`.

---

## ✅ 5. **Run and Debug Configuration**

Create `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Django",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/manage.py",
      "args": ["runserver"],
      "django": true
    }
  ]
}
```

---

## ✅ 6. **Optional: Tasks for Migrations & Tests**

Create `.vscode/tasks.json` to run commands like migrations and tests:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run Migrations",
      "type": "shell",
      "command": "python manage.py migrate"
    },
    {
      "label": "Run Tests",
      "type": "shell",
      "command": "pytest"
    }
  ]
}
```

Run these via **Terminal > Run Task** or with keybindings.

---

## ✅ 7. **.env File for Secrets (Optional)**

Use the [dotenv VS Code extension](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv), and create a `.env` file:

```env
DJANGO_SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://...
```

Update `settings.py` to load these using `python-decouple` or `os.environ`.

---

## ✅ 8. **Run the Server**

From terminal:

```bash
source venv/bin/activate
python manage.py runserver
```

Or press **F5** to run via VS Code debug.

---

## ✅ 9. **Testing REST APIs**

* Use **Postman** or install the **REST Client** extension.
* Or write Django `TestCase` classes in `tests.py` and run via pytest.

---

Let me know if you want a template `settings.json`, `.env`, or sample REST API project layout.

***Git***
git branch -m master main
git remote add origin https://github.com/InfoLaw56/lawyer_todo_be.git
commit
git push -u origin main

pip freeze > requirements.txt

django-admin startproject lawyer_todo .
python manage.py startapp todo
