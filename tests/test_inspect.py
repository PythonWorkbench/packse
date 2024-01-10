import pytest
from packse import __development_base_path__

from .common import snapshot_command


def test_inspect_no_target_finds_all_valid_scenarios(snapshot):
    assert snapshot_command(["inspect"]) == snapshot


def test_inspect_target_does_not_exist(snapshot):
    assert snapshot_command(["inspect", "foo"]) == snapshot


@pytest.mark.usefixtures("tmpcwd")
def test_inspect_one_target_does_not_exist(snapshot):
    target = __development_base_path__ / "scenarios" / "example.json"
    assert snapshot_command(["inspect", str(target), "foo"]) == snapshot


def test_inspect_invalid_target(snapshot, tmpcwd):
    bad_target = tmpcwd / "test.json"
    bad_target.touch()
    good_target = __development_base_path__ / "scenarios" / "example.json"
    assert snapshot_command(["inspect", str(bad_target), str(good_target)]) == snapshot


def test_inspect_invalid_target_skip_invalid(snapshot, tmpcwd):
    bad_target = tmpcwd / "test.json"
    bad_target.touch()
    good_target = __development_base_path__ / "scenarios" / "example.json"
    assert (
        snapshot_command(
            ["inspect", str(bad_target), str(good_target), "--skip-invalid"]
        )
        == snapshot
    )


def test_inspect(snapshot):
    target = __development_base_path__ / "scenarios" / "example.json"
    assert snapshot_command(["inspect", str(target)]) == snapshot


def test_inspect_short_names(snapshot):
    target = __development_base_path__ / "scenarios" / "example.json"
    assert snapshot_command(["inspect", str(target), "--short-names"]) == snapshot
