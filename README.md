# Codebase Collection Utility

Python-based CLI utility for recursively collecting source files from project directories and generating consolidated code snapshots for analysis, documentation, archival, or LLM-assisted workflows.

The utility was developed as part of an internal automation toolkit used to prepare large multi-file codebases for structured review, AI-assisted analysis, and debugging workflows.

## Features

- Recursive project directory traversal
- Multi-extension source file filtering
- Consolidated code snapshot generation
- Structured output formatting with file separators
- Automatic output directory creation
- Configurable CLI arguments
- Broad multi-language support
- Graceful unreadable-file handling
- Lightweight zero-dependency implementation

## Tech Stack

- Python
- Standard Library (`os`, `sys`)

## Architecture

```text
Target Project Directory
            ↓
Recursive Directory Traversal
            ↓
Extension-Based File Filtering
            ↓
Source File Collection
            ↓
Structured Output Formatting
            ↓
Consolidated Snapshot Generation
```

## Project Structure

```text
code-collector/
│
├── output/
│
├── copyp.py
├── README.md
└── .gitignore
```

## Supported File Types

Default extension support includes:

- Python
- JavaScript / TypeScript
- HTML / CSS
- SQL
- Java
- C / C++
- C#
- PHP
- Go
- Ruby
- Shell scripts
- Kotlin
- Swift
- Scala
- Lua
- Dart
- Haskell
- Elixir
- Clojure
- and additional common source formats

## Key Components

- Recursive filesystem traversal engine
- Extension normalization utilities
- Structured snapshot formatting logic
- File aggregation workflows
- CLI parameter parsing
- Output generation utilities


## Notes

Designed for developer tooling workflows involving codebase aggregation, AI-assisted inspection, documentation preparation, debugging workflows, and structured archival of multi-file projects. The utility was frequently used during development of internal scraping systems, automation tooling, and patent-analysis platforms involving large modular codebases.
