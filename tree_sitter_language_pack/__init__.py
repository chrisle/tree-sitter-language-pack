from importlib import import_module
from typing import Literal

from tree_sitter import Language, Parser

SupportedLanguage = Literal[
    "scala",
    "vue",
    "verilog",
    "bitbake",
    "query",
    "qmldir",
    "xcompose",
    "qml",
    "hare",
    "cairo",
    "markdown",
    "ron",
    "capnp",
    "glsl",
    "go-sum",
    "rust",
    "go-mod",
    "ruby",
    "luap",
    "gpg-config",
    "chatito",
    "hack",
    "svelte",
    "cuda",
    "heex",
    "ssh-config",
    "odin",
    "luau",
    "squirrel",
    "arduino",
    "bash",
    "nqc",
    "luadoc",
    "re2c",
    "starlark",
    "yuck",
    "wgsl-bevy",
    "clarity",
    "hlsl",
    "objc",
    "tcl",
    "css",
    "doxygen",
    "toml",
    "go",
    "po",
    "pymanifest",
    "uxntal",
    "pem",
    "elm",
    "vim",
    "ispc",
    "java",
    "printf",
    "jsdoc",
    "lua",
    "cpp",
    "linkerscript",
    "json",
    "gitattributes",
    "hcl",
    "fortran",
    "test",
    "func",
    "agda",
    "javascript",
    "solidity",
    "readline",
    "elixir",
    "embedded-template",
    "thrift",
    "pony",
    "commonlisp",
    "poe-filter",
    "csv",
    "meson",
    "gstlaunch",
    "julia",
    "php",
    "ungrammar",
    "c-sharp",
    "tablegen",
    "udev",
    "cpon",
    "xml",
    "gn",
    "typescript",
    "c",
    "make",
    "ocaml",
    "requirements",
    "kdl",
    "yaml",
    "puppet",
    "properties",
    "swift",
    "firrtl",
    "html",
    "smali",
    "haskell",
    "bicep",
    "kconfig",
]


def get_language(name: SupportedLanguage) -> Language:
    """Get the language with the given name."""
    try:
        module = import_module(name=f".languages.{name}", package=__package__)
        return Language(module.language())
    except ModuleNotFoundError as e:
        raise LookupError(f"Language not found: {name}") from e


def get_parser(name: SupportedLanguage) -> Parser:
    """Get a parser for the given language name."""
    return Parser(get_language(name))


__all__ = ["get_language", "get_parser", "SupportedLanguage"]