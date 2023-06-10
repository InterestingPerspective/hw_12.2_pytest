from utils import dicts


def test_get_val():
    data = {"vcs": "mercurial"}
    assert dicts.get_val(data, "vcs") == "mercurial"
    assert dicts.get_val(data, "vcs", "git") == "mercurial"
    assert dicts.get_val(data, "grt") == "git"
    data = {}
    assert dicts.get_val(data, "vcs", "git") == 'git'
    assert dicts.get_val(data, "vcs", "bazaar") == 'bazaar'
