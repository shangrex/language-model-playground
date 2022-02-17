"""Test :py:mod:`lmp.model` signatures."""

import lmp.model


def test_module_attribute() -> None:
  """Ensure module attributes' signatures."""
  assert hasattr(lmp.model, 'BaseModel')
  assert hasattr(lmp.model, 'ElmanNet')
  assert hasattr(lmp.model, 'LSTM1997')
  assert hasattr(lmp.model, 'LSTM2000')
  assert hasattr(lmp.model, 'LSTM2002')
  assert hasattr(lmp.model, 'ALL_model')
  assert lmp.model.ALL_modelS == [
    lmp.model.ElmanNet,
    lmp.model.LSTM1997,
    lmp.model.LSTM2000,
    lmp.model.LSTM2002,
  ]
  assert hasattr(lmp.model, 'model_OPTS')
  assert lmp.model.model_OPTS == {
    lmp.model.ElmanNet.model_name: lmp.model.ElmanNet,
    lmp.model.LSTM1997.model_name: lmp.model.LSTM1997,
    lmp.model.LSTM2000.model_name: lmp.model.LSTM2000,
    lmp.model.LSTM2002.model_name: lmp.model.LSTM2002,
  }
