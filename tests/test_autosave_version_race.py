import pytest
import gameplay.autosave_version_race as mod

CASES = [
    ("write_lock", (1)),
    ("atomic_replace", (1)),
    ("migrate_up", (1)),
    ("halfwrite_check", (1)),
    ("merge_policy", (1)),
    ("rollback_last", (1)),
    ("sequence_no", (1)),
    ("validation", (1)),
    ("audit", (1)),
    ("fallback", (1)),
    ("checksum", (1)),
    ("metrics", (1)),
    ("schema_guard", (1)),
    ("concurrent_manual", (1)),
    ("determinism", (1)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
