# Frequently Asked Questions

## How do I install BDXpy?
Use pip:
```bash
pip install bdxpy
```
See the [installation section](https://buildinglogix.github.io/BDXpy/getting-started/#installation).

## How do use BDXpy?
See our workflow diagram for getting started: [workflow bdxpy](https://buildinglogix.github.io/BDXpy/getting-started/#process-overview-from-bdx-to-bdxpy-and-python-outputs).

## Do I have to pay for BDXpy?
BDXpy requires an active BDX license including the license feature for RemoteAPI.
Installation of the Python package BDXpy is free and publicly available as well as all documentation and some basic examples to get users started.

## What if I don't know Python?
Python is one of the most widely used [programming languages](https://www.statista.com/statistics/793628/worldwide-developer-survey-most-used-languages/) and is open-source. It has many resources, classes, examples online beginners can pull from.
Likewise most AI chatbots like ChatGPT, Gemini, etc. all generally quite good a Python development and we highly encourage beginners to utilize all these available tools.  

BuildingLogiX is also working on forming a dedicated BDXpy custom GPT, coming soon.....

## What are IDEs, which one should I use for BDXpy?
An IDE (Integrated Development Environment) is a software application that provides coding tools, such as syntax highlighting, debugging, and auto-completion, to make development easier.

For working with BDXpy, most of our team uses VS Code most of the time or Jupyter Notebook in VS Code. There are others we also recommend depending on your experience and preference:

- **VS Code** – Lightweight, customizable, and great for Python development.
- **PyCharm** – More feature-rich, with advanced debugging and code analysis.
- **Jupyter Notebook** – Best for interactive data analysis and quick visualizations.
- **Spyder** – Designed for data science, similar to MATLAB.  

👉 Recommendation: If you need a full-fledged Python IDE, VS Code or PyCharm is great. If you are doing data exploration, try Jupyter Notebook.

## What is the difference between Python and Jupyter Notebook files?
- **Python scripts (.py):**
    - Standard Python files used for writing and executing programs.
Run using a terminal, command line, or an IDE like VS Code/PyCharm.
Best for larger projects and production-ready code.
- **Jupyter Notebooks (.ipynb):**
    - An interactive environment that allows you to mix code, markdown, and visualizations.
Best for data analysis, quick prototyping, and educational purposes.
Supports inline plots (like matplotlib and seaborn).  

👉 Recommendation: Use .py for software development and .ipynb for analysis, documentation, or interactive work.

## Can BuildingLogiX help me develop in Python?
Yes, BuildingLogiX has in-house developers and engineers who are happy to assist. IF you want to collarborate on BDXpy development it is considered custom development and involves working directly with our team! We will also likely have a series of small training seminars annual on BDXpy.
Reach out to us if you are interested.


## I’m getting an HTTP error when trying to connect to BDX — what does it mean?

BDXpy communicates with your **BDX platform server** over HTTPS. When HTTP errors occur, they usually indicate a **server connection**, **authentication**, or **licensing** issue.  
Below are common causes and solutions.

---

### 🔑 401 Unauthorized or 403 Forbidden

**Possible causes:**
- Invalid username or password.  
- Missing or expired BDX license.  
- Your BDX account does not have the RemoteAPI feature enabled.  
- The BDX server is enforcing HTTPS and the client attempted an HTTP connection.

**Fixes:**
- Confirm your credentials in your `.env` or authentication code:
  ```python
  from bdx.auth import UsernameAndPasswordAuthenticator
  auth = UsernameAndPasswordAuthenticator("your_username", "your_password")
  ```
- Make sure your BDX license includes the **RemoteAPI** feature.  
- Check with your administrator that your user role permits API access.  
- Use a proper HTTPS URL, e.g. `https://your-bdx-server.com`.

---

### 🚫 404 Not Found

**Possible causes:**
- Incorrect BDX site URL or server path.  
- The BDX site has not deployed the `/bdx/rest/...` API endpoints.  
- You are connecting to the wrong tenant or environment (e.g., dev vs prod).

**Fixes:**
- Double-check the `host_url` you are using:
  ```python
  bdx = BDX("https://your-bdx-server.com", auth)
  ```
- Confirm that the BDX server is online and accessible.  
- If your instance is behind a VPN or proxy, ensure your client can reach it.

---

### ⚙️ 500 Internal Server Error / 502 / 503 / 504

**Possible causes:**
- The BDX server encountered an internal failure.  
- There are network proxy issues between your client and server.  
- SSL/TLS certificate on the server is invalid or expired.  
- The BDX service may be restarting or under maintenance.

**Fixes:**
- Verify that your server certificate is valid (especially for on-prem installations).  
- Restart the BDX site or check its service health via `/bdx/unrestricted/rest/management/monitoring/summary`.  
- Try again later—some errors resolve after the server finishes restarting.  
- For corporate or on-prem servers, contact your system admin to check service logs.

---

### 🧾 Licensing & BDXpy Access

**Key distinction:**
- The **BDX platform license** controls access to the API.  
- The **BDXpy Python package** is open-source and free to install via pip:
  ```bash
  pip install bdxpy
  ```
  However, BDXpy requires your BDX server to have **an active BDX license with RemoteAPI enabled**.

**Fixes:**
- Contact BuildingLogiX Support to verify that your BDX site has valid licensing for API use.  
- If you can log into the BDX web interface but cannot authenticate via Python, your RemoteAPI feature is likely disabled.

---

### 🔐 Authentication Failures (MFA, Expired Session, etc.)

**Possible causes:**
- MFA is required but not configured in your script.  
- The user’s session has expired.  
- The password has changed since the last stored `.env` update.

**Fixes:**
- Use `UsernameAndPasswordAuthenticator` to refresh credentials each session.  
- Avoid storing plaintext passwords—use an `.env` file or encrypted secret.  
- If MFA is enabled, check for MFA code support (BDXpy currently supports static username/password only).

---

### 🌐 Connection or Certificate Issues

**Possible causes:**
- Invalid SSL certificate on the BDX server.  
- Self-signed certificate without being trusted by the client.  
- Firewall or proxy interference.

**🧪 Quick test only: temporarily ignore SSL verification (insecure):**
- If using a **self-signed certificate**, either:
  - Install it as a trusted certificate on your machine, or  
  - Disable SSL verification *temporarily* for testing:
    ```python
    import urllib3
    from bdx.core import BDX
    from bdx.auth import UsernameAndPasswordAuthenticator

    def make_session_insecure(sess):
        # Silence the "InsecureRequestWarning"
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        # Tell Requests not to verify TLS certs on this session
        sess.verify = False

    auth = UsernameAndPasswordAuthenticator("username", "password")

    # Works the same if you have a convenience helper like get_bdx()
    with BDX("https://your-bdx-server", auth) as bdx:
        # Force SSL ignore at the adapter/session level (affects all calls on THIS session)
        make_session_insecure(bdx.session)

        # Optional: ping triggers auth and populates version internally
        try:
            print("BDX version:", bdx.platform_version)
        except Exception as ex:
            print("[warn] version check failed:", type(ex).__name__, ex)

        # ... now make your data calls, e.g. fetch_daily_cycle_counts(...)

    ```
    ⚠️ *Not recommended for production use!*
- If behind a corporate proxy, configure `HTTP_PROXY` and `HTTPS_PROXY` environment variables.

---

### 🧠 Tip: Test Basic Connectivity

To verify your setup without running a full data call:
```python
from bdx.auth import UsernameAndPasswordAuthenticator
from bdx.core import BDX

auth = UsernameAndPasswordAuthenticator("username", "password")
bdx = BDX("https://your-bdx-server.com", auth)
print(bdx.platform_version)
```

If this fails, it helps identify whether the problem is **authentication**, **network**, or **licensing**.

---




## Who can I contact for support?
Email us at technical.support@buildinglogix.net.