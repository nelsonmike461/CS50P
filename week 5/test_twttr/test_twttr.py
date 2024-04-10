from twttr import shorten


def test_assert():
    assert shorten("Nelson Michael") == "Nlsn Mchl"
    assert shorten("NELSON MICHAEL") == "NLSN MCHL"
    assert shorten("h3ll0 w0rld") == "h3ll0 w0rld"
    assert shorten("h@llo w*rld!!!") == "h@ll w*rld!!!"
