import validator.testcases.markup.csstester as csstester

from helper import TestCase


class TestCSSTestCases(TestCase):
    """
    Test that the CSS test cases are properly flagging unscrupulous CSS
    snippets.
    """

    def _test_file(self, path):
        """Test a CSS file for errors."""
        with open(path) as css_file:
            self._test_snippet(css_file.read())

    def _test_snippet(self, data):
        """Test a snippet of CSS for errors."""
        if self.err is None:
            self.setup_err()

        csstester.test_css_file(self.err, "css.css", data)

    def test_pass(self):
        """Test that a valid CSS file is not flagged."""
        self._test_file("tests/resources/markup/csstester/pass.css")
        self.assert_silent()

    def test_css_moz_binding_remote(self):
        """Test that remote scripts in moz-binding are blocked."""
        self._test_file("tests/resources/markup/csstester/mozbinding.css")
        self.assert_failed(with_warnings=True)

    def test_css_moz_binding_local(self):
        """Test that local scripts in moz-binding are not flagged."""
        self._test_file("tests/resources/markup/csstester/mozbinding-pass.css")
        self.assert_silent()

    def test_css_identitybox(self):
        """Test that modifications to the identity box are flagged."""
        self._test_file("tests/resources/markup/csstester/identity-box.css")
        self.assert_failed(with_warnings=True)

    def test_css_remote_urls(self):
        """Test that remote URLs within CSS are flagged."""

        is_remote_url = lambda s: csstester.BAD_URL.match(s) is not None

        def passes(snippet):
            def wrap(snippet):
                assert not is_remote_url(snippet), \
                        "`%s` should not be flagged as remote."
            return wrap, snippet

        def fails(snippet):
            def wrap(snippet):
                assert is_remote_url(snippet), \
                        "`%s` should be flagged as remote."
            return wrap, snippet

        yield passes("url(foo/bar.abc)")
        yield passes('url("foo/bar.abc")')
        yield passes("url('foo/bar.abc')")

        yield passes("url(chrome://foo/bar)")
        yield passes("url(resource:asdf)")

        yield fails("url(http://abc.def)")
        yield fails("url(https://abc.def)")
        yield fails("url(ftp://abc.def)")
        yield fails("url(//abcdef)")
        yield passes("url(/abc.def)")

        yield passes("UrL(/abc.def)")
        yield fails("url(HTTP://foo.bar/)")

    def test_css_

