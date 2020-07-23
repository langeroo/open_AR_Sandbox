from sandbox import _calibration_dir as calib_dir
from sandbox.sensor import Sensor
import numpy as np

def test_init_kinect_v1():
    """ Test if detects the kinect 1"""
    sensor = Sensor(name='kinect_v1')
    # print(sensor.get_frame(), sensor.get_frame().shape)
    assert sensor.get_frame().shape == (240, 320)

def test_init_kinect_v2():
    """Test if detects the kinect 2"""
    sensor = Sensor(name='kinect_v2')
    # print(sensor.get_frame(), sensor.get_frame().shape)
    assert sensor.get_frame().shape == (424, 512)

def test_init_dummy():
    sensor = Sensor(name='dummy', random_seed=1234)
    print(sensor.depth[0, 0],
          sensor.depth[0, 0],
          sensor.depth[0, 0])
    assert sensor.depth[0, 0] == 1314.7485240531175

def test_save_load_calibration_projector():
    sensor = Sensor(name='dummy')
    file = calib_dir + 'test_sensor_calibration.json'
    sensor.save_json(file=file)
    # now to test if it loads correctly the saved one
    sensor2 = Sensor(name='dummy', calibsensor=file)

def test_get_frame_croped_clipped():
    sensor = Sensor(name='dummy', crop_values=True, clip_values=True)
    frame = sensor.get_frame()
    print(frame.shape,  frame)
    assert frame.shape == (404, 492)

def test_extent_property():
    sensor = Sensor(name='dummy')
    print(sensor.extent)
    assert np.allclose(np.asarray([0, 492, 0, 404, 700, 1500]), sensor.extent)


