# Copyright 2019 The ROBEL Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Unit tests for D'Claw turn tasks."""

from absl.testing import absltest
from absl.testing import parameterized
import gym
import numpy as np

from gcsl_dependencies.robel.dclaw.turn import (DClawTurnFixed, DClawTurnRandom,
                                   DClawTurnRandomDynamics)
# pylint: disable=no-member


@parameterized.parameters(
    ('DClawTurnFixed-v0', DClawTurnFixed),
    ('DClawTurnRandom-v0', DClawTurnRandom),
    ('DClawTurnRandomDynamics-v0', DClawTurnRandomDynamics),
)
class DClawTurnTest(absltest.TestCase):
    """Unit test class for RobotEnv."""

    def test_gym_make(self, env_id, env_cls):
        """Accesses the sim, model, and data properties."""
        env = gym.make(env_id)
        self.assertIsInstance(env.unwrapped, env_cls)

    def test_spaces(self, _, env_cls):
        """Checks the observation, action, and state spaces."""
        env = env_cls()
        observation_size = np.sum([
            9,  # claw_qpos
            1,  # object_x
            1,  # object_y
            9,  # last_action
            1,  # target_error
        ])
        self.assertEqual(env.observation_space.shape, (observation_size,))
        self.assertEqual(env.action_space.shape, (9,))
        self.assertEqual(env.state_space['claw_qpos'].shape, (9,))
        self.assertEqual(env.state_space['claw_qvel'].shape, (9,))
        self.assertEqual(env.state_space['object_qpos'].shape, (1,))
        self.assertEqual(env.state_space['object_qvel'].shape, (1,))

    def test_reset_step(self, _, env_cls):
        """Checks that resetting and stepping works."""
        env = env_cls()
        env.reset()
        env.step(env.action_space.sample())


if __name__ == '__main__':
    absltest.main()
