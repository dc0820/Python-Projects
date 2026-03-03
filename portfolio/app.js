let pyodideInstance = null;

async function loadProjects() {
  const response = await fetch("projects.json");
  if (!response.ok) throw new Error("Failed to load projects.json");
  return response.json();
}

function unique(values) {
  return [...new Set(values)].sort((a, b) => a.localeCompare(b));
}

function appendOutput(text) {
  const out = document.getElementById("runnerOutput");
  out.textContent += text;
  out.scrollTop = out.scrollHeight;
}

async function ensurePyodide() {
  if (pyodideInstance) return pyodideInstance;

  if (!window.loadPyodide) {
    await new Promise((resolve, reject) => {
      const s = document.createElement("script");
      s.src = "https://cdn.jsdelivr.net/pyodide/v0.27.5/full/pyodide.js";
      s.onload = resolve;
      s.onerror = () => reject(new Error("Could not load Pyodide from CDN."));
      document.head.appendChild(s);
    });
  }

  pyodideInstance = await window.loadPyodide();
  return pyodideInstance;
}

async function ensurePackages(pyodide, packages) {
  const needed = (packages || []).filter(Boolean);
  if (!needed.length) return;
  appendOutput(`Loading packages: ${needed.join(", ")}...\n`);
  await pyodide.loadPackage(needed);
}

async function loadRuntimeFiles(project) {
  if (!project.runtimeFile) {
    throw new Error("No runtime bundle found for this project.");
  }
  const response = await fetch(project.runtimeFile);
  if (!response.ok) {
    throw new Error(`Failed to load runtime bundle: ${project.runtimeFile}`);
  }
  return response.json();
}

async function runInBrowser(project) {
  const title = document.getElementById("runnerTitle");
  const out = document.getElementById("runnerOutput");
  title.textContent = `Web Runner - ${project.name}`;
  out.textContent = "Starting...\n";

  try {
    const pyodide = await ensurePyodide();
    appendOutput("Python runtime ready.\n");
    await ensurePackages(pyodide, project.webPackages);

    pyodide.globals.set("js_prompt", (message) => {
      const v = window.prompt(String(message || ""), "");
      return v === null ? "" : v;
    });

    const webFiles = await loadRuntimeFiles(project);

    try { pyodide.FS.rmdir("/project"); } catch (_) {}
    try { pyodide.FS.mkdir("/project"); } catch (_) {}

    for (const file of webFiles) {
      const fullPath = `/project/${file.path}`;
      const parts = fullPath.split("/").filter(Boolean);
      let current = "";
      for (const p of parts.slice(0, -1)) {
        current += `/${p}`;
        try { pyodide.FS.mkdir(current); } catch (_) {}
      }
      pyodide.FS.writeFile(fullPath, file.code, { encoding: "utf8" });
    }

    const runnerCode = `
import io
import os
import sys
import builtins

_stdout = io.StringIO()
_stderr = io.StringIO()
_old_out = sys.stdout
_old_err = sys.stderr
_old_input = builtins.input

sys.stdout = _stdout
sys.stderr = _stderr


def _inp(prompt=''):
    return js_prompt(prompt)

builtins.input = _inp

try:
    os.chdir('/project')
    if os.path.exists('main.py'):
        with open('main.py', 'r', encoding='utf-8') as f:
            src = f.read()
        ns = {'__name__': '__main__'}
        exec(compile(src, 'main.py', 'exec'), ns, ns)
    else:
        print('main.py not found in bundled project files.')
except SystemExit:
    pass
finally:
    sys.stdout = _old_out
    sys.stderr = _old_err
    builtins.input = _old_input

_stdout.getvalue() + _stderr.getvalue()
`;

    const result = await pyodide.runPythonAsync(runnerCode);
    appendOutput(result || "(Program finished with no output)\n");
  } catch (err) {
    out.innerHTML = `<span class="error">${String(err.message || err)}</span>`;
  }
}

function render(projects, state) {
  const grid = document.getElementById("grid");
  const count = document.getElementById("count");
  const template = document.getElementById("cardTemplate");

  const filtered = projects.filter((p) => {
    const trackMatch = state.track === "all" || p.track === state.track;
    const q = state.query.trim().toLowerCase();
    const queryMatch =
      !q ||
      p.name.toLowerCase().includes(q) ||
      p.path.toLowerCase().includes(q) ||
      (p.tags || []).join(" ").toLowerCase().includes(q);
    return trackMatch && queryMatch;
  });

  grid.innerHTML = "";
  filtered.forEach((project) => {
    const node = template.content.firstElementChild.cloneNode(true);
    node.querySelector(".track").textContent = project.track;
    node.querySelector(".kind").textContent = project.kind;
    node.querySelector(".name").textContent = project.name;
    node.querySelector(".path").textContent = project.path;

    const tags = node.querySelector(".tags");
    (project.tags || []).forEach((tag) => {
      const chip = document.createElement("span");
      chip.className = "tag";
      chip.textContent = tag;
      tags.appendChild(chip);
    });

    const note = node.querySelector(".note");
    if (project.webRunnable) {
      const bundleMsg = project.bundleCount ? ` | auto-bundled: ${project.bundleCount}` : "";
      note.textContent = `Browser compatible${bundleMsg}.`;
    } else {
      note.textContent = project.webReason || "Not browser compatible.";
    }

    const runBtn = node.querySelector(".run-web");
    if (project.webRunnable) {
      runBtn.addEventListener("click", () => runInBrowser(project));
    } else {
      runBtn.disabled = true;
      runBtn.textContent = "Desktop Only";
    }

    node.querySelector(".run").textContent = project.run;
    grid.appendChild(node);
  });

  count.textContent = `${filtered.length} project${filtered.length === 1 ? "" : "s"}`;
}

function setupFilters(projects) {
  const search = document.getElementById("search");
  const track = document.getElementById("trackFilter");
  const clearOutput = document.getElementById("clearOutput");
  const output = document.getElementById("runnerOutput");

  unique(projects.map((p) => p.track)).forEach((value) => {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = value;
    track.appendChild(option);
  });

  const state = { query: "", track: "all" };
  render(projects, state);

  search.addEventListener("input", (e) => {
    state.query = e.target.value;
    render(projects, state);
  });

  track.addEventListener("change", (e) => {
    state.track = e.target.value;
    render(projects, state);
  });

  clearOutput.addEventListener("click", () => {
    output.textContent = "";
  });
}

(async () => {
  try {
    const projects = await loadProjects();
    setupFilters(projects);
  } catch (err) {
    const grid = document.getElementById("grid");
    grid.innerHTML = `<p class="error">${err.message}</p>`;
  }
})();
