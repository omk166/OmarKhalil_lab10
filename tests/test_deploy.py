from pathlib import Path
import runpy
import sys

from deploy import deploy


def test_deployment_and_redeployment(tmp_path):
    target = tmp_path / "deployment"
    deployed = deploy(target)
    source = Path(__file__).resolve().parents[1] / "app.py"
    assert deployed.read_bytes() == source.read_bytes()
    deployed.write_text("outdated", encoding="utf-8")
    assert deploy(target).read_bytes() == source.read_bytes()
    assert runpy.run_path(str(deployed))["greet"]("World") == (
        "Hello, World from Omar Khalil!"
    )


def test_deployment_cli(tmp_path, monkeypatch, capsys):
    target = tmp_path / "cli-deployment"
    monkeypatch.setattr(sys, "argv", ["deploy.py", "--target", str(target)])
    runpy.run_module("deploy", run_name="__main__")
    assert (target / "app.py").is_file()
    assert "Deployed application to" in capsys.readouterr().out
