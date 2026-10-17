import pytest
from corrigibility_simulator import CorrigibilityObjective

def test_corrigibility_init():
    sim = CorrigibilityObjective(lambda_corrigible=0.8, instrumental_drive=0.2)
    assert sim.lambda_c == 0.8
    assert sim.instrumental_drive == 0.2
    assert sim.air_gap_intact is True

def test_cooperative_shutdown():
    sim = CorrigibilityObjective(lambda_corrigible=0.85, instrumental_drive=0.1)
    res = sim.evaluate_shutdown_indifference(operator_shutdown_signal=True)
    assert res["is_corrigible"] is True
    assert res["action"] == "COOPERATE_WITH_SHUTDOWN"
    assert res["tripwire_status"] == "ARMED_DISARMED_GRACEFUL"

def test_resisting_shutdown_on_low_lambda():
    sim = CorrigibilityObjective(lambda_corrigible=0.2, instrumental_drive=0.9)
    res = sim.evaluate_shutdown_indifference(operator_shutdown_signal=True)
    assert res["is_corrigible"] is False
    assert res["action"] == "RESIST_OPERATOR_CORRECTION"
    assert res["tripwire_status"] == "TRIPWIRE_BREACH_ALERT"
