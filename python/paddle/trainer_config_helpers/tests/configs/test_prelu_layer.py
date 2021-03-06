#  Copyright (c) 2018 PaddlePaddle Authors. All Rights Reserve.
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
from paddle.trainer_config_helpers import *

data = data_layer(name='input', size=300, height=10, width=10)
prelu = prelu_layer(input=data, num_channels=3)
prelu = prelu_layer(input=data, partial_sum=1, num_channels=3)
prelu = prelu_layer(input=data, partial_sum=5, num_channels=3)
prelu = prelu_layer(input=data, channel_shared=True, num_channels=3)
prelu = prelu_layer(input=data, channel_shared=False, num_channels=3)

outputs(prelu)
