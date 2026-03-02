from app import sanitise_input


class TestInputSanitisation:
    """Tests for input sanitisation."""

    def test_strips_whitespace(self):
        """Leading and trailing whitespace should be removed."""
        assert sanitise_input("  hello  ") == "hello"

    def test_rejects_whitespace_only(self):
        """Messages with only whitespace should be rejected."""
        assert sanitise_input("     ") is None
        assert sanitise_input("\n\t\n") is None

    def test_strips_html_tags(self):
        """HTML tags should be removed."""
        assert sanitise_input("<b>hello</b>") == "hello"
        assert sanitise_input("<script>alert('x')</script>") == "alert('x')"

    def test_rejects_too_long(self):
        """Messages over 500 chars should be rejected."""
        assert sanitise_input("a" * 501) is None
        assert sanitise_input("a" * 500) == "a" * 500
