import re
import subprocess
import tempfile
from cStringIO import StringIO

import validator.testcases.javascript.traverser as traverser
from validator.testcases.javascript.spidermonkey import get_tree, \
                                                        JSReflectException
from validator.constants import PACKAGE_THEME, SPIDERMONKEY_INSTALLATION
from validator.contextgenerator import ContextGenerator
from validator.textfilter import *


JS_ESCAPE = re.compile(r"\\+[ux]", re.I)


def test_js_file(err, filename, data, line=0, context=None, pollutable=False):
    """Test a JS file by parsing and analyzing its tokens."""

    if SPIDERMONKEY_INSTALLATION is None or \
       err.get_resource("SPIDERMONKEY") is None:  # Default value is False
        return

    tree = get_tree(
        data, filename=filename, err=err,
        shell=(err and err.get_resource("SPIDERMONKEY")) or
              SPIDERMONKEY_INSTALLATION)

    if not tree:
        return

    return test_js_tree(err, filename, data, tree, line, context, pollutable)


def test_js_tree(err, filename, data, tree, line=0, context=None,
                 pollutable=False):
    """Test a JS file's parse tree."""

    before_tier = None
    # Set the tier to 4 (Security Tests)
    if err is not None:
        before_tier = err.tier
        err.set_tier(3)

    # Generate a context if one is not available.
    if context is None:
        context = ContextGenerator(data)

    if err.detected_type == PACKAGE_THEME:
        err.warning(
                err_id=("testcases_scripting",
                        "test_js_file",
                        "theme_js"),
                warning="JS run from theme",
                description="Themes should not contain executable code.",
                filename=filename,
                line=line)

    t = traverser.Traverser(
        err, filename, line, context=context,
        is_jsm=filename.endswith(".jsm") or "EXPORTED_SYMBOLS" in data)
    t.pollutable = pollutable
    t.run(tree)

    # Reset the tier so we don't break the world
    if err is not None:
        err.set_tier(before_tier)


def test_js_snippet(err, data, filename, line=0, context=None):
    "Process a JS snippet by passing it through to the file tester."

    if not data.strip():
        return

    # Wrap snippets in a function to prevent the parser from freaking out
    # when return statements exist without a corresponding function.
    data = "(function(){%s\n})()" % data

    # NOTE: pollutable is set to True...for now
    test_js_file(err, filename, data, line, context, pollutable=True)

